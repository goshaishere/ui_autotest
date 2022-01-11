from framework.Browser import Browser
from abc import ABC, abstractmethod
from features.DriverTool import DriverTool
from selenium.webdriver import ActionChains


class BaseElement(ABC):
    """прародитель кнопки и текстфилда"""
    def __init__(self):
        self.element = None
        self.name = None
        self.locator = None

    def is_displayed(self):
        pass

    def wait_for_open(self):
        pass

    def get_the_element_by_xpath(self, locator):
        element = Browser().find_by_x_path(locator=locator)
        return element

    def get_the_element_by_css(self):
        element = Browser().find_by_css_selector(self.locator)
        return element

    def move_2_button(self, button_object):
        driver = DriverTool.get_instance()
        actions = ActionChains(driver)
        actions.move_to_element(button_object).perform()

    def click_the_button(self, button_object):
        actions = ActionChains(DriverTool.get_instance())
        actions.click(button_object).perform()
