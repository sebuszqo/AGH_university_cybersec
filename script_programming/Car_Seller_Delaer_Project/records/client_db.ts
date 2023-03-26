
import {db} from "../utils/db";
import {v4 as uuid} from "uuid";
import {FieldPacket} from "mysql2";
import {ValidationError} from "../utils/errror";

type UserRecordResults = [UserRecord[], FieldPacket[]]

export class UserRecord {
    public id?: string;
    public readonly name: string;
    public readonly car?: string;

    constructor(obj: Omit<UserRecord, 'insert'|'updateNum' | 'deleteOne'>) {
        const {id, name, car} = obj;

        if (name.length < 2 || name.length > 50) {
            throw new ValidationError(`Name should count from 3 to 50 characters. Currently your brand counts: ${name.length}`)
        }


        // validation if my object has id if not then I am creating new uuid for him
        this.id = id ?? uuid();
        this.name = name;
        // same thing as with 'id' with wins if there is no 'carID' I am setting wins to '' (default)
        this.car = car ?? '';
    }
    static async getOneUser(id: string): Promise<UserRecord | null> {
        const [results] = await db.execute("SELECT * FROM `User` WHERE `id` = :id", {
            id,
        }) as UserRecordResults;
        return results.length === 0 ? null : new UserRecord(results[0]);
    }
    async insert(): Promise<string> {
        await db.execute("INSERT INTO `User` (`id`, `name`, `car`) VALUES(:id ,:name ,:car)", {
            id: this.id,
            name: this.name.replace(/^\w/, c => c.toUpperCase()),
            car: this.car
        });
        return this.id;
    }

    static async listAll(): Promise<UserRecord[]> {
        const [results] = await db.execute("SELECT * FROM `User`") as UserRecordResults;
        // mapping array of object to create Users as Objects of UserRecord
        return results.map(obj => new UserRecord(obj))
    }

    static async deleteOne(id:string, name:string): Promise<void>{
        await db.execute("DELETE FROM `User` WHERE car = :car AND name =:name",{
            car: id,
            name: name,
        });

    }
}