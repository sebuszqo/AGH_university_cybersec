#!/bin/bash 

if [ $# = 0 ]
then
	echo "Podaj cokolwiek plis!"
fi

params=()
#n=$#

for arg in $*
do
	params+=($arg)
done

#echo "${params[@]}"

echo "${params[@]}" | rev
