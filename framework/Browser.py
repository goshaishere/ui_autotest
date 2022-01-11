from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from features.DriverTool import DriverTool
import logging
import random
from settings import config as cfg


class Browser:
    def __init__(self):
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info('check webdriver')
        self.driver = DriverTool.get_instance()

    def get_page_source(self):
        return self.driver.page_source

    @staticmethod
    def url_plus_host_f_string_maker(username, password, host, path):
        rev = host[::-1]
        i = rev.find('/')
        clean_host = rev[0:i:1]
        clean_host = clean_host[::-1]
        return f"https://{username}:{password}@{clean_host}{path}"

    def go_to_page_with_auth(self, host, path, username, password):
        url = self.url_plus_host_f_string_maker(username=username, password=password, host=host,
                                                path=path)
        print(url)
        logging.info(f'{url}')
        logging.info('open the link...')
        self.driver.get(url)
        logging.info('link was opened!')
        self.driver.maximize_window()
        return self.driver.page_source

    def close(self):
        self.driver.close()

    def quit(self):
        logging.info('web browser - quit')
        self.driver.close()

    def go_to_page(self, host, path):
        rev = host[::-1]
        i = rev.find('/')
        clean_host = rev[0:i:1]
        clean_host = clean_host[::-1]
        url = f"https://{clean_host}{path}"
        print(url)
        logging.info(f'{url}')
        logging.info('open the link...')
        self.driver.get(url)
        logging.info('link was opened!')
        self.driver.maximize_window()
        return self.driver.page_source

    def find_by_css_selector(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def find_by_x_path(self, locator):
        element = self.driver.find_element_by_xpath(xpath=locator)
        return element

    def wait_for_present_switch_2_alert(self):
        WebDriverWait(driver=self.driver, timeout=cfg.N).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert

    def drag_and_drop(self, element):
        random_integer = random.randint(1, 500)
        random_integer = random_integer/10
        print(random_integer)
        ActionChains(self.driver).drag_and_drop_by_offset(element, random_integer, 0).release().perform()

    def get_slider_status(self, locator):
        info = self.find_by_x_path(locator=locator)
        return info.text

    def move_2_button(self, button_object):
        driver = DriverTool().get_instance()
        actions = ActionChains(driver)
        actions.move_to_element(button_object).perform()

    def get_p_styles(self, locator):
        element = self.find_by_x_path(locator=locator)
        element_styles = element.value_of_css_property("text-align")
        print(element)
        print(element_styles)
        return element_styles

    def switch_2_frame(self):
        self.driver.switch_to.frame()

    def switch_2_iframe_test(self, iframe_id):
        iframe = self.driver.find_element(By.ID, iframe_id)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def click_on_iframe_pin(self, xpath_locator):
        add = WebDriverWait(self.driver, cfg.N).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                                     xpath_locator)))
        add.click()

    def get_the_paragraph_style(self, locator):
        self.driver.find_element(By.XPATH(locator)).text
