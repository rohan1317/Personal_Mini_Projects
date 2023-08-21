from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:


user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('loookki')

time.sleep(9999)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'looookkkiiiii' in output_message.text



