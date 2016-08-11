#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from settings import BASE_DIR
import pexpect
import getpass
import os
from tools import is_installed

#set required variables
software = 'vim'
username = getpass.getuser()
local_userconf = os.path.join(BASE_DIR, "vim_conf/_vimrc")
target_userconf = "/home/%s/.vimrc" % username
local_globalconf = os.path.join(BASE_DIR, "vim_conf/vimrc")
target_globalconf = "/usr/share/vim/vimrc"
is_root = False
if username=="root":
    is_root = True

#config vim
def config_it():
    #configure personal config
    if os.path.exists(target_userconf):
        print("%s is already exists, are you want to cover it?" % target_userconf)
        w = input("[y/n]: ")
        while not w:
            print("You input nothing, please input again.")
            w = input("[y/n]: ")
        if w[0] in 'yY':
            print("Configuring user's vim config")
            pexpect.run(r"cp %s %s" % (local_userconf, target_userconf))
            print("User's vim config is over")
        else:
            print("Keep original.")
    else:
        pexpect.run(r"cp %s %s" % (local_userconf, target_userconf))
    #configure global config
    if is_root:
        print("Configuring gloabl vim config.")
        pexpect.run(r"cp %s %s" % (local_globalconf, target_globalconf))
        print("Global vim config is over.")

#install vim and config it
if is_installed(software):
    config_it()
else:
    if not is_root:
        print("Software %s hadn't been installed, please connect to your administrator." % software)
    else:
        pexpect.run("apt install %s" % software)
        config_it()
print("Vim had been configured.")
