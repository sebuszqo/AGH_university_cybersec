"use strict";
let {isDirOrFile} = require('../module');
let assert = require('assert');

describe('The isDirOrFile() function', function () {
    it('Returns file for plik.txt', function () {
        assert.strictEqual(isDirOrFile("../zad-2/plik.txt"), "file")
    });
    it('Returns dir for /etc', function () {
        assert.strictEqual(isDirOrFile("/etc"), 'dir')
        // expect(op.sum()).to.equal(0);
    });
    it('Returns file for ./script.js', function () {
        assert.strictEqual(isDirOrFile("./script.js"), 'file')
        // expect(op.sum()).to.equal(0);
    });
    it('Returns dir for /', function () {
        assert.strictEqual(isDirOrFile("/"), 'dir')
        // expect(op.sum()).to.equal(0);
    });
});

// cd zad-2
// npx mocha