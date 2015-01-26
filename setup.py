from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

setup(
    # Application name:
    name="Jasper Web Serever Report",

    # Version number (initial):
    version="0.1.2",

    # Application author details:
    author="Luis Fernandes",
    author_email="luisfmfernandes@gmail.com",

    # Packages
    packages=find_packages(),#["jasperserver"],

    # Include additional files into the package
    include_package_data=True,
    #
    # license="LICENSE.txt",
    description="Web rest to jasperserver.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=install_requires,
)
