# Add new employee details

import time

from selenium import webdriver

from CapstoneProject1.PageObjects.data import Data
from CapstoneProject1.PageObjects.yaml_function import YAML_Function
from CapstoneProject1.PageObjects.locators import Locators

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

readData = YAML_Function(Data().yaml_file)


class TestPIM:
    url = Data().web_url
    driver = webdriver.Firefox()

    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.refresh()
        self.driver.implicitly_wait(10)

    def test_login(self):
        # Login
        # self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Locators().username_locator).\
            send_keys(readData.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=Locators().password_locator)\
            .send_keys(readData.yaml_reader()['password'])
        self.driver.find_element(by=By.XPATH, value=Locators().login_button).click()

    # Add new employee
    def test_TC_PIM_01(self):
        self.driver.refresh()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, Locators().pim_locator).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Locators().add_locator).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Locators().first_name).send_keys(readData.yaml_reader()['firstname'])
        self.driver.find_element(By.XPATH, Locators().last_name).send_keys(readData.yaml_reader()['lastname'])
        self.driver.implicitly_wait(15)
        emp_id = self.driver.find_element(By.XPATH, Locators().employee_id)
        emp_id.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        emp_id.send_keys(readData.yaml_reader()['id'])
        self.driver.find_element(By.XPATH, Locators().save_button).click()
        time.sleep(5)

    # Edit existing employee details
    def test_TC_PIM_02(self):
        # Search employee
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, Locators().employee_list).click()
        self.driver.find_element(By.XPATH, Locators().employee_name) \
            .send_keys(readData.yaml_reader()['firstname'])
        self.driver.find_element(By.XPATH, Locators().search_button).click()

        # Add employee details

        # click on Edit icon
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.visibility_of_element_located((By.XPATH, Locators().edit_icon))).click()
        # self.driver.execute_script("arguments[0].click()", edit)
        # Enter license number
        self.driver.find_element(By.XPATH, Locators().license_num) \
            .send_keys(readData.yaml_reader()["license_no"])
        # License Expiry date
        self.driver.find_element(By.XPATH, Locators().license_exp).\
            send_keys(readData.yaml_reader()['license_exp_date'])

        # Nationality
        self.driver.find_element(By.XPATH, Locators().nationality).click()
        self.driver.find_element(By.XPATH, Locators().indian).click()

        # Marital Status
        self.driver.find_element(By.XPATH, Locators().marital_status).click()
        self.driver.find_element(By.XPATH, Locators().married).click()

        # Dob
        self.driver.find_element(By.XPATH, Locators().dob_locator).send_keys(readData.yaml_reader()["dob"])

        # Gender
        action = ActionChains(self.driver)
        gender_radio = self.driver.find_element(By.XPATH, Locators().gender_female_btn)
        action.context_click(gender_radio).perform()
        # save
        self.driver.find_element(By.XPATH, Locators().save_btn1).click()

        # Blood group
        self.driver.find_element(By.XPATH, Locators().blood_group).click()
        self.driver.find_element(By.XPATH, Locators().blood_grp).click()
        # save
        self.driver.find_element(By.XPATH, Locators().save_btn2).click()

        # Job tab

        self.driver.find_element(By.XPATH, Locators.job_locator).click()
        time.sleep(5)
        # Join Date
        self.driver.find_element(By.XPATH, Locators().joined_date).send_keys(readData.yaml_reader()["join_date"])

        # Job title
        self.driver.find_element(By.XPATH, Locators().job_title).click()
        self.driver.find_element(By.XPATH, Locators().qa_engineer).click()

        # sub unit
        self.driver.find_element(By.XPATH, Locators().sub_unit).click()
        self.driver.find_element(By.XPATH, Locators().QA).click()

        # save button
        self.driver.find_element(By.XPATH, Locators().save_btn_job).click()

    # Delete existing employee
    def test_TC_PIM_03(self):

        #  select employee list
        self.driver.find_element(By.XPATH, Locators().employee_list).click()

        # enter employee name
        self.driver.find_element(By.XPATH, Locators().emp_name) \
            .send_keys(readData.yaml_reader()['firstname'])

        # search
        self.driver.find_element(By.XPATH, Locators().search_button).click()

        # Delete
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.visibility_of_element_located((By.XPATH, Locators().delete_icon))).click()

    def test_tearDown(self):
        self.driver.quit()
