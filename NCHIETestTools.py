from time import sleep
from attr import NOTHING
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

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

        disclaimer_modal = WebDriverWait(driver, 5).until (
            ExpectedConditions.presence_of_element_located((By.ID, "DisclaimerModal"))
        )

        if disclaimer_modal is None:
            print ("!* Disclaimer dialog NOT found")
        else:
            print ("!* Disclaimer dialog found")
            logged_on = True

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

        last_name_field = WebDriverWait(driver, 5).until (
            ExpectedConditions.presence_of_element_located((By.ID, "HSPatient_Find_0-item-LastName"))
        )

        if last_name_field is not None:
            last_name_field.send_keys(LASTNAME)
            print ("!* Last Name field found")
        else:
            print ("!* Last Name field not found")

        first_name_field = driver.find_element_by_id("HSPatient_Find_0-item-FirstName")

        if first_name_field is not None:
            first_name_field.send_keys(FIRSTNAME)
            print ("!* First Name field found")
        else:
            print ("!* First Name field not found")

        search_button = driver.find_element_by_id("HSPatient_Find_0-button-Search_clone")
        if search_button is not None:
            search_button.click()
            print ("!* Search button found")
        else:
            print ("!* Search button not found")

    def openPatient(self):
        search_result_link = WebDriverWait(driver, 5).until (
            ExpectedConditions.presence_of_element_located((By.ID, "HSPatient_List_0-row-2-item-NameListUser-link"))
        )

        if search_result_link is None:
            print ("!* Search result NOT found")
        else:
            print ("!* Search result found")
            search_result_link.click()

        select_reason_dropdown = Select(WebDriverWait(driver, 5).until (
            ExpectedConditions.presence_of_element_located((By.ID, "selBTGReason")))
        )

        if select_reason_dropdown is not None:
            select_reason_dropdown.select_by_value('privacyaudit')
            print ("!* BTG reason select found")
        else:
            print ("!* BTG reason select not found")

        declare_button = driver.find_element_by_id("btnBTGDeclare")
        if declare_button is not None:
            declare_button.click()
            print ("!* Declare button found")
        else:
            print ("!* Declare button not found")

        allergies_field = WebDriverWait(driver, 30).until (
            ExpectedConditions.presence_of_element_located((By.ID, "PAAllergy_ListEMR_0-header-caption"))
        )

        if allergies_field is not None:
            print ("!* Allergies field found")
        else:
            print ("!* Alergies field not found")
