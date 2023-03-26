import {createPool} from "mysql2/promise";

export const db = createPool({
    host: 'localhost',
    user: 'root',
    database: 'Skryptowe-Lab12',
    decimalNumbers: true,
    namedPlaceholders: true,
});