const things = require('./module.js');

// sliceing to take only 2 last arguments cuz our numbers that we gave in terminal have positions args[2] args[3]
const args = process.argv.slice(-2)


const operation = new things.Operation(args[0], args[1]);

// node index "43" 3
console.log(operation.sum())

// node module.js 112 1008


// npx mocha