from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SPOTIFY_LOGIN_URL = 'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1&_locale=en-US'


# spotify bot class
class SpotifyBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # login (never use inputs in a class)
    def login(self, email, password):
        # opens website
        self.driver.get(SPOTIFY_LOGIN_URL)

        # types in email
        email_field = self.driver.find_element(
            By.XPATH, '//input[@id= "login-username"]')
        email_field.send_keys(email)

        # types in password
        password_field = self.driver.find_element(
            By.XPATH, '//input[@id= "login-password"]')
        password_field.send_keys(password)

        # clicks login button
        login_button = self.driver.find_element(
            By.XPATH, '//button[@class= "btn btn-block btn-green ng-binding"]')
        login_button.click()
        time.sleep(5)

        # clicks dismiss
        dismiss_button = self.driver.find_element(
            By.XPATH, '//button[@class= "Button-sc-1dqy6lx-0 ccVfjR vDBT9Q6Z8bqFDw0SO1e4 Sm8rqtVFvZY5yMoaPmU_"]')
        dismiss_button.click()
        time.sleep(5)

    # opens playlist
    def play_playlist(self, playlist_url, play_time):
        # go to playlist url
        self.driver.get(playlist_url)

        # plays a song
        play = self.driver.find_element(
            By.XPATH, '//div[@class="_5wXWalxnOyFQX7uHu_j"]//button[@class="_47lzH_9ZSVGM4UUdX90 tBo7WbUk9fgBuWpnsy0_"]')
        play.click()

        # wait some time
        time.sleep(play_time)

    # quit
    def quit(self):
        self.driver.quit()
