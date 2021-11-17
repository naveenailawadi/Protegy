from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SPOTIFY_LOGIN_URL = 'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fopen.spotify.com%2F__noul__%3Fl2l%3D1%26nd%3D1&_locale=en-US'


class SpotifyBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self, email, password):
        self.driver.get(SPOTIFY_LOGIN_URL)

        email_field = self.driver.find_element(
            By.XPATH, '//input[@id= "login-username"]')
        email_field.send_keys(email)

        password_field = self.driver.find_element(
            By.XPATH, '//input[@id= "login-password"]')
        password_field.send_keys(password)

        login_button = self.driver.find_element(
            By.XPATH, '//button[@class= "btn btn-block btn-green ng-binding"]')
        login_button.click()
        time.sleep(5)

        dismiss_button = self.driver.find_element(
            By.XPATH, '//div[@class="bud10Wp39_iwW7cT_xcv"]//button[@class="Button-sc-1dqy6lx-0 ccVfjR vDBT9Q6Z8bqFDw0SO1e4 Sm8rqtVFvZY5yMoaPmU_"]')
        dismiss_button.click()
        time.sleep(5)

    def play_playlist(self, playlist_url, play_time):
        self.driver.get(playlist_url)
        time.sleep(5)

        play = self.driver.find_elements(
            By.XPATH, '//button[@data-testid="play-button"]')[1]
        play.click()
        time.sleep(play_time)

    def quit(self):
        self.driver.quit()
