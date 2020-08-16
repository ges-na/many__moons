from unittest import TestCase
from unittest.mock import Mock, patch
from moon_twitter import MoonName
from datetime import date
import ipdb

class TestMoon(TestCase):
    
    moon = MoonName() 

    def test_is_string(self):
        result = self.moon.get_name()
        self.assertTrue(isinstance(result, str))

    def test_has_moon(self):
        result = self.moon.get_name()
        self.assertIn('Moon', result)

    @patch('moon_twitter.MoonName.get_todays_date')
    def test_special_moon(self, get_todays_date):
        get_todays_date.return_value = date(2020, 9, 2) 
        moon = MoonName()
        result = moon.get_name()
        self.assertIn('go look', result)

    @patch('moon_twitter.MoonName.get_todays_date')
    def test_moon_phase(self, get_todays_date):
        get_todays_date.return_value = date(2020, 8, 18) 
        moon = MoonName()
        result = moon.get_name()
        self.assertIn('New', result)
