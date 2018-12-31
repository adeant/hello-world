from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
# chromeDriver = webdriver.Chrome('C:\\Users\\Alex Trim\\Documents\\GitHub\\hello-world\\AtomPython\\Miscellaneous\\chromedriver.exe')
chromeDriver = webdriver.Chrome('C:\\Users\\Dean\\Documents\\GitHub\\hello-world\\AtomPython\\Miscellaneous\\chromedriver.exe')
chromeDriver.get('https://www.cityofmadison.com/assessor/property/salesbyarea.cfm')
areaElem = chromeDriver.find_element_by_id('AssessmentArea')
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
# soup the page
pageSoup = BeautifulSoup(pageSource)
tbodies = pageSoup.find_all('tbody')
pageSoup.find('tbody')
for cell in tbodies[0].find_all('td'): print(cell.text.strip())
for option in areaOptions: print(option.text)
