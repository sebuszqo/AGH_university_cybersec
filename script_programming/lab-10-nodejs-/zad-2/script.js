const { isDirOrFile } = require('./module');

let fileOrDir = process.argv.slice(-1);

console.log(isDirOrFile(fileOrDir[0]))

// node script.js plik.txt
// node script.js /etc