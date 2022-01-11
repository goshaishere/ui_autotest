from framework.Browser import Browser
from framework.BaseForm import BaseForm
from framework.Button import Button
from constants import locators as loc


class IframePage(BaseForm):
    def get_page(self, host, path):
        return super().get_page(host=host, path=path)

    def get_paragraph_text(self):
        self.switch_2_iframe_test(iframe_id=loc.LOCATOR_IFRAME)
        element = Browser().find_by_x_path(locator='//p')
        print(element.text)
        return element.text

    def switch_2_iframe_test(self, iframe_id):
        Browser().switch_2_iframe_test(iframe_id=iframe_id)

    def align_text_left(self):
        button = Button().get_the_button(locator=loc.LOCATOR_ALIGN_LEFT)
        Button().click_the_button(button_object=button)

    def align_text_right(self):
        button = Button().get_the_button(locator=loc.LOCATOR_ALIGN_RIGHT)
        Button().click_the_button(button_object=button)

    def align_text_center(self):
        button = Button().get_the_button(locator=loc.LOCATOR_ALIGN_CENTER)
        Button().click_the_button(button_object=button)

    def change_font_size(self):
        pass

    def click_file_new_document(self):
        pass
