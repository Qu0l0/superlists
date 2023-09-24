from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.IeOptions()
driver = webdriver.Ie(options=options)
driver.get('http://127.0.0.1:8000/')
assert 'Django' in driver.title