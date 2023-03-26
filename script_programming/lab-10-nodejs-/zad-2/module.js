const fs = require('fs');

// exports function to use it in script.js

exports.isDirOrFile = (fileOrDirectory) => {
    try {
        const stat = fs.statSync(fileOrDirectory);
        if (stat.isFile()) {
            console.log(`${fileOrDirectory} jest plikiem, a jego zawartością jest:`);
            console.log(fs.readFileSync(fileOrDirectory, 'utf-8'));
            return "file"
        } else if (stat.isDirectory()) {
            console.log(`${fileOrDirectory} jest katalogiem`);
            return "dir"
        } else {
            console.log(`${fileOrDirectory} to coś innego`);
            return "something else"
        }
    } catch (error) {
        return (`Nie udało się odczytać informacji o pliku lub katalogu: ${error}`);
    }
}
