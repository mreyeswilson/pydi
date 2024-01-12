from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="pydi",
    description="An injection dependecy package for python",
    long_description=readme,
    author="Wilson Mendoza",
    author_email="mreyeswilson@gmail.com",
    packages=find_packages(),
    version="0.0.2",
    readme=readme,
    install_requires=requirements,
    package_dir={"di": "di"}
)