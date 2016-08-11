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
