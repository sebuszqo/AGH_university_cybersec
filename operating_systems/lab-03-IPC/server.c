#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h> 
#include <netinet/in.h>

struct sockaddr_in server;
int fd; // File descriptor
int conn;
char msg[1] = " ";

int main(){
    server.sin_family = AF_INET;
    server.sin_port = htons(2424);
    printf("Server listening on port `2424`\n");

    fd = socket(AF_INET, SOCK_STREAM, 0);
    bind(fd, (struct sockaddr *)&server, sizeof(server));
    listen(fd, 3); // Max of 3 connections is permitted

    // Connections handling
    while (conn == accept(fd, (struct sockaddr *)NULL, NULL)){
        int pid;
        if ((pid = fork()) == 0){
            while(recv(conn, msg, 256, 0) > 0){
                printf("$> %s\n", msg);
                msg[1] = " ";
            }
            exit(0);
        }
    }

    return 0;
}