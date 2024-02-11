import allure


class AllureUtils:
    @staticmethod
    def attach_screenshot(filename):
        with open(filename, "rb") as file:
            allure.attach(file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
