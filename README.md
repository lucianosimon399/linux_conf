#LINUX_CONF
----------------------
##Author:Luciano Simon
##Date:2016-08-11 21:33
-------------------------

I had improved this project to a software(or script, or something like).

You don't need to cp config by yourself, these python scripts can help you to configure your Ubuntu system.

It default to configure `git`, `vim`, `zsh`. Of course you can custom it by yourself.If you want to custom your own scripts, you need to add the software's name into the list `SOFTWARES` in the file `autoinit/settings.py', and you your python script(Please use python3's syntax), and the scripts' name should be ` <softwareName\>_conf.py`(like `git_conf.py`).