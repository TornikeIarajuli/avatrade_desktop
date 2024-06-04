import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import RegistrationLocators
from utils.Singleton import Singleton
from selenium.webdriver.common.keys import Keys

driver = Singleton()


class RegistrationSteps(RegistrationLocators):

    def generic_click(self, locator: tuple) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

    def generic_select(self, locator: tuple) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        actions.send_keys(Keys.DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()

    # I wrote this for fill-based functions, but for some reasons isn't working like others
    # def generic_fill(self, locator: tuple, text: str) -> None:
    #     driver = self.driver.get_driver()
    #     element = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable(locator)
    #     )
    #     actions = ActionChains(driver)
    #     actions.move_to_element(element).click().send_keys(text).perform()

    def click_register_now(self) -> None:
        driver.find_element(*self._register_now).click()

    def fill_email(self, email: str) -> None:
        driver.find_element(*self._email).send_keys(email)

    def fill_password(self, password: str) -> None:
        driver.find_element(*self._password).send_keys(password)

    def click_create_account(self) -> None:
        driver.find_element(*self._create_account_btn).click()

    def switch_frame(self) -> None:
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located(self._frame))
        driver.get_driver().switch_to.frame(iframe)

    def fill_first_name(self, first_name: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._first_name)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(first_name).perform()

    def fill_last_name(self, last_name: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._last_name)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(last_name).perform()

    def fill_day(self, day: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._date_day)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(day).perform()

    def fill_month(self, month: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._date_month)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(month).perform()

    def fill_year(self, year: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._date_year)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(year).perform()

    def fill_country(self, name: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._country)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(name).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)

    def fill_city(self, locator, city: str) -> None:
        driver = self.driver.get_driver()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)

        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(city).perform()

    def fill_street(self, locator, street: str) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(street).perform()

    def fill_number(self, locator, number: int) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(number).perform()

    def fill_postal_code(self, locator, postal_code: int) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(postal_code).perform()

    def fill_phone_number(self, phone_number: int) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._phone_number)
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(phone_number).perform()
        driver.implicitly_wait(1)

    def click_continue(self) -> None:
        self.generic_click(self._continue_btn)

    def occupation_select(self) -> None:
        self.generic_select(self._occupation)

    def employment_select(self) -> None:
        self.generic_select(self._employment)
        time.sleep(1)

    def source_funds_select(self) -> None:
        self.generic_select(self._source_funds)
        time.sleep(1)

    def income_select(self) -> None:
        self.generic_select(self._income)
        time.sleep(1)

    def income_select_france(self) -> None:
        self.generic_select(self._income_france)
        time.sleep(1)

    def investments_select(self) -> None:
        driver = self.driver.get_driver()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self._investments)
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.generic_select(self._investments)
        time.sleep(1)

    def financial_risk_select(self) -> None:
        self.generic_select(self._financial_risk)

    def click_financial_continue(self) -> None:
        self.generic_click(self._financial_continue_btn)
        driver.get_driver().implicitly_wait(1)

    def click_terms_and_conditions(self) -> None:
        self.generic_click(self._terms_and_conditions)

    def click_finish_button(self) -> None:
        self.generic_click(self._finish_btn)

