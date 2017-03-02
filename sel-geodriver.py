from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
# Firefox 47 (stable) is currently not supported,
# and may give you a suboptimal experience.
#
# On Mac OS you must point to the binary executable
# inside the application package, such as
# /Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin
caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
geckodriver="/usr/local/Cellar/geckodriver/0.14.0/bin/geckodriver"

driver = webdriver.Firefox(capabilities=caps, executable_path="/usr/local/Cellar/geckodriver/0.14.0/bin/geckodriver")
driver.get("http://www.google.com")

driver.quit()
