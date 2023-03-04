#include <iostream>
#include <signal.h>
#include <unistd.h>
using namespace std;
// SIGKILL, SIGSTOP cannot be handled
void sigHandler(int sig){
	if( sig == SIGINT )
		cout << "Caught SIGINT" << endl;
	else if( sig == SIGKILL )
		cout << "Caug`ht SIGKILL" << endl;
}
int main(){

	pid_t pid = getpid();
    printf("pid: %d\n", pid);
	if(signal(SIGINT, sigHandler) == SIG_ERR)
		cout << "\nCannot catch SIGINT" << endl;
	if(signal(SIGKILL, sigHandler) == SIG_ERR)
		cout << "\nCannot catch SIGKILL" << endl;


	while(1){
		cout << "................" << endl;
		sleep(1);
	}
	return 0;
}
