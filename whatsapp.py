import datetime
import time
import sys
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

sys.path.append("/home/avishek/Code")
from data.whatsapp_automation.message import replace_message_name,holi_msg
from data.whatsapp_automation.names import names

send_message = True

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
actions = ActionChains(driver)

# Check for login and wait for login
a = input("Press enter after you login.")

for name in names.keys():

    first_name = names[name] if names[name] else name
    message = replace_message_name(holi_msg,first_name)
    

    # Search for the search box and type the name
    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]' 
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search_box.clear()

    time.sleep(1)
    search_box.send_keys(name)
    time.sleep(1)

    # Search For Name and click it
    person_xpath = f'//span[@title="{name}"]'
    person = driver.find_element_by_xpath(person_xpath) 
    person.click()
    time.sleep(1)

    # Find message Box and send the message
    message_box_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
    message_box = driver.find_element_by_xpath(message_box_xpath)
    message_box.clear()

    if send_message:
        message_box.send_keys(message)
        message_box.send_keys(':rainbow')
        
        message_box.send_keys(Keys.ENTER)
        message_box.send_keys(Keys.ENTER)

    # Wait for sometime then close the browser
    time.sleep(1)
driver.quit()
