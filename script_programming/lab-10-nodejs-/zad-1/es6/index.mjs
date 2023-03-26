import { Operation } from './module.mjs';

let op = new Operation(3, '5');
console.log(op.sum())

// node index.mjs

//
// Due to the synchronous nature of require(), it is not possible to use it to load ECMAScript module files. Attempting to do so will throw a ERR_REQUIRE_ESM error. Use import() instead.
//
//The .mjs extension is reserved for ECMAScript Modules which cannot be loaded via require(). See Determining module system section for more info regarding which files are parsed as ECMAScript modules.