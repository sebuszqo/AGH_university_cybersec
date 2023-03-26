/** Class Operation made for laboratory exercises */
exports.Operation = class {
    /**
     * Constructor. Represents two values. Could be either string or number.
     * @constructor
     * @param {int} x - first number
     * @param {int} y - second number
     */
    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    /**
     * Sum x and y. Either x and y can be string because sum() makes them numbers.
     * @function
     * @param {none}
     * @returns int
     */
    sum(){
        return parseInt(this.x) + parseInt(this.y);
    }
}
// cd zad-1/
// npx mocha