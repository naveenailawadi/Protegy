from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

# opens website
driver.get('https://accounts.spotify.com/en/login/?continue=https:%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1&_locale=en-US')


# types in email
email_field = driver.find_element(By.XPATH, '//input[@id= "login-username"]')
email_input = input('Type in your email: ')
email_field.send_keys(email_input)


# types in password
password_field = driver.find_element(
    By.XPATH, '//input[@id= "login-password"]')
password_input = input('Type in your password: ')
password_field.send_keys(password_input)


# clicks login button
login_button = driver.find_element(
    By.XPATH, '//button[@class= "btn btn-block btn-green ng-binding"]')
login_button.click()
time.sleep(5)

# clicks dismiss
dismiss_button = driver.find_element(
    By.XPATH, '//button[@class= "Button-sc-1dqy6lx-0 ccVfjR vDBT9Q6Z8bqFDw0SO1e4 Sm8rqtVFvZY5yMoaPmU_"]')
dismiss_button.click()
time.sleep(5)

# opens playlist
playlist_button = driver.find_element(
    By.XPATH, '//a[@href="/playlist/0gnOs3Fl6BhnU8BvDQQ54R"]')
playlist_button.click()

time.sleep(5)

# plays a song
play = driver.find_element(
    By.XPATH, '//div[@class="_5wXWalxnOyFQX7uHu_j"]//button[@class="_47lzH_9ZSVGM4UUdX90 tBo7WbUk9fgBuWpnsy0_"]')
play.click()
time.sleep(350)


_ = input("terminate")
driver.quit()
