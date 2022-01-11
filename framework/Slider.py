from framework.Browser import Browser
from framework.BaseForm import BaseForm
from framework.Button import Button
from settings import config as cfg
from bs4 import BeautifulSoup
import requests


class Slider(BaseForm):
    def __init__(self):
        self.hang_0 = None
        self.hang_1 = None

    def get_page(self, host, path):
        super().get_page(host=host, path=path)

    def move_slider_test(self, xpath):
        element = Browser().find_by_x_path(xpath=xpath)
        Browser().drag_and_drop(element=element)

    def get_span_status_0(self):
        response = requests.get(cfg.LINK_FOR_3_TASK_ASSERT)
        soup = BeautifulSoup(response.text, 'lxml')
        span_status = soup.span.text
        self.hang_0 = span_status
        print(span_status)

    def get_span_status_1(self):
        response = requests.get(cfg.LINK_FOR_3_TASK_ASSERT)
        soup = BeautifulSoup(response.text, 'lxml')
        span_status = soup.span.text
        self.hang_1 = span_status
        print(span_status)

    def check(self):
        if self.hang_0 is self.hang_1:
            return 1
        return 0
