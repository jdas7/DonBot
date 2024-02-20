import subprocess


class BehaveRunner:
    @staticmethod
    def run_tests(steps_path="features/steps", tags=None):
        """
        Run Behave tests with configurable options.

        :param steps_path: Path of the step definition files.
                           Default: "features/steps".
        :param tags: Behave tags to filter tests.
        """
        command = ["behave"]

        # Configuration of step and feature paths
        command.extend(["--steps", steps_path])
        command.extend(["--format", "allure_behave.formatter:AllureFormatter -o allure-results"])

        # Tags configuration
        if tags:
            command.extend(["--tags", tags])

        subprocess.call(command)

    @staticmethod
    def generate_allure_report():
        """
        Generate Allure report from the results and open it.
        """
        subprocess.call(["allure", "generate", "allure-results"])
        subprocess.call(["allure", "open"])
