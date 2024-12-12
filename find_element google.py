import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_google_images():
    # Initialize a new instance of the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the specified URL in the browser
    driver.get("https://www.google.com/")

    # Pause execution for 2 seconds to allow the page to load fully
    time.sleep(2)

    # Find the title element using its CSS Selector
    driver.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys("newyork.com")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input.gNO89b").click()
    # WebDriverWait(driver,120).until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[text()="Not now"]')))
    # driver.find_element(By.XPATH,'//div[text()="Not now"]').click()
    WebDriverWait(driver, 120).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[text()="Images"]')))
    driver.find_element(By.XPATH, '//div[text()="Images"]').click()
    driver.find_element(By.XPATH, '//span[text()="www.newyork.com"]').click()
    time.sleep(5)
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])

    assert "https://www.newyork.com/" in driver.current_url #== "https://www.newyork.com/"
    # Close the browser and end the WebDriver session
    driver.quit()
