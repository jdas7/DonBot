import subprocess


class BehaveRunner:
    @staticmethod
    def run_tests(tags=None):
        """
        Run Behave tests with configurable options.

        :param tags: Behave tags to filter tests.
        """
        command = ["behave"]

        # Configuration of step and feature paths
        command.extend(["-f", "allure_behave.formatter:AllureFormatter"])
        command.extend(["-o", "allure-results"])

        # Tags configuration
        if tags:
            command.extend(["--tags", tags])

        subprocess.call(command)
