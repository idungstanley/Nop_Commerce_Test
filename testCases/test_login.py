import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
class Test_001_Login:
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username = 'admin@yourstore.com'
    password = "admin"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

