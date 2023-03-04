#!/bin/bash

# sprawdzam, czy został podany katalog
if [ -z "$1" ]; then
  echo "Nie podano katalogu!"
  exit 1
fi

# pobieram listę plików dowiązań miękkich w podanym katalogu
files=$(find "$1" -type l)

echo "Oto pobrana lista plikow do sprawdzenia: $files"

# sprawdzam, czy znaleziono jakieś dowiązania
if [ -z "$files" ]; then
  echo "Nie znaleziono żadnych dowiązań miękkich w podanym katalogu."
  exit 0
fi

echo "Znaleziono następujące dowiązania miękkie:"

# tworze zmienna counter do zliczania zapętleń
counter=0

# dla każdego znalezionego dowiązania
for file in $files; do
  # sprawdzam, czy jest ono zapętlone
  if [ -L "$file" ]; then
    # wypisuje nazwę pliku i długość zapętlenia
    echo "$file: $(realpath --canonicalize-existing "$file")"
    # inkrementuje counter o 1 bo znaleziono zapetlony link
    counter=$((counter + 1))
  fi
done

# wypisuje liczbę zapętleń
echo "Liczba zapętleń: $counter"
exit 0

