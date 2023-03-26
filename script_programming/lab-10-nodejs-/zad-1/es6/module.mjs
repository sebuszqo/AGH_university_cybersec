class Operation{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    sum(){
        return parseInt(this.x) + parseInt(this.y);
    }
}

//
// const first = new Operation(2,3)
// console.log(first.sum())
    // ReferenceError: Cannot access 'Operation' before initialization



export { Operation }