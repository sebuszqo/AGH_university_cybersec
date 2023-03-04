#!/bin/bash

if [ $# != 2 ]
then
        echo "Wlasciwe  uzycie to:  ./skrypt3.sh <podstawa> <potega>"
        exit 1
fi

if [ $2 == 0 ]
then
        echo "1"
else
	let num=$1**$2
	echo "Liczba to: $num"
fi
