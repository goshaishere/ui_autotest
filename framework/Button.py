from framework.Browser import Browser
from framework.BaseElement import BaseElement


class Button(BaseElement):
    @staticmethod
    def get_the_button(locator):
        return Browser().find_by_x_path(locator=locator)
