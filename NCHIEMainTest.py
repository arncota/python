from asyncio.windows_events import NULL
from time import sleep
from attr import NOTHING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from NCHIETestTools import NCHIETestTools

testDriver = NCHIETestTools()

driver = testDriver.initialize()
testDriver.logon()
sleep(5)
testDriver.patientSearch()
sleep(10)
testDriver.logoff()

driver.quit
