from selenium import webdriver
from time import sleep
import pywhatkit

from selenium.webdriver.common.by import By
# options = Options()
# options.page_load_strategy = 'eager'
# driver = webdriver.Chrome(options=options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized");
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=chrome_options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')

input('Enter anything after scanning QR code')

user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element(By.XPATH,'//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element(By.XPATH,
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
send_button.click()