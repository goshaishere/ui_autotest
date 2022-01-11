from framework.BaseForm import BaseForm
from framework.Button import Button


class Hovers(BaseForm):
    def get_page(self, host, path):
        return super().get_page(host=host, path=path)

    def aim_and_click(self, locator):
        hover_button = Button().get_the_element_by_xpath(locator=locator)
        Button().move_2_button(button_object=hover_button)
        Button().click_the_button(button_object=hover_button)
