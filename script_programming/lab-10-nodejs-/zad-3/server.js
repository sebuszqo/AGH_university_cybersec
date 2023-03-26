const http = require('http');
const fs = require('fs');
const path = require('path');


// REMEMBER TO RUN SERVER BEFORE TESTING !
// npx nodemon server.js
// then --> npx mocha


async function showFileData(res, absolutePath){
    fs.stat(absolutePath, (err, stats) => {
        if (err){
            res.write('Nie udało mi się znaleźć tego pliku/katalogu, chyba nie istnieje :o.');
            res.end();
        } else if (stats.isFile()){
            fs.readFile(absolutePath, (err, data) => {
                if (err) throw err;
                console.log('Wczytuję plik', data);
                res.write("To jest nazwa pliku. A oto zawartość pliku:\n" + data);
                res.end();
            });
        } else if (stats.isDirectory()){
            res.write('To jest katalog.');
            res.end();
        }
    });
}

http.createServer((req, res) => {
    let url = new URL(req.url, `http://${req.headers.host}`); // Create the URL object
    if (url.pathname == '/submit') {
        let nameToSearch = url.searchParams.get('name');
        console.log(`Sprawdzam ${nameToSearch}`);

        console.log("Tworzę header odpowiedzi");
        res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
        console.log("Tworzę body odpowiedzi");

        if (req.method == 'GET'){
            showFileData(res, path.resolve(nameToSearch));
        }else{
            res.write(`Moja aplikacja nie wspiera takiej metody zapytań jak: ${req.method} method`);
            console.log("Wysyłam odpowiedź");
            res.end();
        }
    }
    else {
        console.log("Tworzę header odpowiedzi")
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        console.log("Tworzę header odpowiedzi");
        res.write(`<form method="GET" action="/submit">
                            <label for="name">Name of file or directory</label>
                            <input name="name">
                            <br>
                            <input type="submit">
                            <input type="reset">
                        </form>`);
        console.log("Wysyłam odpowiedź");
        res.end();
    }
}).listen(8000)

console.log("http://localhost:8000")