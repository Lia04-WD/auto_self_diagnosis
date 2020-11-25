import time
import functions
import os

from selenium import webdriver

# option data
region_name = functions.getRegion()
sc_level = functions.getSchoolLevel()
sc_name = functions.getSchoolName()
user_name = functions.getUserName()
user_birth = functions.getUserBirth()
user_pass = functions.getUserPassword()

driver = webdriver.Chrome("./chromedriver")
driver.get("https://hcs.eduro.go.kr/#/loginHome")

# first login (requirement)
join = driver.find_element_by_xpath("//button[@id='btnConfirm2']")
join.click()

# wait page loaded
time.sleep(2)

# search school
school_search_button = driver.find_element_by_xpath("//button[@class='searchBtn']")
school_search_button.click()

# wait page loaded
time.sleep(2)

# select school region
xpath = "//option[@value='" + region_name + "']"

school_region = driver.find_element_by_xpath(xpath)
school_region.click()

# select school level
xpath = "//option[@value='" + sc_level + "']"

school_level = driver.find_element_by_xpath(xpath)
school_level.click()

# inupt & search school name
school_name = driver.find_element_by_xpath("//input[@class='searchArea']")
school_name.send_keys(sc_name)

school_name_searchButton = driver.find_element_by_xpath("//button[@class='searchBtn']")
school_name_searchButton.click()

# wait page loaded
time.sleep(2)

# confirm school name
school_confirmButton = driver.find_element_by_xpath("//ul[@class='layerSchoolArea'][1]")
school_confirmButton.click()

# confirm school
school_confirm = driver.find_element_by_xpath("//div[@class='layerBtnWrap'][1]")
school_confirm.click()

# input name
input_name = driver.find_element_by_xpath("//input[@title='성명 입력']")
input_name.send_keys(user_name)

# input birth
input_birth = driver.find_element_by_xpath("//input[@placeholder='YYMMDD']")
input_birth.send_keys(user_birth)

# end up personal information
end_info = driver.find_element_by_xpath("//input[@id='btnConfirm']")
end_info.click()

# wait page load
time.sleep(2)

# input password
input_password = driver.find_element_by_xpath("//input[@class='input_text_common']")
input_password.send_keys(user_pass)

# end up password
confirm_password = driver.find_element_by_xpath("//input[@id='btnConfirm']")
confirm_password.click()

# wait page load
time.sleep(2)

# entry point check page
check_page = driver.find_element_by_xpath("//button[@class='btn']")
check_page.click()

# wait page load
time.sleep(2)

# first question
q_first = driver.find_element_by_xpath("//label[@for='survey_q1a1']")
q_first.click()

# second question
q_second = driver.find_element_by_xpath("//label[@for='survey_q2a1']")
q_second.click()

# third question
q_third = driver.find_element_by_xpath("//label[@for='survey_q3a1']")
q_third.click()

# submit answer
submit_button = driver.find_element_by_xpath("//input[@id='btnConfirm']")
submit_button.click()

os.system("taskkill /f /t /im chromedriver.exe")