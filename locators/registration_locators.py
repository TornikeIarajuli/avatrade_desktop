from selenium.webdriver.common.by import By


class RegistrationLocators:
    _register_now = (By.ID, 'btn_ga_real_header')
    _email = (By.ID, 'input-email')
    _password = (By.ID, 'input-password')
    _create_account_btn = (By.ID, 'btn_ga_real_main menu_cfd')
    _frame = (By.CSS_SELECTOR, 'iframe[data-qa="iframe__container"]')
    _first_name = (By.ID, 'question-1_247')
    _last_name = (By.ID, 'question-2_248')
    _date_day = (By.ID, 'date-day')
    _date_month = (By.ID, 'date-month')
    _date_year = (By.ID, 'date-year')
    # _country = (By.ID, 'input-129')
    _country = (By.XPATH, '//*[@id="question-5_250"]/div/div/div[1]/div[2]/div[1]')
    _city = (By.ID, 'question-6_3')
    _city_france = (By.ID, 'question-7_3')
    _street_name = (By.ID, 'question-7_94')
    _street_name_france = (By.ID, 'question-8_94')
    _number = (By.ID, 'question-8_95')
    _number_france = (By.ID, 'question-9_95')
    _postal_code = (By.ID, 'question-10_5')
    _postal_code_france = (By.ID, 'question-11_5')
    _phone_number = (By.ID, 'phone-number-input')
    _continue_btn = (By.XPATH, '//*[@id="scroll-target"]/div[2]/div/div/form/div/div[2]/div/button')
    _occupation = (By.ID, 'question-1_15')
    _employment = (By.ID, 'question-2_91')
    _income = (By.ID, 'question-4_16')
    _income_france = (By.ID, 'question-4_88')
    _source_funds = (By.ID, 'question-3_18')
    _investments = (By.ID, 'question-5_89')
    _financial_risk = (By.ID, 'question-6_90')
    _terms_and_conditions = (By.XPATH, '//*[@id="question-2_21"]/div/div/div/div[1]/div/div[2]')
    _financial_continue_btn = (By.XPATH, '//*[@id="scroll-target"]/div[3]/div/div/form/div/div[2]/div/button')
    _finish_btn = (By.XPATH, '//*[@id="scroll-target"]/div[4]/div/div/form/div/div[2]/div/button')
