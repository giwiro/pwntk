import os
from setuptools import setup

def read(filestr: str):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pwntk",
    version = "0.0.1",
    author = "Gi Wah Davalos",
    author_email = "giwirodavalos@gmail.com",
    description = "GG",
    license = "MIT",
    keywords = "toolkit",
    packages = ["pwntk"],
)

