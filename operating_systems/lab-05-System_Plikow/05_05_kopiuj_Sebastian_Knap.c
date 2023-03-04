#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    // sprawdzam, czy zostały podane wszystkie wymagane parametry
    if (argc != 4) {
        printf("Niepoprawna liczba parametrów!\n");
        printf("Użycie: kopiuj <rozmiar bufora> <plik.src> <plik.trg>\n");
        return 1;
    }

    // pobieram rozmiar bufora i nazwy plików
    int buf_size = atoi(argv[1]);
    char *src_name = argv[2];
    char *trg_name = argv[3];

    // otwieram plik źródłowy i docelowy
    FILE *src_file = fopen(src_name, "rb");
    if (src_file == NULL) {
        perror("Błąd otwierania pliku źródłowego");
        return 1;
    }
    FILE *trg_file = fopen(trg_name, "wb");
    if (trg_file == NULL) {
        perror("Błąd otwierania pliku docelowego");
        return 1;
    }

    // rezerwuje pamięć na bufor
    char *buffer = malloc(buf_size);
    if (buffer == NULL) {
        perror("Błąd alokacji pamięci");
        return 1;
    }

    // zapisuje początek czasu
    clock_t start = clock();

    // kopiuje plik, tak długo jak są dane do odczytu
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, buf_size, src_file)) > 0) {
        fwrite(buffer, 1, bytes_read, trg_file);
    }

    // zapisuje koniec czasu
    clock_t end = clock();

    // zamkykam pliki
    fclose(src_file);
    fclose(trg_file);

    // wyświetlam wyniki tj. rozmiar bufora i czas kopiowania
    printf("Rozmiar bufora: %d bajtów\n", buf_size);
    printf("Czas kopiowania: %.2fs\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}

