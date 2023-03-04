#!/bin/bash

# sprawdzam, czy został podany katalog
if [ -z "$1" ]; then
  echo "Nie podano katalogu!"
  exit 1
fi

# pobieram listę plików o więcej niż jednym dowiązaniu twardym
files=$(find "$1" -type f -links +1)

# sprawdzam, czy znaleziono jakieś pliki o więcej niż jednym dowiązaniu twardym
if [ -z "$files" ]; then
  echo "Nie znaleziono żadnych plików o więcej niż jednym dowiązaniu twardym w podanym katalogu."
  exit 0
fi

echo "Znaleziono następujące pliki o więcej niż jednym dowiązaniu twardym:"

# dla każdego znalezionego pliku o więcej niż jednym dowiązaniu twardym
for file in $files; do
  # wypisuje nazwę pliku i liczbę dowiązań twardych
  echo "$file: $(stat --format='%h' "$file") dowiązań twardych"
done

exit 0

