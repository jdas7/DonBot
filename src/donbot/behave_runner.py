import subprocess


class BehaveRunner:
    @staticmethod
    def run_tests(tags=None):
        command = ["behave"]
        if tags:
            command.extend(["--tags", tags])
        subprocess.call(command)
