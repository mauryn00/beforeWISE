
#SBT SITE CRAWL

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome('C:\\Users\\Maureen Maina\\Desktop\\4.2\\IS PROJECT TOOLS\\chromedriver.exe') 

browser.get("https://www.sbtjapan.com/used-cars/?t_country=26&sort=5")

# find_elements_by_xpath returns an array of selenium objects.


ul = browser.find_element_by_class_name("carlist")# work on searching for price as well
li_items = ul.find_elements_by_tag_name('h2')

 #ul = browser.find_element_by_class_name("totalprices_area")
#li_items = ul = browser.find_element_by_class_name("car_prices")
for item in li_items:
    text = item.text
    print(text,'\n')


 