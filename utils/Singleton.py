from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def get_driver(self):
        if self.driver is None:
            c_options = Options()
            c_options.add_argument("--enable-automation")
            c_options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(options=c_options, service=Service(ChromeDriverManager().install()))
            self.driver.maximize_window()
        return self.driver


    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def find_element(self, by, value: str, timeout=10):
        driver = self.get_driver()
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value)))
            return element
        except Exception as e:
            raise e

    def navigate_to(self, url):
        driver = self.get_driver()
        driver.get(url)

    def wait_for_element_clickable(self, by, value: str, timeout=10):
        driver = self.get_driver()
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value)))
            return element
        except Exception as e:
            raise e

    def click_element(self, by, value: str, timeout=10):
        element = self.wait_for_element_clickable(by, value, timeout)
        element.click()

    def input_text(self, by, value: str, text, timeout=10):
        element = self.wait_for_element_clickable(by, value, timeout)
        element.send_keys(text)

    def switch_to_frame(self, by, value: str, timeout=10):
        driver = self.get_driver()
        try:
            frame = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value)))
            return frame
        except Exception as e:
            raise e

    def switch_to_default_content(self):
        self.get_driver().switch_to.default_content()

    def get_current_url(self):
        return self.get_driver().current_url
