import * as express from "express";
import {Request, Response, static as expressStatic, urlencoded} from "express";
import 'express-async-errors';
import * as methodOverride from "method-override";
import {engine} from "express-handlebars";

/**
 * Import to create a connection pool to database when we are starting an app
 */
import "./utils/db";
import { clientRouter } from "./routers/client";
import {dealerRouter} from "./routers/dealer";
import {UserRecord} from "./records/client_db";
import {CarRecord} from "./records/car_db";
import helmet from "helmet";

// creating an express app
const app = express();

// methodOverride to use with PATCH PUT etc.
app.use(methodOverride('_method'));

`
Dyrektywa defaultSrc określa zasoby, które mogą być ładowane przez przeglądarkę domyślnie, przez co 'self' oznacza tylko zasoby z tej samej strony.
scriptSrc, styleSrc, imgSrc, fontSrc, connectSrc, objectSrc, workerSrc, frameSrc, frameAncestors, formAction, mediaSrc,
 określa skąd mogą być ładowane odpowiednie zasoby, dla każdej z tych dyrektyw przestawione jest na 'self' co oznacza tylko zasoby z tej samej strony, 
 a 'unsafe-inline' pozwala na używanie skryptów i stylów z linii inline z kodu HTML
`
app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        styleSrc: ["'self'"],
        imgSrc: ["'self'"],
        fontSrc: ["'self'"],
        connectSrc: ["'self'"],
        objectSrc: ["'none'"],
        workerSrc: ["'self'"],
        frameSrc: ["'self'"],
        frameAncestors: ["'self'"],
        formAction: ["'self'"],
        mediaSrc: ["'self'"]
    }
}));


// I will use it cuz we will get our data through forms
app.use(urlencoded({
    extended: true,
}));

// I will be serving static data from dir named 'public'
// app.use(expressStatic("__dir"))
app.use(expressStatic("public"));

// layouts engine - I will use express handlebars
app.engine('.hbs', engine({
    extname: '.hbs',
    //helpers: ???,
}));

// setting my view engine to .hbs
app.set('view engine', '.hbs')

// using clientRouter
app.use('/client', clientRouter);
// using dealerRouter
app.use('/dealer', dealerRouter)

app.get('/', async(req:Request,res:Response):Promise<void> => {
    const users = await UserRecord.listAll()
    const carsToRender = await CarRecord.listAll()
    const log = []
    for (const user of users) {
        let cars = await CarRecord.getOneCar(user.car)
        log.push({
            car: user.car,
            name: user.name,
            brand: cars.brand,
            model: cars.model,
            year: cars.year,
            num: cars.num
        })
    }
    res.render('home',{log})
})



//handling errors
// app.use(handleError)


// app is listening on port 3000 - console log to click every time when I need it - I do not have to copy it ;)
app.listen(3000, 'localhost', () => {
    console.log("Listening on http://localhost:3000");
});



