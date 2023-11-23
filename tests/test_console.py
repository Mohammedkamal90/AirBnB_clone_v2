#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestDoCreate(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_state_with_name(self):
        with patch("console.storage.create") as create_mock:
            self.console.do_create("State name=\"California\"")
            create_mock.assert_called_with("State", name="California")

    def test_create_place_with_multiple_parameters(self):
        with patch("console.storage.create") as create_mock:
            self.console.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
            create_mock.assert_called_with("Place", city_id="0001", user_id="0001", name="My little house", number_rooms=4, number_bathrooms=2, max_guest=10, price_by_night=300, latitude=37.773972, longitude=-122.431297)

if __name__ == "__main__":
    unittest.main()
