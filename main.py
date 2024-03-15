from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import time

chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
PROMISED_DOWN = 300
PROMISED_UP = 300
INTERNET_PROVIDER = "@bellCanada"

EMAIL = os.environ["EMAIL"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_internet_speed(self):
        print("In the get_internet_seed function")
        self.driver.get("https://www.speedtest.net/")
        print("wait 5 seconds")
        time.sleep(5)
        try:
            print("accept cookies")
            accept_cookies_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_cookies_button.click()
            time.sleep(3)
        except NoSuchElementException:  # spelling error making this code not work as expected
            print("no cookies window")
            pass
        print("start the test and wait 60s")
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        start_button.click()
        time.sleep(60)
        print("get the download speed and register in self.down")
        download_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").get_attribute("innerHTML"))
        self.down = download_speed
        print("get the upload speed and register in self.up")
        upload_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").get_attribute("innerHTML"))
        self.up = upload_speed

    def tweet_at_provider(self):
        print("go on twitter")
        self.driver.get("https://twitter.com/")
        time.sleep(10)
        print("find the connect button and click on it")
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        sign_in_button.click()
        time.sleep(15)
        print("find the input email and enter email")
        input_email = self.driver.find_element(By.NAME, "text")
        input_email.send_keys(EMAIL)
        time.sleep(5)
        input_email.send_keys(Keys.ENTER)
        try:
            time.sleep(5)
            print("robot detection window")
            input_email = self.driver.find_element(By.NAME, "text")
            input_email.send_keys(USERNAME)
            time.sleep(10)
            input_email.send_keys(Keys.ENTER)
        except NoSuchElementException:  # spelling error making this code not work as expected
            print("no robot detection window")
            pass
        time.sleep(3)
        print("find password input and enter password")
        password_email = self.driver.find_element(By.NAME, "password")
        password_email.send_keys(PASSWORD)
        time.sleep(5)
        password_email.send_keys(Keys.ENTER)
        time.sleep(10)
        print("find the tweet area and enter message")
        tweet_area = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span")
        message = f"{INTERNET_PROVIDER} you promised {PROMISED_UP} up and {PROMISED_DOWN} down. I've got only {self.up} up and {self.down} down."
        print(message)
        tweet_area.send_keys(message)
        print("send the message!")
        send_twit_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div')
        # send_twit_button.click()
        self.driver.quit()


print("-- create bot --")
bot = InternetSpeedTwitterBot()
print("bot -->", bot)
print("-- go to get_internet_speed --")
bot.get_internet_speed()
print(bot.down)
print(bot.up)
if bot.up < PROMISED_UP and bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
