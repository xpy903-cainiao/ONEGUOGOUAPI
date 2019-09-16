import requests
import unittest
import random
from unittest import TestCase


class TestCase(unittest.TestCase):
    def test_01_goods(self):
        url = 'http://localhost:8000/api/goods/'
        resp = requests.get(url)
        print(resp.json())
    def test_02_goodscart(self):
        url = 'http://localhost:8000/api/goodscart'
        resp = requests.get(url)
        js_data = resp.json()
        print(js_data[0]['goods_id'])

    def test_03_address(self):
        url = 'http://localhost:8000/api/address'
        resp = requests.get(url)
        print(resp.json())

    def test_04_orderdetail(self):
        url = 'http://localhost:8000/api/orderdetail'
        resp = requests.get(url)
        print(resp.json())

    def test_05_comment(self):
        url = 'http://localhost:8000/api/comment'
        resp = requests.get(url)
        print(resp.json())

    def test_06_city(self):
        url = 'http://localhost:8000/api/city'
        resp = requests.get(url)
        print(resp.json())

    def test_07_category(self):
        url = 'http://localhost:8000/api/category'
        resp = requests.get(url)
        print(resp.json())

    def test_08_nav(self):
        url = 'http://localhost:8000/api/nav'
        resp = requests.get(url)
        print(resp.json())

    def test_09_navinfo(self):
        url = 'http://localhost:8000/api/navinfo'
        resp = requests.get(url)
        print(resp.json())

if __name__ == '__main__':
    suite1 = unittest.TestSuite()
    suite1.addTest(TestCase)
    all_suite = unittest.TestSuite((suite1,))
    unittest.TextTestRunner().run(all_suite)
