import requests
import unittest
import random
from unittest import TestCase

class CityTestCase(unittest.TestCase):
    def test_01_all_city(self):
        url = 'http://localhost:8000/api/goods/'
        resp = requests.get(url)

        # city_list = resp.json().get('data')
        # city = random.choice(city_list)

        # self.city_id = city['id']
        # print('_____.._____',city['city_name'])
        print(str(resp.content,encoding='utf-8'))
    def test_02_city_area(self):
        url = 'http://localhost:8000/api/goodscart'
        # url = 'http://localhost:8000/api/goodscart?one_id=%s'
        # resp = requests.get(url,{
        #     'one_id':self.city_id
        # })
        # area_list = resp.json().get('data')
        # area = random.choice(area_list)
        # print('____..____',)
        #
        # self.area_id = area['id']
        resp = requests.get(url)
        print(str(resp.content,encoding='utf-8'))

if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(CityTestCase.test_dll_city)

    suite2 = unittest.TestSuite()
    suite2.addTest(CityTestCase.test_dll_area)

    all_suite = unittest.TestSuite((suite1,suite2))

    unittest.TextTestRunner().run(all_suite)