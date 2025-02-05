from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get("https://urbanroutes.tripleten-services.com")

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url, "URL verification failed!"

# Close the browser
driver.quit()
