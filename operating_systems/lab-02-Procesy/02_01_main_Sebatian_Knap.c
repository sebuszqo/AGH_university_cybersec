#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int staticMemGlobal = 20;
int* dynamicMemGlobal;

int main(){
    int number1, number2, number3;
    FILE *file = fopen("./txtFile.txt", "w");
    int staticMemLoc = 20;
    int* dynamicMemLoc = (int*)malloc(sizeof(int)*10); //10ints
    dynamicMemLoc[9] = 1;
    dynamicMemGlobal = (int*)malloc(sizeof(int)*20); //20ints
    dynamicMemGlobal[19] = 2;

    pid_t pid = fork();
    printf("PiD: %d\n",pid);
    if(pid < 0){
        fprintf(stderr, "Fork Failes");
        return 1;
    }
    else if(pid == 0){
        // execlp("/bin/ls","ls",NULL);
        // pstree <child's PID> // main
        // pstree <its parent PID> // main---main
        printf("Child's PID: %d\n", getpid());
		printf("Its Parent PID: %d\n", getppid());
        scanf("%d", &number1);
    }
    else{
        // wait(NULL);
        scanf("%d", &number2);
        printf("Parent's PID: %d\n", getpid());
		printf("Its Parent PID: %d\n", getppid());
        printf("Child Complete\n");
        scanf("%d", &number3);
    }
    // Rodzic odczyta wprowadzone dane z klawiatury
    // printf("%d\n", number2);

    // 9152 procesów potomnych uda się utworzyć
    return 0;
}