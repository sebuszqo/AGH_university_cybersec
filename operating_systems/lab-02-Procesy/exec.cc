#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
	printf("Hello, I'm exec program!");
	getchar();
	char* args[] = {"./another", NULL};
	execvp(args[0], args);
	/*another has exec pid*/
	printf("Ending");
	return 0;
}
/*
	Exec family of functions replaces the current running process with a new process. It comes under the header
	unistd.h. execvp - the created child process does not have to run the same program as the parent process does.
*/
