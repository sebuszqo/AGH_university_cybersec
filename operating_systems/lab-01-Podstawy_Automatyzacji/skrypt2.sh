#!/bin/bash

if [ $# != 2 ]; then
	echo "Prawidlowe uzycie to:  ./skrypt2 <min> <max>"
	exit 1
fi

random_num=$(((RANDOM % $2) + $1 ))
#echo $random_num

count=1
read GUESS
while [ $GUESS -ne $random_num ]
do
	if [ $count -lt 10 ]
	then
		if [ $GUESS -lt $random_num ]
		then 
			echo 'Wiecej!'
		else
			echo 'Mniej!'
		fi
		count=$(($count + 1))
		read GUESS
	else
		echo "Za duzo prob ... Limit to 10!"
		exit 1
	fi
done

echo "Wygrales, twoja liczba to: $random_num"


