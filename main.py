from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import os
import time

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


PROMISED_DOWN = 37
PROMISED_UP = 27


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
        service = Service(chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_internet_speed(self):
        print("go to speedtest")
        self.driver.get("https://www.speedtest.net")
        self.driver.maximize_window()
        time.wait(3)
        print("accept cookies")
        accept_cookies_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookies_button.click()
        time.wait(3)
        print("start the test and wait 45 s")
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        start_button.click()
        time.sleep(45)
        print("get the download speed and register in self.down")
        download_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").get_attribute("innerHTML"))
        self.down = download_speed
        print("get the upload speed and register in self.up")
        upload_speed= float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").get_attribute("innerHTML"))
        self.up = upload_speed

    def tweet_at_provider(self):
        # to connect to twitter
        # driver.get("https://twitter.com/")
        pass


internet_bot = InternetSpeedTwitterBot()
internet_bot.get_interest_speed()
print(internet_bot.down)
print(internet_bot.up)




