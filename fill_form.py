"""
Built for filling out a form with random values, so you don't have to keysmash your way
through testing. It begins with a small gui which decides which parts of the form to
fill out. You may or may not need that bit.
"""

import subprocess
# subprocess.run(['notify-send', 'Title', 'Message'])

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

import tkinter as tk
from tkinter import ttk
import random
import string
import time

# Data lists (as before)
import random
import string

def build_structure():
	# this structure defines how the form will be filled out. Using values from the gui, it decides
	# which parts to fill out, and which to skip.
	#
	# caption: for developer use so you can see where you are
	# list: there are several lists from which a value is chosen at random: street names, cities, states
	#		The lists begin at ln 215, and are enumerated for the programs use starting at ln 239
	# func: when more complex processing is needed, you can call a function from here: the output will be used as the value
	# after: if blank, the program will send the output and tab to the next item. If NOT blank, the "after" value
	#		will be appended to the value of the list or function. When a blank is encountered, the collected
	#		values will be inserted and the program tabs to the next item.
	struct = [
		{"caption": "Dealer Name", "list": "dealers", "func": None, "after": ""},
		{"caption": "First Name", "list": "firstnames", "func": None, "after": ""},
		{"caption": "Middle Name", "list": None, "func": lambda: random_letters_numbers(1, 1, flag=4), "after": ""},
		{"caption": "Last Name", "list": "lastnames", "func": None, "after": "-TEST"},
		{"caption": "skip", "list": None, "func": None, "after": ""},
		{"caption": "DOB", "list": None, "func": lambda: generate_random_relative_date_str(-80, -18), "after": ""},
		{"caption": "SSN", "list": None, "func": lambda: ''.join(random_letters_numbers(3, 3, flag=2) for _ in range(3)), "after": ""},
		{"caption": "phone", "list": None, "func": lambda: ''.join(random_letters_numbers(5, 5, flag=2) for _ in range(2)), "after": ""},
		{"caption": "email", "list": "emails", "func": None, "after": ""},
		{"caption": "addr1", "list": None, "func": lambda: random_letters_numbers(3, 6, flag=2), "after": " "},
		{"caption": "addr2", "list": "directions", "func": None, "after": " "},
		{"caption": "addr3", "list": "trees", "func": None, "after": " "},
		{"caption": "addr4", "list": "street_types", "func": None, "after": ""},
		{"caption": "city", "list": "cities", "func": None, "after": ""},
		{"caption": "state", "list": None, "func": lambda: send("<down>", random_letters_numbers(2, 49, flag=2)), "after": ""},
		{"caption": "zip", "list": None, "func": lambda: random_letters_numbers(5, 5, flag=2), "after": ""},
		{"caption": "residence", "list": None, "func": lambda: send("<down>", random_letters_numbers(1, 5, flag=2)), "after": ""},
		{"caption": "years at address", "list": None, "func": lambda: send("<down>", random_letters_numbers(3, 8, flag=2)), "after": ""},
		{"caption": "months at address", "list": None, "func": lambda: send("<down>", random_letters_numbers(2, 11, flag=2)), "after": ""},
		{"caption": "rent", "list": None, "func": lambda: random_letters_numbers(3, 4, flag=2), "after": ""},

		{"caption": "driver license #", "list": None, "func": lambda: random_letters_numbers(5, 8, flag=6), "after": ""},
		{"caption": "license state", "list": None, "func": lambda: send("<down>", random_letters_numbers(2, 49, flag=2)), "after": ""},
		{"caption": "license exp", "list": None, "func": lambda: generate_random_relative_date_str(1, 3), "after": ""},

		{"caption": "employ status", "list": None, "func": lambda: send("<down>", random_letters_numbers(1, 5, flag=2)), "after": ""},
		{"caption": "employer", "list": "employers", "func": None, "after": ""},
		{"caption": "phone", "list": None, "func": lambda: ''.join(random_letters_numbers(5, 5, flag=2) for _ in range(2)), "after": ""},
		{"caption": "job", "list": "occupations", "func": None, "after": ""},
		{"caption": "years", "list": None, "func": lambda: send("<down>", random_letters_numbers(3, 8, flag=2)), "after": ""},
		{"caption": "months", "list": None, "func": lambda: send("<down>", random_letters_numbers(2, 11, flag=2)), "after": ""},
		{"caption": "salary", "list": None, "func": lambda: random_letters_numbers(4, 4, flag=2), "after": ""},

		# if include_sidehustle.get():
		#	 struct.append({"caption": "Side Hustle", "list": "sidehustles", "func": None})
		#other income
	]
	# side hustles - skipping this for now because it's late and I'm beat.
	struct.extend([{"caption": "skip", "list": None, "func": None, "after": ""}] * 3)

	#vehicle of interest
	voi = [
		{"caption": "model year", "list": None, "func": lambda: random_number_between(1970, 2021), "after": ""},
		{"caption": "make", "list": "car_makes", "func": None, "after": ""},
		{"caption": "model", "list": "car_models", "func": None, "after": ""},
		{"caption": "miles", "list": None, "func": lambda: random_number_between(1000, 1000000), "after": ""},
		{"caption": "vin", "list": None, "func": lambda: random_letters_numbers(17, 17, flag=6), "after": ""},
		{"caption": "price", "list": None, "func": lambda: random_number_between(5000, 20000, 500), "after": ""},
		{"caption": "down pmt", "list": None, "func": lambda: random_number_between(1000, 5000, 500), "after": ""},
		# couldn't get the next one to work for some reason, so I'm just skipping it.
		# {"caption": "include title", "list": None, "func": lambda: send("<down>", 1), "after": ""},
		{"caption": "skip", "list": None, "func": None, "after": ""}
	]

	trade = [{"caption": "model year", "list": None, "func": lambda: random_number_between(1970, 2021), "after": ""},
		{"caption": "make", "list": "car_makes", "func": None, "after": ""},
		{"caption": "model", "list": "car_models", "func": None, "after": ""},
		{"caption": "miles", "list": None, "func": lambda: random_number_between(1000, 1000000), "after": ""},
		{"caption": "vin", "list": None, "func": lambda: random_letters_numbers(17, 17, flag=6), "after": ""}
	]

	if include_voi.get():
		struct.extend(voi)
	else:
		struct.extend([{"caption": "skip", "list": None, "func": None, "after": ""}] * 8)

	if include_trade.get():
		struct.extend(trade)
	else:
		struct.extend([{"caption": "skip", "list": None, "func": None, "after": ""}] * 5)

	#trade


	# Add conditional items based on checkboxes
	# if include_cobuyer.get():
	#	 struct.append({"caption": "Co-buyer Name", "list": "firstnames", "func": None})





	return struct


