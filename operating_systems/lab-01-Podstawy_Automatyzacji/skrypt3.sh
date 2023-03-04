#!/bin/bash

if [ $# != 2 ]
then
	echo "Wlasciwe  uzycie to:  ./skrypt3.sh <podstawa> <potega>"
	exit 1
fi

count=1
num=$1

if [ $2 == 0 ]
then
	echo "1"
else
	while [ $count -lt $2 ]
	do
		count=$(($count + 1 ))
		num=$(($num * $1))
	done

	echo "Liczba to: $num"
	exit 1 
fi
	
