import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Function import function

t = 2

class base_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNewUser(self):
        driver = self.driver
        f = function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.new_user()

    def testLogin(self):
        driver = self.driver
        f = function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()


    def testChoose(self):
        driver = self.driver
        f = function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()
        f.choose_products("XL")
        f.choose_products("M")
        f.choose_products("L")

    def testCart(self):
        driver = self.driver
        f = function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()
        f.cart()

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()