import subprocess


class BehaveRunner:
    @staticmethod
    def run_tests(steps_path="features/steps", features_path="features", tags=None):
        """
        Run Behave tests with configurable options.

        :param steps_path: Path of the step definition files.
                           Default: "features/steps".
        :param features_path: Path to the .feature files.
                              Default: "features".
        :param tags: Behave tags to filter tests.
        """
        command = ["behave"]

        # Configuration of step and feature paths
        command.extend(["--steps", steps_path])
        command.extend(["--no-capture", "--format", "allure_behave.formatter:AllureFormatter"])
        if features_path:
            command.extend([features_path])

        # Tags configuration
        if tags:
            command.extend(["--tags", tags])

        subprocess.call(command)

        # Generate Allure report after test execution
        subprocess.call(["allure", "serve", "allure-results"])
