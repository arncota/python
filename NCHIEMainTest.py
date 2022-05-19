from time import sleep
from NCHIETestTools import NCHIETestTools

testDriver = NCHIETestTools()

driver = testDriver.initialize()
testDriver.logon()
testDriver.patientSearch()
testDriver.openPatient()
testDriver.logoff()

driver.quit
