from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class DriverTool:
    __instance__ = None

    def __init__(self):
        if DriverTool.__instance__ is not None:
            raise RuntimeError("Cannot init class twice, as it is as singelton")
        else:
            DriverTool.__instance__ = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    @classmethod
    def get_instance(cls):
        """
        :rtype: WebDriver
        """
        if cls.__instance__ is None:
            DriverTool()
        return cls.__instance__
