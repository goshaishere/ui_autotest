from task_3.framework.Browser import Browser
from task_3.framework.BaseElement import BaseElement


class Paragraph(BaseElement):
    @staticmethod
    def get_the_paragraph(locator):
        return Browser().find_by_x_path(locator=locator)

    @staticmethod
    def get_the_paragraph_style(locator):
        return Browser().get_the_paragraph_style(locator=locator)
