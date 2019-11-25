
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

#browser.get("https://www.sbtjapan.com/used-cars/?t_country=26&sort=5")
browser.get("https://www.sbtjapan.com/used-cars/?make=&model=&model_code=&steering=all&type=0&sub_body_type=0&drive=0&year_f=&month_f=&year_t=&month_t=&price_f=&price_t=&cc_f=0&cc_t=0&mile_f=0&mile_t=0&trans=0&savel=0&saveu=0&fuel=0&color=0&bodyLength=0&loadClass=0&engineType=0&truck_size=&location=0&port=0&ready_to_ship=kenya&search_box=1&sold=&p_years=&bid_code=&pdate_f=&pdate_t=&locationIds=0&stock_ids=&d_country=26&d_port=52&ship_type=0&FreightChk=yes&currency=2&insurance=1&sort=0&psize=&custom_search=#listbox")

# find_elements_by_xpath returns an array of selenium objects.


ul = browser.find_element_by_class_name("carlist")# work on searching for price as well
li_items = ul.find_elements_by_class_name('totalprices_area')
li_items2 = ul.find_element_by_tag_name("h2")



 #ul = browser.find_element_by_class_name("totalprices_area")
#li_items = ul = browser.find_element_by_class_name("car_prices")
for item in li_items:
    text = item.text
    print(text,'\n')


 