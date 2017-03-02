from appium import webdriver
import time

#Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['appiumVersion'] = '1.6.3'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['browserName'] = 'Browser'
desired_caps['name'] = 'Sample Test'

# For Remote Testing in Testobject
#desired_caps['testobject_api_key'] = 'INSERT_API_KEY_HERE'
#desired_caps['testobject_device'] = 'Motorola_Moto_E_2nd_gen_free'
#driver = webdriver.Remote('http://appium.testobject.com/wd/hub', desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get("http://www.chakib.de")

time.sleep(10)

driver.quit()
