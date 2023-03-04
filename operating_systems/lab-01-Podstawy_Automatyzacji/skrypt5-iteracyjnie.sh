#!/bin/bash 

if [ $# = 0 ]
then
        echo "Podaj cokolwiek plis!"
fi

for (( i=$#;i>0;i-- ))
do
	echo -n "${!i} "
done

printf "\n"
