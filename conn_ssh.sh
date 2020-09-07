#!/bin/bash



IP=$1

USER=$2

PASS=$3


sudo sshpass -p  $PASS   ssh $USER@$IP



