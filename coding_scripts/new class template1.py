tmp = """<?php

if (!class_exists('_curl')) {

    class _curl
    {

        public $a = '';
        private $b = '';

        //--------------------------------------------------------------------------------
        function __construct()
        {
        }

        //--------------------------------------------------------------------------------
        public function set($k, $v)
        {
            if (property_exists($this, $k)) {
                $this->$k = $v;
            }
        }

        //--------------------------------------------------------------------------------
        public function get($k)
        {
            if (property_exists($this, $k)) {
                return $this->$k;
            }
            return null;
        }
    }
}"""

clipboard.fill_clipboard(tmp)
time.sleep(1)
keyboard.send_keys("<ctrl>+v")