// "use strict";
// let expect = chai.expect;
//
// function sum(x,y) {
//     return x+y;
// }
//
// describe('The sum() function', function() {
//     it('Returns 4 for 2+2', function() {
//         expect(sum(2,2)).to.equal(4);
//     });
//     it('Returns 0 for -2+2', function() {
//         expect(sum(-2,2)).to.equal(0);
//     });
//     it('Returns 6 for 2+2', function() {
//         expect(sum(3,3)).to.equal(6);
//     });
// });

// let arrToSum = []
const addDigits = (string) => {
    let arr = string.split("")
    return arr.filter(char => Boolean(Number(char))).reduce((prev, curr)=> Number(prev) + Number(curr), 0)
}

const countLetters = (string) =>{
    const arr = string.split("")
    return arr.filter(item => isNaN(item)).length
    // console.log(arr)
}

let sum = 0
const addAllNumbers = (string) =>{
    let arr = string.split("");
    console.log('suma:',sum)
    return (!isNaN(arr[0]) ? sum += Number(arr.filter(char => !isNaN(char)).join("")) : sum )

    // if (Number(arr[0])){
    //     arr = arr.filter(char => Boolean(Number(char)))
    //     return sum += Number(arr.join(""))
    // }
    // return sum
}


"use strict";

let expect = chai.expect;
describe("The addDigits() function", function () {
    it("Returns 3 for 111", function () {
        expect(addDigits("111")).to.equal(3);
    });
    it("Returns 0 for aa", function () {
        expect(addDigits("aa")).to.equal(0);
    });
    it("Returns 2 for aa11", function () {
        expect(addDigits("aa11")).to.equal(2);
    });
    it("Returns 2 for 20aab", function () {
        expect(addDigits("20aab")).to.equal(2);
    });
    it("Returns 0 for ''", function () {
        expect(addDigits("")).to.equal(0);
    });
});

describe("The countLetters() function", function () {
    it("Returns 0 for 111", function () {
        expect(countLetters("111")).to.equal(0);
    });
    it("Returns 2 for aa", function () {
        expect(countLetters("aa")).to.equal(2);
    });
    it("Returns 2 for aa11", function () {
        expect(countLetters("aa11")).to.equal(2);
    });
    it("Returns 3 for 20aab", function () {
        expect(countLetters("20aab")).to.equal(3);
    });
    it("Returns 0 for ''", function () {
        expect(countLetters("")).to.equal(0);
    });
});

describe("The addAllNumbers() function", function () {
    it("Returns 111 for 111", function () {
        expect(addAllNumbers("111")).to.equal(111);
    });
    it("Returns 111 for aa", function () {
        expect(addAllNumbers("aa")).to.equal(111);
    });
    it("Returns 111 for aa11", function () {
        expect(addAllNumbers("aa11")).to.equal(111);
    });
    it("Returns 131 for 20aab", function () {
        expect(addAllNumbers("20aab")).to.equal(131);
    });
    it("Returns 131 for ''", function () {
        expect(addAllNumbers("")).to.equal(131);
    });
});
