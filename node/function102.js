

// let is local in scope, var is global


if(require.main === module){
 
}

let f = function (a, b, c, d) {
    console.log("Got (%o, %o, %o, %o)", a, b, c, d);
}

let f1 = function (...rest) {
    console.log("Got (%o)", rest);
}

let f2 = function (a, b, c, d, ...rest) {
    console.log("Got (%o)", rest);
}

// Rest Parameters and Spread Operator

// Spread operator ... allows you to pass an array of arguments to a function
let a = [1,2,3,4,5,6]
> f(...a)        
//Got (1, 2, 3, 4)

// When used inside a function signature, it allows you to receive an array of arguments as input
> f1(...a)
// Got ([ 1, 2, 3, 4, 5, 6, [length]: 6 ]) --> Got a 1D array of all elements

> f1(a, a, a)
// Got ((3) [Array(6), Array(6), Array(6)])  --> Got a 2D array of arrays

> f2(...a)
// Got ((2) [5, 6])  --> the remaining two elements are available in "rest"
