
if [ $# != 1 ] 
then
	echo "Wlasciwe uzycie to: ./serwer.sh <liczba_gier>"
	exit 1
fi

GAMES=$1
P1=0
P2=0

#Situations:
#0 1
#1 0
#2 1
#1 2
#0 2
#2 0
#If some combination is not there it means it was a draw

while [ $GAMES -gt 0 ] 
do
	echo "start" > komenda.txt

	source ./player1.sh
	source ./player2.sh

	sleep 0.1

	rm -rf komenda.txt

	PICK1=$(cat los1.txt)
	PICK2=$(cat los2.txt)

	echo "Player1: $PICK1	vs   Player2: $PICK2"

	if [[ $PICK1 = 0 && $PICK2 = 2 ]] 
	then
		echo "Player1 won"
		P1=$(($P1 + 1))
	elif [[ $PICK1 = 2 && $PICK2 = 1 ]] 
	then
		echo "Player1 won"
		P1=$(($P1 + 1))
	elif [[ $PICK1 = 1 && $PICK2 = 0 ]] 
	then
		echo "Player1 won"
		P1=$(($P1 + 1))
	elif [[ $PICK1 = 0 && $PICK2 = 1 ]] 
	then
		echo "Player2 won"
		P2=$(($P2 + 1))
	elif [[ $PICK1 = 1 && $PICK2 = 2 ]] 
	then
		echo "Player2 won"
		P2=$(($P2 + 1))
	elif [[ $PICK1 = 2 && $PICK2 = 0 ]] 
	then
		echo "Player2 won"
		P2=$(($P2 + 1))
	else
		echo "Draw"
	fi

	rm -rf los1.txt
	rm -rf los2.txt

	GAMES=$(($GAMES - 1))
done

echo "Player1 scored: $P1"
echo "Player2 scored: $P2"
