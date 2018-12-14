from setuptools import setup

setup(
    name="spam",
    install_requires="ptest",
    entry_points={"ptest": ["spam=spam"]},
    py_modules=["spam"],
)