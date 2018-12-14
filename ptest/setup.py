from setuptools import setup, find_packages

setup(
    name="ptest",
    install_requires="pluggy>=0.3,<1.0",
    entry_points={"console_scripts": ["ptest=ptest.host:main"]},
    packages=find_packages(),
)