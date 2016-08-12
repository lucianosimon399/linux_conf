#-*- coding:utf-8 -*-

import settings
import subprocess 
import os.path
from tools import is_installed

software = "git"

#configure git
def config_it():
    subprocess.Popen(["git","config","--global","user.name",settings.CONF_USER])
    subprocess.Popen(["git","config","--global","user.email",settings.CONF_EMAIL])
    if os.path.exists(os.path.join(settings.USER_DIR, ".ssh/id_rsa")):
        print("id_rsa has exists, do you want to cover it?")
        w = input("[y/n]")
        while not w:
            print("You input nothing,please input again.")
            w = input("[y/n]")
        if w[0] in "yY":
            subprocess.Popen(["ssh-keygen","-t","rsa","-C",settings.CONF_EMAIL])
        else:
            print("Cancel run ssh-keygen")
    else:
        subprocess.Popen(["ssh-keygen","-t","rsa","-C",settings.CONF_EMAIL])

#install and configure git
if is_installed(software):
    config_it()
else:
    if settings.USER_NAME=="root":
        subprocess.Popen(["apt","install",software])
        while not is_installed(software):
            print("%s hadn't been installed. Do you want to install again?" % software)
            w = input("[y/n]")
            while not w:
                print("You input nothing, please input again.")
                w = input("[y/n]")
            if w[0] in "yY":
                config_it()
            else:
                print("Cancel install")
    else:
        print("%s hadn't been installed, please connect to your adminstrator." % software)
