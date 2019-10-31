
#CHEKI SITE CRAWL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome('C:\\Users\\Maureen Maina\\Desktop\\4.2\\IS PROJECT TOOLS\\chromedriver.exe') 

browser.get("https://www.cheki.co.ke/vehicles")

# find_elements_by_xpath returns an array of selenium objects.
ul = browser.find_element_by_class_name("listing-unit__container")
li_items = ul.find_elements_by_class_name('ellipses')
li_items2 = ul.find_elements_by_tag_name('h2')


for item in li_items:
    text = item.text
   #we insert the first column(car_make)
    print(text,'\n')
    
#READ ON#####curl request to the api

for item2 in li_items2:
    text = item2.text
   #we insert the second column (price)
    print(text,'\n')

