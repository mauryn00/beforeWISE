
#INDIVIDUAL CAR SEARCH

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys

#Data manipulation
import pandas as pd

#visualization


browser = webdriver.Chrome('C:\\Users\\Maureen Maina\\Desktop\\4.2\\IS PROJECT TOOLS\\chromedriver.exe')

sbt_url = 'https://www.sbtjapan.com'
browser.get ('https://www.sbtjapan.com') #can also be browser.get(sbt_url)
search_item = 'Toyota Ractis'  # Chose this as an example
search_bar = browser.find_element_by_id('keyword')
search_bar.send_keys(search_item)
search_bar.send_keys(Keys.RETURN)






