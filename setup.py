from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='DonBot',
    version='1.0',
    author='Juan David Alvis Sanchez',
    description='Una biblioteca para automatizar pruebas con Selenium, Allure y Behave con python',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
)
