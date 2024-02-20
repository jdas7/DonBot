import allure


class AllureUtils:
    @staticmethod
    def attach_screenshot(filename):
        """
        Attach a screenshot to Allure report.

        :param filename: The path to the screenshot file.
        """
        with open(filename, "rb") as file:
            allure.attach(file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
