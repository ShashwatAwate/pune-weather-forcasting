from setuptools import find_packages,setup

MINUS_E_DOT = "-e ."
def get_packages(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if MINUS_E_DOT in requirements:
            requirements.remove(MINUS_E_DOT)
    return requirements

setup(
    name="pune-weather-forcasting",
    author='shashwat awate',
    packages=find_packages(),
    install_requires=get_packages('D:\coding\Pune_weather_forcasting\\requirements.txt'),
)