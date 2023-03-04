#include <iostream>
#include <new>

using namespace std;

void statyczna();

void dynamiczna();

// RSS:
//
// htop:
//
// 1608 
// 10284 
// 10284 
// 18264 
// 10492 
//
// /proc/[id]/smaps:
// '''awk '/Rss:/{ sum += $2 } END { print sum }' /proc/[id]/smaps'''
// 2680
// 10492
// 10492
// 18308
// 10492
//
//
int main() {

	// start
	cout << "Nacisnij Enter aby kontynuowac" << endl;
	cin.get();

	statyczna();	
	cout << "Statyczna koniec" << endl;

	// mid
	cout << "Nacisnij Enter aby kontynuowac" << endl;
	cin.get();

	dynamiczna();
	cout << "Dynamiczna koniec" << endl;

	// end
	cout << "Nacisnij Enter aby kontynuowac" << endl;
	cin.get();
}

void statyczna() {

	cout << "statyczna start" << endl;
	// stack
	double tablica[1000000];
	for (int i = 0; i < 1000000; i++) {
		tablica[i] = 2.0;
	}
	// stat
	cin.get();
}

void dynamiczna() {

	cout << "dynamiczna start" << endl;
	// heap
	double *tablica = new double[1000000];
	for (int i = 0; i < 1000000; i++) {
		tablica[i] = 3.0;
	}
	// dyna
	cin.get();

	delete[] tablica;
}