# Minimal data lists
first_names = [
	"Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah",
	"Ian", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oliver", "Paula",
	"Quentin", "Rachel", "Steven", "Tina"
]

last_names = [
	"Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
	"Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
	"Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

city_names = [
	"New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
	"San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
	"Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis",
	"Seattle", "Denver", "Washington"
]

tree_species = [
	"Oak", "Pine", "Maple", "Birch", "Cedar", "Spruce", "Willow", "Poplar",
	"Fir", "Redwood", "Cypress", "Ash", "Elm", "Magnolia", "Spruce", "Sequoia",
	"Hemlock", "Cherry", "Walnut", "Aspen"
]

street_types = [
		"AV", "ST", "BLVD", "LN", "CY"
]

us_state_abbrs = [
	"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
	"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
	"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
	"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
	"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

labels = ["Mortgage", "Rent", "Own", "Family"]

employers = [
	"TechCorp", "HealthPlus", "EcoSolutions", "FinBank", "EduWorld",
	"AutoMakers", "Foodies", "BuildIt", "TravelCo", "MediaHouse",
	"DesignPro", "GreenEnergy", "RetailMart", "FashionHub", "LogiTrans",
	"CyberSecure", "BioGen", "AeroDynamics", "MediaPlus", "SmartHome"
]

occupations = [
	"Engineer", "Doctor", "Teacher", "Nurse", "Architect",
	"Developer", "Designer", "Manager", "Clerk", "Analyst",
	"Consultant", "Chef", "Photographer", "Pilot", "Mechanic",
	"Farmer", "Writer", "Musician", "Lawyer", "Pharmacist"
]

side_hustles = [
	"Dropshipping", "Freelance Writing", "Pet Sitting", "Handmade Crafts",
	"Blogging", "Tutoring", "Ride Sharing", "Photography", "Event Planning",
	"Car Detailing", "Lawn Care", "House Cleaning", "Personal Training",
	"Vlogging", "Online Courses", "Social Media Management", "Voice-over Work",
	"Reselling", "Gardening Services", "Cooking Classes"
]

car_makes = [
	"Zircon", "Vortex", "Nimbus", "Aero", "Catalyst",
	"Fusion", "Quantum", "Nova", "Eclipse", "Spectra",
	"Phoenix", "Vanguard", "Stratus", "Falcon", "Tiger",
	"Steel", "Raptor", "Shadow", "Viper", "Cyclone"
]

car_models = [
	"X1", "Z3", "Q5", "Eclipse", "Falcon",
	"Vortex", "Nimbus", "Ranger", "Pioneer", "Voyager",
	"Summit", "Cobra", "Phantom", "Dragon", "Titan",
	"Blaze", "Iron", "Shadow", "Bolt", "Zephyr"
]

auto_dealers = [
	"Velocity Auto Sales",
	"Premier Car Emporium",
	"Sunrise Auto Mall",
	"Pinnacle Motors",
	"Liberty Auto Boutique",
	"Evergreen Car Center",
	"Skyline Vehicle Hub",
	"Gold Coast Auto",
	"NextGen Auto Group",
	"Silverline Motors",
	"Crestview Car Dealers",
	"Blue Horizon Auto",
	"Urban Drive Motors",
	"Fusion Auto Outlet",
	"Maple Leaf Motors",
	"Highland Auto Plaza",
	"Starlight Car Company",
	"Redwood Auto Sales",
	"Oceanview Motors",
	"Ironclad Auto Traders"
]

emails = [
	"clarkgable@warnerbros.com",
	"humphreybogart@paramount.com",
	"laurencedeep@metro-goldwyn-mayer.com",
	"bingcrosby@warnerbros.com",
	"gretagarbo@paramount.com",
	"johnwayne@universalstudios.com",
	"margaretlockwood@columbiapictures.com",
	"fredastaire@warnerbros.com",
	"kirkdouglas@paramount.com",
	"carygrant@universalstudios.com",
	"vivienleigh@metro-goldwyn-mayer.com",
	"garycooper@columbiapictures.com",
	"joancranford@paramount.com",
	"bettepage@warnerbros.com",
	"fredmcmurray@universalstudios.com",
	"clairetrevor@paramount.com",
	"boriskarloff@losangeles.gov",
	"lonchaney@newyorkcity.org",
	"glennstrange@boston.gov",
	"belalugosi@chicago.gov"
]

# List of all data structures for referencing
data_lists = {
	"firstnames": first_names,
	"lastnames": last_names,
	"cities": city_names,
	"trees": tree_species,
	"states": us_state_abbrs,
	"directions": directions,
	"labels": labels,
	"employers": employers,
	"occupations": occupations,
	"sidehustles": side_hustles,
	"car_makes": car_makes,
	"car_models": car_models,
	"dealers": auto_dealers,
	"street_types": street_types,
	"emails": emails
}




# --------------------------------------------------------------------------------
def random_number_between(start, end, increment=1):
	if increment <= 0:
		raise ValueError("Increment must be a positive number.")

	# Calculate the lowest value in the range aligned with the increment
	min_value = ((start + increment - 1) // increment) * increment
	# Calculate the highest value in the range aligned with the increment
	max_value = (end // increment) * increment

	if min_value > end or max_value < start:
		raise ValueError("No values found in the given range with the specified increment.")

	# Generate a random value within the range stepping by 'increment'
	return random.randint(min_value // increment, max_value // increment) * increment

# --------------------------------------------------------------------------------
def random_number_between(start, end, increment=1):
	if increment <= 0:
		raise ValueError("Increment must be a positive number.")

	# Calculate the lowest value in the range aligned with the increment
	min_value = ((start + increment - 1) // increment) * increment
	# Calculate the highest value in the range aligned with the increment
	max_value = (end // increment) * increment

	if min_value > end or max_value < start:
		raise ValueError("No values found in the given range with the specified increment.")

	# Generate a random value within the range stepping by 'increment'
	return random.randint(min_value // increment, max_value // increment) * increment

# --------------------------------------------------------------------------------
def send(strKey, intCount):
	# subprocess.run(['notify-send', 'debug send', 'Sending ' + strKey + ' ' + str(intCount) + ' time(s)'])
	for _ in intCount:
		keyboard.send_keys(strKey)

# --------------------------------------------------------------------------------
def generate_random_relative_date_str(years_min=0, years_max=0, format="%m/%d/%Y"):
	dt = generate_random_relative_date(years_min, years_max)
	date_str = dt.strftime(format)
	# Extract components based on the format
	# For simplicity, assume format uses %m, %d, %Y in some order separated by delimiters
	# We'll parse the date string by splitting
	parts = date_str.replace('-', '/').split('/')  # normalize delimiters
	# Map parts to day, month, year depending on format
	# For the default "%m/%d/%Y" order:
	month, day, year = parts
	return int(month), int(day), int(year)


# --------------------------------------------------------------------------------
def generate_random_relative_date(years_min=0, years_max=0):
	"""
	Generate a random date relative to the current year.
	- years_min and years_max are offsets relative to current year.
	"""
	current_year = date.today().year
	year = random.randint(current_year + years_min, current_year + years_max)

	# Random month 1-12
	month = random.randint(1, 12)

	# Days in each month (ignoring leap years)
	days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	max_day = days_in_month[month - 1]

	# Random day in valid range
	day = random.randint(1, max_day)

	return date(year, month, day)



# --------------------------------------------------------------------------------
# Function to generate random string
def random_letters_numbers(start=4, end=8, length=None, flag=4):
	if length is None:
		length = random.randint(start, end)
	if flag == 2:
		# First digit can't be zero
		first_char = random.choice('23456789')
		remaining_chars = ''.join(random.choice(string.digits) for _ in range(length - 1))
		return first_char + remaining_chars
	elif flag == 4:
		chars = string.ascii_letters
	elif flag == 6:
		chars = string.ascii_letters + string.digits
	elif flag == 8:
		# First character must be a letter
		first_char = random.choice(string.ascii_letters)
		# Remaining characters can be letters or digits
		remaining_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - 1))
		return first_char + remaining_chars
	else:
		chars = string.ascii_letters
	return ''.join(random.choice(chars) for _ in range(length))



# --------------------------------------------------------------------------------
# Function to build the structure based on checkboxes
def run_sequence():
	window.activate("Vantage Finance LLC")
	struct = build_structure()
	collected_string = ""
	for item in struct:
		caption = item["caption"]
		list_name = item.get("list")
		func = item.get("func")
		after_keys = item.get("after", "")
		# Generate the value
		if list_name:
			value = random.choice(data_lists[list_name])
		elif func:
			value = func()
		else:
			value = ""

		# Fill clipboard and paste
		if isinstance(value, tuple):
			for element in value:
				# Fill clipboard with each element if needed
				keyboard.send_keys(str(element))
				time.sleep(0.2)
			keyboard.send_keys("<tab>")
			time.sleep(0.2)
			keyboard.send_keys("<tab>")
		else:
			# Process 'after' logic
			if after_keys == "":
				# Collect values in a string
				if collected_string == "":
					clipboard.fill_clipboard(str(value))
					# subprocess.run(['notify-send', 'Debug', str(value)])
				else:
					clipboard.fill_clipboard(str(collected_string))
					collected_string = ""

				time.sleep(0.2)
				keyboard.send_keys("<ctrl>+v")
				time.sleep(0.2)
				keyboard.send_keys("<tab>")
				# Loop through subsequent items to collect their values
				# (Assuming you want to do this for contiguous items with 'after' == " ")
				# For simplicity, here we'll just send a tab after the current item
			elif after_keys:
				# Send specified after keys
				collected_string = collected_string + str(value) + after_keys


		time.sleep(0.1)
	root.destroy()

# --------------------------------------------------------------------------------
# Setup GUI window
root = tk.Tk()
root.title("AutoKey Data Generator")

include_cobuyer = tk.BooleanVar()
include_sidehustle = tk.BooleanVar()
include_trade = tk.BooleanVar()
include_voi = tk.BooleanVar()

ttk.Checkbutton(root, text="Include Co-buyer", variable=include_cobuyer).pack(padx=(12), ipady=6, anchor='w')
ttk.Checkbutton(root, text="Include Side Hustles", variable=include_sidehustle).pack(padx=(12), ipady=6, anchor='w')
ttk.Checkbutton(root, text="Include Trade", variable=include_trade).pack(padx=(12), ipady=6, anchor='w')
ttk.Checkbutton(root, text="Include VOI", variable=include_voi).pack(padx=(12, 60), ipady=6, ipadx=60, anchor='w')

ttk.Button(root, text="Run", command=run_sequence).pack(pady=10)
root.mainloop()
