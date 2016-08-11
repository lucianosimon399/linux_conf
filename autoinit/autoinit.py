#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import settings
import pexpect

if __name__ == '__main__':
    softwares = settings.SOFTWARES
    for s in softwares:
        print("init %s" % s)
        pexpect.run(r"python3 %s_conf.py" % s)
        print("%s had been initialized." % s)
