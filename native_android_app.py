# Android environment
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = '/Users/chakerz/Documents/ExpenseManager.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.find_element_by_id("menu_new_expense_only").click()
driver.find_element_by_id("digit_3").click()
driver.find_element_by_id("digit_1").click()
driver.find_element_by_id("button1").click()

el_list = driver.find_elements(By.ID, 'category_name')

el_list[1].click()

driver.find_element(By.XPATH, "//android.widget.TextView[@text='Speichern']").click()

driver.quit()
