from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import os.path

class HTMLComponentTest(unittest.TestCase):
    def test_style(self):
        srv=Service(r"C:\Users\wc018\Driver\chromedriver.exe")
        drv=webdriver.Chrome(service=srv)
        drv.get(repr(os.path.join("tests","html_component_test_page.html")))
        drv.find_element(By.XPATH ,"//div[text()='test']")
        drv.close()
    
    def test_classes(self):
        srv=Service(r"C:\Users\wc018\Driver\chromedriver.exe")
        drv=webdriver.Chrome(service=srv)
        drv.get(repr(os.path.join("tests","html_component_test_page.html")))
        self.assertEquals(drv.find_element(By.ID,"a123").value_of_css_property("font-size"),"36px")
        drv.close()

print(os.path.join("tests","html_component_test_page.html"))