#include <iostream>
#include <unistd.h>
#include <sys/types.h>
using namespace std;

int main(){
	pid_t pid = getpid();
	pid_t child;
	child = fork();
	if(child == 0){
		printf("Child PID: %d\n", getpid());
		printf("Its Parent PID: %d\n", getppid());
		getchar();

		pid_t grandChild;
		grandChild = fork();
		getchar();
		if(grandChild == 0){
			printf("Grandchild PID: %d\n", getpid());
			printf("Its Parent PID: %d\n", getppid());
			getchar();
		}
	}
	return 0;
}
