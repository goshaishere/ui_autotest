import logging
import time
from framework.Browser import Browser
from framework.Alerts import Alerts
from framework.Slider import Slider
from framework.Hovers import Hovers
from framework.IframePage import IframePage
from settings import config as cfg
from constants import locators as loc
from constants import paths as path
from constants import test_data


class Test:
    @staticmethod
    def setup():
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info('\n')
        logging.info('*** START OF THE NEW TEST ***\n')

    def test_01(self):
        logging.info('CASE - 1 - START')

        Browser().go_to_page_with_auth(host=cfg.HOST, path=path.PATH_1, username=test_data.USERNAME, password=test_data.PASSWORD)
        assert 'Congratulations! You must have the proper credentials.' in Browser().get_page_source()
        logging.info('assertion passed')

        logging.info('CASE - 1 - OK')

    def test_02(self):
        logging.info('CASE - 2 - START')
        assert 'JavaScript alerts' in Alerts().get_page(host=cfg.HOST, path=path.PATH_2)

        logging.info('assertion 1 passed')
        Alerts().click_first_button()
        Alerts().get_alert()
        assert "I am a JS Alert" in Alerts().get_alert().text
        logging.info('assertion 2 passed')

        Alerts().click_alert(alert=Alerts().get_alert())
        logging.info('alert accepted')
        Alerts().click_second_button()
        Alerts().get_alert()
        assert "I am a JS Confirm" in Alerts().get_alert().text
        logging.info('assertion 3 passed')

        Alerts().click_alert(alert=Alerts().get_alert())
        logging.info('alert accepted')
        Alerts().click_third_button()
        Alerts().get_alert()
        assert "I am a JS prompt" in Alerts().get_alert().text
        logging.info('assertion 4 passed')

        Alerts().send_keys_random(alert=Alerts().get_alert())
        Alerts().click_alert(alert=Alerts().get_alert())
        logging.info('alert accepted')

        logging.info('CASE - 2 - OK')

    def test_03(self):
        logging.info('CASE - 3 - START')
        Slider().get_page(host=cfg.HOST, path=path.PATH_3)
        assert "Horizontal Slider" in Browser().get_page_source()

        this_is_object = Slider()
        this_is_object.get_span_status_0()
        Slider().move_slider_test(xpath=loc.MOVE_SLIDER_LOCATOR)
        this_is_object.get_span_status_1()

        logging.info('assertion is passed')
        logging.info('CASE - 3 - OK')

    def test_04(self):
        logging.info('CASE - 4 - START')

        Hovers().get_page(host=cfg.HOST, path=path.PATH_4)
        assert "Hover over the image for additional information" in Hovers().get_page(host=cfg.HOST, path=path.PATH_4)
        logging.info('assertion 1 passed')

        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_1)
        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_2)

        Hovers().get_page(host=cfg.HOST, path=path.PATH_4)
        assert "Hover over the image for additional information" in Hovers().get_page(host=cfg.HOST, path=path.PATH_4)

        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_1)
        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_2)

        Hovers().get_page(host=cfg.HOST, path=path.PATH_4)
        assert "Hover over the image for additional information" in Hovers().get_page(host=cfg.HOST, path=path.PATH_4)

        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_1)
        Hovers().aim_and_click(locator=loc.LOCATOR_4_1_2)

        Hovers().get_page(host=cfg.HOST, path=path.PATH_4)
        assert "Hover over the image for additional information" in Hovers().get_page(host=cfg.HOST, path=path.PATH_4)

    def test_05(self):

        logging.info('CASE - 5 - START')

        IframePage().get_page(host=cfg.HOST, path=path.PATH_5)
        assert 'An iFrame containing the TinyMCE WYSIWYG Editor' in IframePage().get_page(host=cfg.HOST,
                                                                                          path=path.PATH_5)
        logging.info('assertion 1 passed')

        IframePage().align_text_right()
        IframePage().align_text_left()
        IframePage().align_text_center()

        IframePage().get_paragraph_text()


        # Click File -> New document
        # IframePage().click_file_new_document()
        logging.info('***END OF THE TEST***\n')

    def test_06(self):
        logging.info('CASE - 6 - START')

    @staticmethod
    def teardown():
        Browser().close()

    def go(self):
        self.setup()
        self.test_01()
        self.test_02()
        self.test_03()
        self.test_04()
        self.test_05()
        self.teardown()


a = Test()
a.go()
