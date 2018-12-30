from selenium import webdriver
chromeDriver = webdriver.Chrome('C:\\Users\\Alex Trim\\Documents\\GitHub\\hello-world\\AtomPython\\Miscellaneous\\chromedriver.exe')
chromeDriver.get('https://www.cityofmadison.com/assessor/property/salesbyarea.cfm')
areaElem = chromeDriver.find_element_by_id('AssessmentArea')
from selenium.webdriver.support.ui import Select
# select the field
areaSelect = Select(areaElem)
# get all of the available options
areaOptions = areaSelect.options
# enter the value into the field
areaSelect.select_by_value('52')
# find the button
submitBtn = chromeDriver.find_element_by_css_selector("input[type='submit']")
# select submit to get the page data
submitBtn.click()
# grab the page source
pageSource = chromeDriver.page_source
# get the demystifier
from bs4 import BeautifulSoup
# soup the page
pageSoup = BeautifulSoup(pageSource)
pageSoup.find_all('tbody')
