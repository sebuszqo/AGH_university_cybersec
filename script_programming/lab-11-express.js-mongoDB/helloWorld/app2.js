// Application using the 'Pug' template system
const express = require('express'),
    logger = require('morgan');
const {readFile} = require('fs').promises;
const app = express();
let x = 1;
let y = 2;

const mongo = require('mongodb');
const client = new mongo.MongoClient('mongodb://localhost:27017');


// *** Functions definitions ***

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
            break
        default:
            res.send("Invalid Operation");
            res.end();
            break;
    }
}

// Configuring the application
app.set('views', __dirname + '/views');               // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');                        // Use the 'Pug' template system
app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', (req, res) => {
    // res.render('index', {sum: `${x} + ${y} = ${sum(x,y)}`})
    res.render('sum', {sum: `${x} + ${y} = ${sum(x,y)}`}); // Render the 'index' view
});

app.get('/json/:name', async(req,res)=>{

    const fileName = req.params.name
    try {
        const file = await readFile(`./data/${fileName}.json`, "utf-8")
        const data = JSON.parse(file)
        data.forEach(element =>
            element.result = results(res, element.o, element.x, element.y)
        )
        // res.render('index', {table: data})
        res.render('operations',{table: data})
    }
    catch (err){
        res.send(`Error occurred during reading a file: ${fileName}`)
    }
}
);

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
                await client.connect()
                console.log("Connected to MongoDB")
                const operationObj = {
                    o: operation,
                    x,
                    y,
                    result: results(res,operation, x, y)
                }
                const db = client.db('skryptowe');
                const result = await db.collection("lab11").insertOne(operationObj);
                console.log(result)

            }
            catch (err){
                console.log("Error has occurred")
            }finally {
                await client.close()
            }
        })();
        let rep = `${req.params.x} ${operation} ${req.params.y} = ${results(res, req.params.operation, x, y)}`
        res.render('index', {sum: rep})
    }
    else {
        throw Error("Invalid operation")
    };
});

app.get('/result', (req, res)=>{
    client
        .connect()
        .then(()=>{
            console.log("Connected to MongoDB")
            const db = client.db('skryptowe')
            db.collection("lab11")
                .find({})
                .toArray((err,docs)=>{
                    if (err) console.error("error occurred", err)
                    console.log("Retrieved documents: ", docs)
                    client.close()
                    res.render("operations", {table: docs})
                });
        })
        .catch((err) =>{
            console.error("Cannot connect to MongoDb", err)
        });
});
// The application is to listen on http://localhost:3000
app.listen(3000, function () {
    console.log('The application is available on http://localhost:3000');
});