/*
  Mocha allows you to use any assertion library you wish. In this example, we are using the built-in module called 'Assert'.
  If you prefer the 'Chai' library (https://www.chaijs.com/) then you have to install it yourself: 'npm install chai --save-dev',
  and then you need to uncomment the lines below.
*/

//----------------------------------------
// Mocha tests with CommonJS style imports
//----------------------------------------

// var expect = require('chai').expect;
let assert = require('assert');
let module1 = require('../commonJs/module');

describe('The sum() method', function () {
    it('Returns 7 for 5+2', function () {
        let op = new module1.Operation(5, 2);
        assert.strictEqual(op.sum(), 7)
        // expect(op.sum()).to.equal(4);
    });
    it('Returns 0 for -4+4', function () {
        let op = new module1.Operation(-4, 4);
        assert.strictEqual(op.sum(), 0)
        // expect(op.sum()).to.equal(0);
    });
});

// npx mocha gives:
// The sum() method
//     ✔ Returns 7 for 5+2
//     ✔ Returns 0 for -4+4
//
//
//     2 passing (3ms)


//-----------------------------------
// Mocha tests with ES6 style imports
//-----------------------------------

/*
- You must install the 'esm' module (https://www.npmjs.com/package/esm) — npm install esm --save-dev
- You must run tests as follows: npx mocha --require esm
Source: https://stackoverflow.com/questions/57004631/mocha-tests-with-es6-style-imports

import { Operation } from "../module";
import assert from 'assert';

describe('The sum() method', function () {
  it('Returns 4 for 2+2', function () {
    var op = new Operation(2, 2);
    assert.strictEqual(op.sum(), 4)
  });
  it('Returns 0 for -2+2', function () {
    var op = new Operation(-2, 2);
    assert.strictEqual(op.sum(), 0)
  });
});
*/