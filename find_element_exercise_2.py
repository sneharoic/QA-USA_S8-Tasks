import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://cnt-8ce080bb-5625-466e-8fa0-6ba19b15562a.containerhub.tripleten-services.com")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find all elements on the page using an XPath selector
elements = driver.find_elements(By.XPATH,"//div[@class='dst-picker-marker']")

# Check that the number of elements found is greater than 1 by using len()
assert len(elements)>1

# Close the browser and end the WebDriver session
driver.quit()
W