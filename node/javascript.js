

/* let vs var */
// let has block scope -> i.e. you cannot redefine the variable within the block {} that it was declared
// var [deprecated] has *function* or *global* scope depending on whether it is declared inside a function or outside, and imposes no restrictions on redefinitions

var x = 4
var x = 5 // OK

{
    let y = 4
    let y = 5 //NOK
}


/* 7 DEADLY DATA TYPES */
function myfunc() {

}

console.log('There are 7 data types, and "function" is not one of them')
console.log(typeof undefined) // "undefined"

console.log(typeof 0) // "number". To convert to Number -> Number(value)

console.log(typeof true) // "boolean". To convert to Boolean -> Boolean(value)

console.log(typeof "foo") // "string". To convert to String -> String(value)

console.log(typeof Symbol("id")) // "symbol"

console.log(typeof Math) // "object"  (1)

console.log(typeof null) // "object"  --> This is wrong, but retained for back compat

console.log(typeof myfunc) // "function" --> This is also technically wrong as functions are objects, but useful in practise


/* Objects  */
// Objects are dictionaries
// Create:
var o = {}  // Literal syntax
var o = Object() // constructor syntax

// Properties
o.p1 = 4     // same as o["p1"]
o.p2 = 5     // o["p2"]
delete o.pi
// Properties may be computed on the fly [Note how the nuber is auto converted into a string]
o[5 + 4] = 9
// __proto__ is a special property that is used to implement inheritance
console.log("Object = %o, __proto__= %o", o, Object.getPrototypeOf(o))
console.log(9 in o)  // check membership

// Iterate over the keys
for (let key in o) console.log(key)

// Recusive cloning of objects is not supported in JS by default, you have to use the _.cloneDeep() API from lodash
// https://lodash.com/docs/4.17.11#cloneDeep
// Single level cloning can be done using Object.assign(dest, src1, src2, ..)

// Constructors
/* In JS *any* function called with the 'new' keyword is used as a constructor. The convention is to have them named with a capital letter.
 * Constructor functions perform two implicit operations - (1) Create an empty "this" object and (2) return the "this" object
 * It is assumed that the code in the function between steps 1 and 2 will have added some properties to the "this" object
 * */

function SomeConstructor(x) {
    // this = {}   --> calling with new does this

    this.X = x;
    this.name = "govind"

    // return (this)  --> and this
}

var o = new SomeConstructor(4)
console.log(o)

// http://dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition/
// .prototype property
/* All functions have a special property called .prototype, this is in addition to __proto__ available for all objects
 * The .protptype property in turn contains a .constructor property that references the function that created this object
 * i.e. my_obj.prototype.constructor -> SomeConstructor
 * 
 * This behavior is available to support classes. Previously many of these steps had to be done namually, now a days you can do it with the "Class" keyword
 */

/* Classes */
// Classes can be created using the Class keyword or by "low-level" manipulation of the .prototype property

// Old way
function User(name) {
    this.name = name;
}

User.prototype.sayHi = function () {
    alert(this.name);
}

let user = new User("John");
user.sayHi();

// New way - you use the Class keyword + a "constructor" function that is used for the .property.constructor funda under the hood
class User {
    constructor(name) {
        this.name = name;
    }

    sayHi() {
        alert(this.name);
    }
}

let user = new User("John");
user.sayHi();















/* Symbols */

