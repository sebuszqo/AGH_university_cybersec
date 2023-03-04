#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>

struct sockaddr_in server;
int fd; // File descriptor
int conn;
char msg[256] = "";

int main(void){
    fd = socket(AF_INET, SOCK_STREAM, 0);

    server.sin_family = AF_INET;
    server.sin_port = htons(2424);

    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr); // Client to localhost
    connect(fd, (struct sockaddr *)&server, sizeof(server)); // Client to server

    // TODO: LISTENING FROM SERVER. Second thread


    while (1) {
        printf("You> ");
        fgets(msg, 256, stdin);
        send(fd, msg, strlen(msg), 0);
    }

    return 0;
}