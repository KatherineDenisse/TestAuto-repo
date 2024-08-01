import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker
from openpyxl import workbook


class function():

    def __init__(self,driver):
        self.driver = driver

    def load_page(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@class='self-center']").click()
        time.sleep(2)

    def new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[@href='/account/register']").click()
        fake = Faker()
        name = fake.name()
        driver.find_element(By.XPATH, "//input[@name='full_name']").send_keys(name)
        mail = fake.email()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(mail)
        clave = fake.password(length=8)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(clave)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Nombre: " + name)
        print("Correo: " + mail)
        print("Contraseña: " + clave)

    def login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Katyna_acua16@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Kate1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def choose_products(self, filtro):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[@class='nav-link hover:underline'][contains(.,'Men')]").click()
        time.sleep(2)
        if filtro == "XL":
            driver.find_element(By.XPATH, "//span[@class='filter-option'][contains(.,'XL')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//img[contains(@alt,'Seasonal color chuck 70')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@name='qty']").clear()
            driver.find_element(By.XPATH, "//input[@name='qty']").send_keys("1")
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'XL')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[contains(.,'Green')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//span[contains(.,'ADD TO CART')]").click()
            time.sleep(2)
        elif filtro == "M":
            driver.find_element(By.XPATH, "//span[@class='filter-option'][contains(.,'M')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//img[contains(@alt,'Nike react infinity run flyknit')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@name='qty']").clear()
            driver.find_element(By.XPATH, "//input[@name='qty']").send_keys("3")
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'M')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[contains(.,'Purple')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//span[contains(.,'ADD TO CART')]").click()
            time.sleep(2)
        elif filtro == "L":
            driver.find_element(By.XPATH, "//span[@class='filter-option'][contains(.,'L')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//img[contains(@alt,'Nike air zoom pegasus 35')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@name='qty']").clear()
            driver.find_element(By.XPATH, "//input[@name='qty']").send_keys("2")
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'M')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//a[contains(.,'Black')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//span[contains(.,'ADD TO CART')]").click()
            time.sleep(2)
        time.sleep(2)

    def cart(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@class='mini-cart-wrapper self-center']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "// span[contains(., 'CHECKOUT')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Kate Nieves")
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("999999999")
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Av. El Sol 111")
        driver.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("Lima")
        time.sleep(2)
        country = driver.find_element(By.XPATH, "//select[contains(@id,'address[country]')]")
        c = Select(country)
        c.select_by_visible_text("China")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,800)")
        time.sleep(2)
        prov = driver.find_element(By.XPATH, "//select[contains(@id,'address[province]')]")
        pro = Select(prov)
        pro.select_by_index(1)
        driver.find_element(By.XPATH, "(//input[@type='text'])[5]").send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "(//span[contains(@class,'pl-1')])[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[contains(.,'Continue to payment')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//img[contains(@alt,'Cash On Delivery')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[contains(.,'Place Order')]").click()
        time.sleep(3)