#!/bin/bash

# zadanie 1

# ./skrypt01.sh <katalog> <wielkość>


if [ $# != 2 ] 
then
	echo "Poprawne uzycie to ./skrypt01.sh <katalog> <wielkość>"
	exit 1
fi

if [ ! -d $1 ] 
then
	echo "$1 nie jest katalogiem !"
	exit 1
fi

find $1 -type f -size +$2c -printf "%T@ %p\n" | sort -n | cut -d' ' -f2 | tail -n 1
#find $1 -type f -size +$2c  | sort -n | cut -d' ' -f2 | tail -n 1
