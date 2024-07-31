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
        f.load_page("https://demo.evershop.io/",t)
        driver.find_element(By.XPATH, "//a[@href='/account/register']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='full_name']").send_keys("Katherine Nieves")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Katherine.nievesalva@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Kate1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


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