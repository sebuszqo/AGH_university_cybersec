#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct Element
{
    double** tablica;
    struct Element* nastepny;
};

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Niepoprawna liczba argumentow\n");
        return 1;
    }

    int rozmiar = atoi(argv[1]);

    struct Element* lista = NULL;

    // tworzenie nowych elementów listy
    while (true)
    {
        struct Element* nowy = (struct Element*) malloc(sizeof(struct Element));
        nowy->tablica = (double**) malloc(1000 * sizeof(double*));
        for (int i = 0; i < 1000; i++)
        {
            nowy->tablica[i] = (double*) malloc(1000 * sizeof(double));
        }
        nowy->nastepny = lista;
        lista = nowy;

        // zatrzymanie programu
        printf("Naciśnij klawisz, aby kontynuować...\n");
        getchar();

        if (--rozmiar == 0) break;
    }

    // zwalnianie pamięci
    while (lista != NULL)
    {
        struct Element* stary = lista;
        lista = lista->nastepny;
        for (int i = 0; i < 1000; i++)
        {
            free(stary->tablica[i]);
        }
        free(stary->tablica);
        free(stary);
    }

    return 0;
}

