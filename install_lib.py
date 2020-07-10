#!/usr/bin/python3

import os
import sys
import subprocess


def fopen(file_name):
    
    if not os.path.exists(file_name):
        print("WARN!!! file not exists")
        sys.exit(1)    
    if not os.path.isfile(file_name):
        print("WARN!!! is not file")
        sys.exit(1)    
    with open(file_name) as f:
        libs = f.read()
        
    return libs
    

def main(file_name):
    print("Begin install ".format(file_name))
    libs_str = fopen(file_name)
    try:
        cmd = "sudo apt install {}".format(' '.join(libs_str.split(',')))
        print(cmd)
        subprocess.call(cmd, shell=True)
        #os.system(cmd)
    except OSError:
        print ('wrongcommand does not exist')

    print("End install")


if  __name__ == "__main__":
    try:
        main(sys.argv[1:][0])
    except KeyboardInterrupt:
        print("Keyboard interrupt exception caught")
