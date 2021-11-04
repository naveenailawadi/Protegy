from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# make a driver
driver = webdriver.Chrome()

# click contact page
driver.get('https://entredeveloperslab.com')

# click contact page
contact_btn = driver.find_element_by_xpath(
    '//a[@href="/contact"]')
contact_btn.click()

# wait for the page to load
time.sleep(3)

# get all the fields to contact
name_field = driver.find_element_by_xpath('//input[@id="nameField"]')
name_field.send_keys('Naveen')

email_field = driver.find_element_by_xpath('//input[@id="emailField"]')
email_field.send_keys('admin@entredeveloperslab.com')

message_field = driver.find_element_by_xpath('//textarea[@id="messageField"]')
message_field.send_keys('Annoying message from Naveen')


send_btn = driver.find_element_by_xpath(
    '//button[@class="s-12 submit-form button background-primary text-white"]')

# scroll down
for i in range(3):
    send_btn.send_keys(Keys.PAGE_DOWN)


send_btn.click()

# termination block
_ = input('Terminate?')
driver.quit()
