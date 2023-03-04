#include <stdio.h>
#include <stdlib.h>

int main(){
	printf("Hello,  I'm system program!\n");
	getchar();
	system("ls -al /var/log/");
	// getchar();
	return 0;
}
