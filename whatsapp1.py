import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://web.whatsapp.com/")

name = "Devyani"

# To get a new date and time stamp for every new message, I have converted message as a function.
def message():
    return "Hi.. I am a simple python script..I here to tell you the current  date and time.. Date :- " \
           + str(datetime.datetime.now().date()) + " Time :- " + str(datetime.datetime.now().time()) + "\n"

# Check for login and wait for login
a = input("Press enter after you login.")

# Search for the search box
search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]' 
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
search_box.send_keys(name)
time.sleep(1)

# Search For Name
name_xpath = f'//span[@title="{name}"]'
person = driver.find_element_by_xpath(name_xpath) 
person.click()
time.sleep(1)

# Find message Box
message_box_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
message_box = driver.find_element_by_xpath(message_box_xpath)
message_box.send_keys(message())
message_box.send_keys(Keys.ENTER)

# Wait for sometime then close the browser
time.sleep(5)
driver.quit()
