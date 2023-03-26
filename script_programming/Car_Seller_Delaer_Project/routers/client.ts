import {Request, Response, Router} from "express";
import {UserRecord} from "../records/client_db";
import {CarRecord} from "../records/car_db";
import {type} from "os";
import {log} from "util";

// making a 'arena' router
export const clientRouter = Router();

clientRouter
    // form to make a fight
    .get('/', async (req:Request, res:Response) => {
        const users = await UserRecord.listAll()
        const carsToRender = await CarRecord.listAll()
        const array = []
        for (const user of users) {
            let cars = await CarRecord.getOneCar(user.car)
            array.push({
                car: user.car,
                name: user.name,
                brand: cars.brand,
                model: cars.model,
                year: cars.year,
                num: cars.num
            })
        }
        res.render("client", {array, carsToRender})
    })
    // post to start a fight

    .post('/return', async (req:Request, res:Response): Promise<void> => {
        const {returnId} = req.body
        const name = returnId.split(",")[1]
        const id = returnId.split(",")[0]
        const car = await CarRecord.getOneCar(`${id}`)
        await car.incNum()
        await UserRecord.deleteOne(id,name)
        res.redirect('/client')
    })
    .post('/rent', async (req:Request, res:Response) :Promise<void> => {
        // const {rentId} = req.body
        const {rentId, name}= req.body
        const user = new UserRecord({"name":name, "car":rentId})
        await user.insert()
        const car = await CarRecord.getOneCar(rentId)
        await car.decNum()
        res.redirect('/client')
    })
