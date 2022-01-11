import logging
from framework.Browser import Browser
from settings import config as cfg
from framework.Button import Button
from features.Randomizer import Randomizer


class Alerts:
    @staticmethod
    def get_page(host, path):
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info('trying get the page web element...')
        page_web_element = Browser().go_to_page(host=host, path=path)
        logging.info('page source is scrapped!')
        return page_web_element

    @staticmethod
    def click_first_button():
        alert_button = Button(locator=cfg.LOCATOR_2_1).get_the_button()
        alert_button.click()

    @staticmethod
    def get_alert():
        alert = Browser().wait_for_present_switch_2_alert()
        return alert

    @staticmethod
    def click_alert(alert):
        alert.accept()

    @staticmethod
    def click_second_button():
        alert_button = Button(locator=cfg.LOCATOR_2_2).get_the_button()
        alert_button.click()

    @staticmethod
    def click_third_button():
        alert_button = Button(locator=cfg.LOCATOR_2_3).get_the_button()
        alert_button.click()

    @staticmethod
    def send_keys_random(alert):
        keys_to_send = Randomizer(length=cfg.SIZE_RANDOM_TEXT).get_rand_string()
        alert.send_keys(keysToSend=keys_to_send)
