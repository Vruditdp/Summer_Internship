from selenium import webdriver
import time
driver=webdriver.Chrome("E:/A vrudit/Working/Python Projects/Glassdoor_Scraper/chromedriver.exe")
driver.get("https://www.google.com/")
# time.sleep(7)
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_xpath("//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]").click()
