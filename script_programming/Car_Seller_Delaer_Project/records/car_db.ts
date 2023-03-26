import {db} from "../utils/db";
import {v4 as uuid} from "uuid";
import {FieldPacket} from "mysql2";
import {ValidationError} from "../utils/errror";

type CarRecordResults = [CarRecord[], FieldPacket[]]

export class CarRecord {
    public id?: string;
    public readonly brand: string;
    public readonly model: string;
    public readonly year: number;
    public num: number;

    constructor(obj: Omit<CarRecord, 'insert' | 'updateNum' | 'deleteOne' | 'decNum' | 'incNum'>) {
        const {id,model,brand, year, num} = obj;

        if (brand.length < 2 || brand.length > 50) {
            throw new ValidationError(`brand should count from 3 to 50 characters. Currently your brand counts: ${brand.length}`)
        }
        if (model.length < 2 || model.length > 50) {
            throw new ValidationError(`model should count from 3 to 50 characters. Currently your brand counts: ${model.length}`)
        }
        // validation if my object has id if not then I am creating new uuid for him
        this.id = id ?? uuid();
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.num = num
    }

    static async getOneCar(id: string): Promise<CarRecord | null> {
        const [results] = await db.execute("SELECT * FROM `Car` WHERE `id` = :id", {
            id,
        }) as CarRecordResults;
        return results.length === 0 ? null : new CarRecord(results[0]);
    }

    async insert(): Promise<string> {
        await db.execute("INSERT INTO `Car` (`id`, `model`, `brand`, `year`, `num`) VALUES(:id ,:model ,:brand ,:year, :num )", {
            id: this.id,
            brand: this.brand,
            model: this.model,
            year: this.year,
            num: this.num
        });

        return this.id;
    }

    async deleteOne(): Promise<void>{
        await db.execute("DELETE FROM `Car` WHERE id = :id",{
            id: this.id
        })
    }

    static async listAll(): Promise<CarRecord[]> {
        const [results] = await db.execute("SELECT * FROM `Car`") as CarRecordResults;
        return results.map(obj => new CarRecord(obj))
    }

    async decNum(): Promise<void> {
        await db.execute("UPDATE `Car` SET `num` = :num WHERE id = :id", {
            id: this.id,
            num: this.num - 1
        })
    }
    async incNum(): Promise<void>{
        await db.execute("UPDATE `Car` SET `num` = :num WHERE id = :id", {
            id: this.id,
            num: this.num + 1
        })
    }
}