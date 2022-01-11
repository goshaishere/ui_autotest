import logging
from task_3.framework.Browser import Browser
from task_3.framework.BaseForm import BaseForm


class PageBasicAuth(BaseForm):
    def get_page(self, host, path, username, password):
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info('trying get the page web element...')
        page_web_element = Browser().go_to_page_with_auth(host=host, path=path, username=username, password=password)
        logging.info('page source is scrapped!')
        return page_web_element
