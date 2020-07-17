#!/usr/bin/bash



ifconfig $1 down

brctl delbr $1
