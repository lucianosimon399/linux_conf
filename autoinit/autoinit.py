#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time
from tools import bcolors
from os.path import join
from os.path import exists
import subprocess
from settings import SOFTWARES
from settings import BASE_DIR

if __name__ == '__main__':
    for sft in SOFTWARES:
        print("---------------------------------")
        print("init %s" % sft)
        sft_path = join(BASE_DIR, "autoinit/%s_conf.py" % sft)
        try:
            if not exists(sft_path):
                raise FileNotFoundError("[Error]%s:No such file." % sft_path)
            child = subprocess.Popen(["python3", sft_path])
            child.wait()
        except FileNotFoundError as e:
            print(bcolors.WARNING + e.__str__() + bcolors.ENDC)
        else:
            print("%s had been initialized." % sft)
        print("---------------------------------")
        time.sleep(1)
