from setuptools import setup, find_packages

with open('requirements.txt','r') as req_file:
    required_packages= req_file.readlines()

with open('README.md','r') as readme_file:
    long_description=readme_file.read()

setup(
    name="pymusicterm",
    # version=""
    author="Gamaliel Garcia",
    desciption="A music player and spotify client for a terminal",
    long_description=long_description,
    url="https://github.com/EGAMAGZ/pymusicterm",
    # license=""
    keyword="git cli cui curses command-line",
    packages=find_packages(exclude=['tests','docs']),
    entry_points={
        'console_scripts':['pymusicterm = pymusicterm:main',]
    },
    install_requires=required_packages,
)
