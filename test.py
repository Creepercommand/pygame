from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.implicitly_wait(2)
url = 'http://m.cgv.co.kr/WebApp/SpecialV4/Detail.aspx?seq=1&type='
driver.get(url)

css_selector = "#ContainerView > div:nth-child(4) > div.location_listwrap > ul:nth-child(5) > li:nth-child(3) > a"
elem = driver.find_element_by_css_selector(css_selector)

time.sleep(15)
while True:
    elem.send_keys(Keys.RETURN)
    inputElement = driver.find_element_by_id('Alert')
    inputElement.click()

