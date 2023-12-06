from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import os.path
import os
from tests.browser_test import SeleniumBrowsers

class HTMLComponentTest(unittest.TestCase):
    def test_style(self):
        drv=SeleniumBrowsers(headless=False).getFirst()
        cwd=os.getcwd()
        drv.get(os.path.join(cwd,"tests","html_component_test_page.html"))
        drv.find_element(By.XPATH ,"//div[text()='test']")
        drv.close()
    
    def test_classes(self):
        drv=SeleniumBrowsers(headless=False).getFirst()
        cwd=os.getcwd()
        drv.get(os.path.join(cwd,"tests","html_component_test_page.html"))
        self.assertEquals(drv.find_element(By.ID,"a123").value_of_css_property("font-size"),"36px")
        drv.close()