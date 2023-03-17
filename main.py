from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import os
import time

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
# chrome_driver_path = r"C:\Users\Utilisateur1\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.speedtest.net")
driver.maximize_window()

PROMISED_DOWN = 37
PROMISED_UP = 27
