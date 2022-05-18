from asyncio.windows_events import NULL
from time import sleep
from attr import NOTHING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class NCHIETestTools:
    driver = 0
    
    def initialize(self):
        TITLE = "Login"
        global driver

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http:\\portal.nchealthconnex.net")
        print("Application title is ", driver.title)
        title = driver.title
        assert title == TITLE 
        print("Application url ", driver.current_url)

        return driver

    def logon(self):
        USERNAME = "acota"
        PASSWORD = "V32T$pbara$YP6kk"

        username_field = driver.find_element_by_id("_username")
        username_field.send_keys(USERNAME)
        password_field = driver.find_element_by_id("_password")
        password_field.send_keys(PASSWORD)
        login_button = driver.find_element_by_class_name("btn-login")
        login_button.click()

        logged_on = False

        try:
            element = WebDriverWait(driver, 5).until (
                EC.presence_of_element_located((By.ID, "DisclaimerModal"))
            )
            if element is None:
                print ("!* Disclaimer dialog NOT found")
            else:
                print ("!* Disclaimer dialog found")
                logged_on = True
        except:
            print ("!* Disclaimer not found, timeout")

        if logged_on == False:
            driver.quit

        accept_button = driver.find_element_by_xpath("//*[text()='Agree']")

        if accept_button is not None:
            accept_button.click()
            print ("!* Accept button found")
        else:
            print ("!* Accept button not found")
        
        return logged_on
        
    def logoff(self):
        logout_button = driver.find_element_by_xpath("//*[text()='Logout']")

        if logout_button is not None:
            logout_button.click()
            print ("!* Logout button found")
        else:
            print ("!* Logout button not found")

    def patientSearch(self):
        LASTNAME = "CHDR"
        FIRSTNAME = "CHDR"

        last_name_field = driver.find_element_by_id("HSPatient_Find_0-item-LastName")
        last_name_field.send_keys(LASTNAME)

        first_name_field = driver.find_element_by_id("HSPatient_Find_0-item-FirstName")
        first_name_field.send_keys(FIRSTNAME)

        search_button = driver.find_element_by_id("HSPatient_Find_0-button-Search_clone")
        if search_button is not None:
            search_button.click()
            print ("!* Search button found")
        else:
            print ("!* Search button not found")
