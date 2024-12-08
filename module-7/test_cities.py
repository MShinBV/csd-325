# Miles Shinsato 11/29/2024 7.2 Assignment

# Importing Unittest
import unittest

# From statement to show where to import from
from city_functions import city_country

# Creating Class
class TestCityCountry(unittest.TestCase):

    #Tests for the city_country function
    def test_city_country(self):

        #Test that the function works for city and country
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
