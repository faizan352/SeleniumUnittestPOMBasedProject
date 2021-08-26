import time
import unittest
import HtmlTestRunner
from selenium import webdriver

import sys

sys.path.append('C:/Users/ANSARI/PycharmProjects/pythonUnitTestProject_POMBased')

from pageObjects.loginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURl = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = 'admin@yourstore.com'
    password = 'admin'
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURl)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual('Dashboard / nopCommerce administration',
                         self.driver.title, 'webpage title is not match')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ANSARI'
                                                                  '/PycharmProjects'
                                                                  '/pythonUnitTestProject_POMBased'
                                                                  '/reports'))
