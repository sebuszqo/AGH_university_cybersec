#!/bin/bash

# 0 - kamien
# 1 - papier
# 2 - nozyczki

if [ -f "komenda.txt" ]
then
	COM=$(head -n 1 komenda.txt)
	if [ $COM == "start" ]
       	then
		echo $(($RANDOM%3)) > los2.txt
	fi
fi
