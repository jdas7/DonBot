from abc import ABC, abstractmethod
from .selenium_utils import SeleniumUtils
from .allure_utils import AllureUtils
from .behave_runner import BehaveRunner


class UtilsFactory(ABC):
    @abstractmethod
    def create_selenium_utils(self):
        pass

    @abstractmethod
    def create_allure_utils(self):
        pass

    @abstractmethod
    def create_behave_runner(self):
        pass


class DefaultUtilsFactory(UtilsFactory):
    def create_selenium_utils(self, driver_path):
        return SeleniumUtils(driver_path)

    def create_allure_utils(self):
        return AllureUtils()

    def create_behave_runner(self):
        return BehaveRunner()
