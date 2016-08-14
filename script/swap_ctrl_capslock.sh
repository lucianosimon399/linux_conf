#!/bin/sh

### BEGIN INIT INFO
# Provides:          lucinao
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# X-Interactive:     true
# Short-Description: xmodmap script
# Dscription:        
#                    This shell script was used to swap Ctrl and CapsLock when system reboot.
#                    It should be copy to /etc/init.d/ dirctory. and add it to auto-execute queue
#                    by command "sudo update-rc.d [SCRIPT NAME] defaults [RUN LEVEL]".
### END INIT INFO


xmodmap -e "remove Lock = Caps_Lcok"
xmodmap -e "remove Control = Control_L"
xmodmap -e "keysym Control_L = Caps_Lock"
xmodmap -e "keysym Caps_Lock = Control_L"
xmodmap -e "add Lock = Caps_Lock"
xmodmap -e "add Control = Control_L"
