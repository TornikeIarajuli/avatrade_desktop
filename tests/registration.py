import time

from utils.Singleton import Singleton
from steps.registration_steps import RegistrationSteps
from locators.registration_locators import RegistrationLocators
import pytest
from faker import Faker

driver = Singleton()
faker = Faker()
locator = RegistrationLocators()


class TestRegistration(RegistrationSteps):

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = driver
        try:
            self.driver.get_driver()
            self.driver.navigate_to('https://www.avatrade.com/?mode=test-static-widget')
            yield
        finally:
            try:
                self.driver.quit_driver()
            except Exception as e:
                print(e)

    #Could be done better with pytest.mark.parametrize if not for changing locators
    def test_01register_afghanistan(self):
        self.click_register_now()
        self.fill_email(faker.email())
        self.fill_password("!P1asssss")
        self.click_create_account()
        self.switch_frame()
        self.fill_first_name(faker.first_name())
        self.fill_last_name(faker.last_name())
        self.fill_day('19')
        self.fill_month('11')
        self.fill_year('1999')
        self.fill_country('afghanistan')
        self.fill_city(locator._city, faker.city())
        # self.fill_city(faker.city())
        self.fill_street(locator._street_name, faker.street_name())
        self.fill_number(locator._number, 22)
        self.fill_postal_code(locator._postal_code, 1190)
        self.fill_phone_number(551554588)
        self.click_continue()
        self.occupation_select()
        self.employment_select()
        self.source_funds_select()
        self.income_select()
        self.investments_select()
        self.financial_risk_select()
        self.click_financial_continue()
        self.click_terms_and_conditions()
        self.click_finish_button()
        self.fill_country()

    def test_02register_france(self):
        self.click_register_now()
        self.fill_email(faker.email())
        self.fill_password("!P1asssss")
        self.click_create_account()
        self.switch_frame()
        self.fill_first_name(faker.first_name())
        self.fill_last_name(faker.last_name())
        self.fill_day('19')
        self.fill_month('11')
        self.fill_year('1999')
        self.fill_country('france')
        self.fill_city(locator._city_france, faker.city())
        self.fill_street(locator._street_name_france, faker.street_name())
        self.fill_number(locator._number_france, 22)
        self.fill_postal_code(locator._postal_code_france, 1190)
        self.fill_phone_number(551554588)
        self.click_continue()
        self.occupation_select()
        self.employment_select()
        self.source_funds_select()
        self.income_select_france()
        self.investments_select()
        self.financial_risk_select()
        self.click_financial_continue()
        self.click_terms_and_conditions()
        self.click_finish_button()
        self.fill_country()

