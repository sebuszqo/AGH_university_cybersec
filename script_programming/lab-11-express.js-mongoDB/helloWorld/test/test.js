//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
const supertest = require("supertest");
const chai = require('chai');
const chaiJson = require('chai-json');

chai.use(chaiJson);
const fs = require('fs');
const path = require("path");
const server = supertest.agent("http://localhost:3000");



// npm run test - to run tests

// UNIT test begin
describe('GET /', () => {
    it('respond with html', (done) =>{
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200, done);
    });
});

describe('GET /', () => {
    it("My first Test",(done)=>{
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200,done)
    })
})

describe("Checking GET /json/example",()=>{
    it('Response',(done)=>{
        server.get('/json/example').expect('Content-Type',/html/).expect(200,done)
    });

    it('Check /json/example route content',function (done){
        server
            .get('/json/example')
            .expect('Content-Type', /html/)
            .expect(async (res)=>{
                chai.expect(res.text, `<table class="table" border="solid 1px black"">
    <thead>
    <tr>
        <th width="60px"> x </th>
        <th width="60px"> Operation </th>
        <th width="60px"> y </th>
        <th width="60px"> Result </th>
    </tr>
    </thead>
    <tbody>
     <tr><td text-align="center"> 4 </td><td text-align="center"> + </td><td text-align="center"> 6 </td><td text-align="center"> 10 </td></tr><tr><td text-align="center"> 11 </td><td text-align="center"> - </td><td text-align="center"> 24 </td><td text-align="center"> -13 </td></tr><tr><td text-align="center"> 15 </td><td text-align="center"> * </td><td text-align="center"> 3 </td><td text-align="center"> 45 </td></tr><tr><td text-align="center"> 21 </td><td text-align="center"> / </td><td text-align="center"> 7 </td><td text-align="center"> 3 </td></tr><tr><td text-align="center"> 21 </td><td text-align="center"> + </td><td text-align="center"> 7 </td><td text-align="center"> 28 </td></tr>
    </tbody>
    </table>
`)}).end(done)
    });
});


describe('Check returning sum /', ()=>{
    it("Check / route content", (done)=>{
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(async (res)=>{
                chai.expect(res.text, '<h1>Summing numbers that were hardcoded inside!</h1><p>1 + 2 = 3</p>')
            }).end(done);
    });
});

describe('Checking JSON file', () => {
    it("Should be a valid JSON file ", () => {
        const file = fs.readFileSync("./data/example.json");
        chai.expect(file).to.be.jsonObj()
    });
    it("Should contain specific properties and values",()=>{
        chai.expect("./data/example.json").to.be.jsonWithProps(
        {
            "o":"+",
            "x": 4,
            "y": 6
        },
        {
            "o":"-",
            "x": 11,
            "y": 24
        },
        {
            "o":"*",
            "x": 15,
            "y": 3
        },
        {
            "o":"/",
            "x": 21,
            "y": 7
        },
        {
            "o":"+",
            "x": 21,
            "y": 7
        }
        );
    });
});


