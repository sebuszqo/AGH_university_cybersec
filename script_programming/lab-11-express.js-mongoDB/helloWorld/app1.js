// No use of any template system
// noinspection JSVoidFunctionReturnValueUsed

const express = require('express'),
    logger = require('morgan');
const {readFile} = require('fs').promises;

const mongo = require('mongodb');
const client = new mongo.MongoClient('mongodb://localhost:27017');

// creating an app
const app = express();
const x = 1;
const y = 2;

app.set('views', __dirname + '/views');
app.set('view engine', 'pug');
app.locals.pretty = app.get('env') === 'development';

// Informacja dla prowadzącego:
// Jako, że dotychczas w życiu pisałem już trochę w express.js oraz node.js pozwoliłem sobie pisać w sposób uproszczony — funkcje strzałkowe etc. - stwierdziłem, że przy pisaniu tak prostych przykładów nie ma sensu dodatkowe użycie TS

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

const sum = (x,y) => x + y;

const results = (res, o, x, y) =>{
    switch (o) {
        case "+":
            return x + y;
            break
        case "-":
            return x - y;
            break
        case "*":
            return  x * y;
            break
        case "/":
            return x / y;
            break;
        default:
            res.send("Invalid Operation");
            res.end();
            break;
    }
}

app.get("/", (req,res) =>{
 res.send(`<h1>Summing numbers that were hardcoded inside!</h1><p>${x} + ${y} = ${sum(x,y)}</p>`)
})

app.get('/json/:name', async(req,res)=>{
    const fileName = req.params.name
    try{
        const file = await readFile(`./data/${fileName}.json`, "utf-8")
        const data = JSON.parse(file);
        let response = '';
        let restOfMyResponse = '';
        data.forEach(element =>{
            restOfMyResponse += '<tr>'
            restOfMyResponse += `<td text-align="center"> ${element.x} </td>`
            restOfMyResponse += `<td text-align="center"> ${element.o} </td>`
            restOfMyResponse += `<td text-align="center"> ${element.y} </td>`
            const result = results(res, element.o, element.x, element.y)
            restOfMyResponse += `<td text-align="center"> ${result} </td>`
            restOfMyResponse +="</tr>"
        })
        response += `<table class="table" border="solid 1px black">
    <thead>
    <tr>
        <th width="60px"> x </th>
        <th width="60px"> Operation </th>
        <th width="60px"> y </th>
        <th width="60px"> Result </th>
    </tr>
    </thead>
    <tbody>
     ${restOfMyResponse}
    </tbody>
    </table>
    `
        res.send(`${response}`);
    }
    catch (err){
        res.send(`Error during reading a file: ${fileName}`);
        res.end();
    };
});


app.get('/calculate/:operation/:x/:y', (req,res)=>{
    let {x, y, operation} = req.params;
    if (operation === ":"){
        operation = "/"
    }
    x = Number(x)
    y = Number(y)
    if (['+','-','*',':'].includes(req.params.operation)){
        (async () =>{
            try{
                client.connect()
                console.log("Connected to MongoDB")
                const operationObj = {
                    o: operation,
                    x,
                    y,
                    result: results(res,operation, x, y)
                }
                const db = client.db('skryptowe');
                const result = await db.collection("lab11").insertOne(operationObj);
                // console.log(result)

            }
            catch (err){
                console.error("Error has occurred", err)
            }finally {
                await client.close()
            }
        })();
        res.send(`${req.params.x} ${operation} ${req.params.y} = ${results(res, req.params.operation, x, y)}`)
    }
    else {
        throw Error("Invalid operation")
    };
});

app.get('/result', async (req, res) =>{
    try {
        client.connect()
        console.log("Connected to MongoDB")
        const db = client.db('skryptowe')
        const collection = db.collection("lab11")
        const data = collection.find({})
        data.toArray((err,docs)=>{
            if (err) console.error("error occurred", err)
            console.log("Retrieved documents: ", docs)
            client.close()
            res.render("operations", {table: docs})
        });
    }
    catch (err){
        console.error('Cannot connect to MongoDB:', err)
    }
});

// // The application is to listen on http://localhost:3000
app.listen(3000, function () {
    console.log('The application is available on http://localhost:3000');
});

// Usunięcie node_modules
// rm -rf node_modules

// Ponowne przywrócenie aplikacji do życia
// npm i






//Code that our instructor gave us to find out what's express about
//
// // The first route
// app.get('/', function (req, res) {
//     res.send(`
// <!DOCTYPE html>
// <html lang="en" data-bs-theme="dark">
//   <head>
//     <meta charset="utf-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1">
//     <link
//       href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
//       rel="stylesheet"
//       integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
//       crossorigin="anonymous">
//     <title>Your first page</title>
//   </head>
//   <body>
//     <main class="container">
//       <h1>Hello World</h1>
//     </main>
//     <script
//       src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
//       integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
//       crossorigin="anonymous">
//     </script>
//   </body>
// </html>
// `); // Send a response to the browser
// });

