from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Create the HTML structure using Selenium
driver.get("data:text/html;charset=utf-8,")

# Head section
head = driver.find_element(By.TAG_NAME, "head")

# Meta charset
meta_charset = driver.find_element(By.TAG_NAME, "head").find_element(By.NAME, "charset")
meta_charset.send_keys("utf-8")

# Meta viewport
meta_viewport = driver.find_element(By.TAG_NAME, "head").find_element(By.NAME, "viewport")
meta_viewport.send_keys("width=device-width, initial-scale=1")

# Meta description
meta_description = driver.find_element(By.TAG_NAME, "head").find_element(By.NAME, "description")
meta_description.send_keys("One District One Product | A ecommerce website")

# Title
title = driver.find_element(By.TAG_NAME, "head").find_element(By.TAG_NAME, "title")
title.send_keys("One District One Product")

# Link stylesheet
link = driver.find_element(By.TAG_NAME, "head").find_element(By.TAG_NAME, "link")
link.send_keys("rel=stylesheet")
link.send_keys("type=text/css")
link.send_keys("href=%PUBLIC_URL%/style.css")

# Body section
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys("id=page-top")

# noscript
noscript = driver.find_element(By.TAG_NAME, "body").find_element(By.TAG_NAME, "noscript")
noscript.send_keys("You need to enable JavaScript to run this app.")

# Div container
div_container = driver.find_element(By.TAG_NAME, "body").find_element(By.ID, "root")
div_container.send_keys("class=font-light text-base text-gray-800 bg-white flex flex-col min-h-screen")

# Display the generated HTML
print(driver.page_source)

# Close the browser
driver.quit()
