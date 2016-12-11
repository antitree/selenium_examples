from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv, time

EMAILADDR = 'recoveryemail@yourdomain.com'
account_url = 'https://accounts.google.com'

with open('accounts.csv', 'r') as f:
  reader = csv.reader(f)
  accounts = list(reader)

for account in accounts:
	driver = webdriver.Chrome('./chromedriver')
	driver.get(account_url)

	try:
	  e_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
	  e_email = driver.find_element_by_id('Email')
	  e_email.send_keys(account[0])
	  e_email.submit()

	finally:
	  print "done"
	  #driver.quit()

	try:
	  e_passwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Passwd')))
	  e_passwd = driver.find_element_by_id('Passwd')
	  e_passwd.send_keys(account[1])
	  e_passwd.submit()
	finally:
	  print "password sent"

	try:
	  e_email = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, 'Edit')))
	  e_edit = driver.find_element_by_link_text("Edit")
	  e_edit.click()

	  e_recovery = driver.find_element_by_class_name("Kc")
	  e_recovery.clear()
	  e_recovery.send_keys(EMAILADDR)

	  e_done = driver.find_element_by_xpath('//a[@role = "button"]')
	  e_done.submit()
	except:
 	  print "No it did not go ok"

        finally:
	  print("Did it go ok?")

	time.sleep(3)
	driver.quit()
