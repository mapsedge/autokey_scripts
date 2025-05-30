clipboard.fill_clipboard(
"""var namespace = (function ($) {

    // defined within the local scope
    var privateMethod1 = function () { /* ... */ }
    var privateProperty1 = 'foobar';

    return {

        //nested namespace with public properties
        properties:{
            publicProperty1: privateProperty1
        },
        function1: function(){
            // function contents
        }
    }
})(jQuery);"""
)
time.sleep(.5)
keyboard.send_keys("<ctrl>+v")

 
