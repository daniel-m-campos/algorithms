from setuptools import setup, find_packages

requirements_file = open("requirements.txt")

setup(
    name="algorithms",
    description="Assignment solutions for Tim Roughgarden's four algorithm courses",
    url="https://github.com/Bocha84/algorithms",
    author="Daniel Campos",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=requirements_file.read().strip().split("\n"),
)

