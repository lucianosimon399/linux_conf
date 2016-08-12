import pexpect
from os.path import exists

def is_installed(sft):
    out = pexpect.run("which %s" % sft)
    if out == b'':
        return False
    elif exists(out.split(b'\r\n')[0].decode()):
        return True
    else:
        raise Exception("You really should have a look. There is something really wrong in tools.py")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_input(prompt):
    m = input(prompt)
    while not m:
        print("You input nothing, please again.")
        m = input(prompt)
    return m
