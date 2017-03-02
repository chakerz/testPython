# Android environment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#user und password
user = "xxxxx@live.de"
pwd = "xxxxx"

#selenium driver
driver = webdriver.Firefox()

#navigiere zu facebook
driver.get("http://www.facebook.com")

#sicherstellen das wir auf der facebok seite sind
assert "Facebook" in driver.title

#finde das input-feld für email
elem = driver.find_element_by_id("email")
elem.send_keys(user)

#finde das input-feld für passwort
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

#enter drücker
elem.send_keys(Keys.RETURN)

#selenium driver schließen
driver.close()
