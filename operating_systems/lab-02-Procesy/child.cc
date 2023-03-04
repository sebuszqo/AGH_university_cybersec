#include <iostream>
#include <unistd.h>
#include <sys/types.h>
using namespace std;

int main(){
	// pid_t pid = getpid();
	printf("Its PID:%d\n", getpid());
	getchar(); 
	pid_t child;
	child = fork();
	if(child == 0){
		printf("Child PID: %d\n", getpid());
		printf("Its Parent PID: %d\n", getppid());
		getchar();
	}
	return 0;
}
