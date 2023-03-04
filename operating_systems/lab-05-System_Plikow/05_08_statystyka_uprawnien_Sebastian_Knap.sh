#!/bin/bash

# sprawdzam, czy został podany katalog
if [ -z "$1" ]; then
  echo "Nie podano katalogu!"
  exit 1
fi

# pobieram listę plików w podanym katalogu i podkatalogach
files=$(find "$1" -type f)

#echo $files

# sprawdam, czy znaleziono jakieś pliki
if [ -z "$files" ]; then
  echo "Nie znaleziono żadnych plików w podanym katalogu."
  exit 0
fi

echo "Statystyka plików w drzewie katalogów:"

# dla każdego znalezionego pliku
for file in $files; do
  # wyświetlam statystykę pliku
  stat -c "%A %n" "$file"
done

exit 0

