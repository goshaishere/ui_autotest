import logging
from framework.Browser import Browser
from abc import ABC, abstractmethod


class BaseForm(ABC):
    """прародитель страницы и айфреймстраницы"""
    def __init__(self):
        self.locator = None
        self.name = None
        self.page_web_element = None

    def get_page(self, host, path):
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info('trying get the page web element...')
        self.page_web_element = Browser().go_to_page(host=host, path=path)
        logging.info('page source is scrapped!')
        return self.page_web_element

    def is_displayed(self):
        pass

    def click(self):
        pass

    def find_element(self):
        pass
