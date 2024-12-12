import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://cnt-7fe6031d-2125-4b7c-9c09-7a40d9eaadfc.containerhub.tripleten-services.com")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver.find_element(By.ID,"from").send_keys("East 2nd Street, 601 ")


# Find the TO field and fill it in
driver.find_element(By.ID,"to").send_keys("1300 1st St")

time.sleep(2)

# Find the "Call a taxi" button and click on it
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button').click()

# Add an explicit wait for the field to load
WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID,'comment')))

# Write a comment to the driver
message_to_taxi_driver=driver.find_element(By.ID,"comment")
message_to_taxi_driver.send_keys("hello bring me chocolate")
time.sleep(2)

# Check that your comment is what you expect it to be
assert message_to_taxi_driver.get_attribute("value")=="hello bring me chocolate"

driver.quit()
