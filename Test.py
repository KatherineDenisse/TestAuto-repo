import time
import unittest
from selenium import webdriver
from Function import Function
from selenium.webdriver.common.by import By
t = 2


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testNewUser(self):
        driver = self.driver
        f = Function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.new_user()


    def testLogin(self):
        driver = self.driver
        f = Function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()

    def testChoose(self):
        driver = self.driver
        f = Function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()
        f.choose_products("XL")
        f.choose_products("M")
        f.choose_products("L")

    def testCart(self):
        driver = self.driver
        f = Function(driver)
        f.load_page("https://demo.evershop.io/", t)
        f.login()
        f.choose_products("XL")
        #f.choose_products("M")
        #f.choose_products("L")
        driver.refresh()
        f.cart()


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
