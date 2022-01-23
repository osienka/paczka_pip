from setuptools import setup

import toml

with open("data.toml") as f_p:
    data = toml.load(f_p)

setup(
    name="homework_exercise",
    version = "0.1",
    license_files = 'LICENSE.txt'
)
