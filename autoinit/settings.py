import getpass
from os import path

SOFTWARES = [
        'git',
        'vim',
        'zsh',
]

BASE_DIR = path.abspath("..")
USER_DIR = path.expanduser("~")
USER_NAME = getpass.getuser()
CONF_USER = "Luciano Simon"
CONF_EMAIL = "lucianosimon399@yahoo.com"
