
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome()
driver.get("http://enr.sos.mo.gov/CountyResults.aspx")
time.sleep(5)
print driver.find_element_by_xpath("*//select[@name='cboCounty']")
#/option[text()='option_text']").click()
