import unittest
from city_functions import get_formatted_site

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_name = get_formatted_site('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')
        
    def test_city_country_population(self):
        formatted_name = get_formatted_site('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago Chile - population 5000000')
        
unittest.main()
