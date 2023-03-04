#include<stdio.h>
#include<signal.h>
#include<unistd.h>
#include<stdlib.h>

int main(int argc, char **argv){
    int pid = atoi(argv[1]);
    printf("PID = %d\n", pid);
    // SIGINT = 2
    kill(pid, atoi(argv[2]));
    return 0;
}