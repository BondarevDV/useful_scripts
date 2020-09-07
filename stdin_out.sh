#!/bin/bash

DIR=$1
SAVE_FILE=$2

ls -la  $DIR  >  $SAVE_FILE    2>> error.txt || date>>error.txt 
