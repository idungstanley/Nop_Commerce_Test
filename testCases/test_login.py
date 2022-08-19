import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username = 'admin@yourstore.com'
    password = "admin"

    def test_homePageTitle(self):
        self.driver = webdriver.chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

