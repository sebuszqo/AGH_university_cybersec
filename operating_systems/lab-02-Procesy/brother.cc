#include <iostream>
#include <unistd.h>
#include <sys/types.h>
using namespace std;

int main(){
	pid_t pid = getpid();
	printf("First PID: %d\n",getpid());getchar();
	pid_t child = fork();
	printf("child fork %d\n", child);
	if(child == 0){
		printf("Child PID's: %d\n", getpid());
		printf("Its Parent PID: %d\n", getppid());
		getchar();

		pid_t grandChild = fork();
		if(grandChild == 0){
			printf("Grandchild's PID: %d\n", getpid());
			printf("Its Parent PID: %d\n", getppid());
		}
	}
    else{
        pid_t brother = fork();
        if(brother == 0){
            printf("Brother's PID: %d\n", getpid());
			printf("Its Parent PID: %d\n", getppid());
        }
    }
	getchar();
	return 0;
}
