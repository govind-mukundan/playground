

// require() is a special function defined in Node which is useful for module encapsulation
// https://nodejs.org/api/modules.html#modules_modules
// https://nodejs.org/api/modules.html#modules_the_module_wrapper
const http = require('http'); // This loads the core HTTPS module 

console.log("Hello World");

const { PI } = Math;


// ###### EXPORTING - module.exports ##########

// - requuire() makes everything not specifically exported private to this module by encapsulating the module inside a function()
// - require() defines an alias called exports that initially points to module.exports for convenience
// - The RETURN value of require() is the module.exports of the module you "required"
exports = module.exports   // Implicitly part of require()

// You can export functions or variables or whatever, as long as they are bound to the module.exports object / dictionary
exports.funGovind = () => console.log("Govind for export");

// Another way to do this is to directly insert all elements you want to export into module.exports
module.exports = {
    
    funGovind : function () {
        console.log("Govind for export");
    },
    
    funMukundan : function (){
        console.log("Mukundan for export");
    },
    
    boringConstant : 42
}

// Yet abother way to do this. This is pretty much what module.exports does
module.exports = function(){
    
    // None of these are exported by default
    function _funGovind () {
        console.log("Govind for export");
    }
    
    function _funMukundan (){
        console.log("Mukundan for export");
    }
    
    boringConstant = 42
    myPrivateStuff = 103
    
    
    return {
        funGovind : _funGovind,
        funMukundan : _funMukundan,
        coolConstant : boringConstant
        
    }
    
}


// Just like __main__ in python
// === is necessary for equality of type + value, == does automatic type coersion
if(require.main === module){
    // This shows you something like this:     
    console.log(require.main);
    
    // Note how you cannot call funGovind() directly
    exports.funGovind();

    SimulationResult = false; // Flag to control the simulation result, true to test the +ve flow, false for error path
    Application_Sync();
    //ApplicationAsync_ChainedCB();
    ApplicationAsync_Promise();
    //ApplicationAsync_async();

}


// ################## CALLBACKS ####################
/* - All user code runs inside a single threaded callback+event loop managed by Node library.
   - Every node library that does any slow process is expected to provide a callback interface
   - These callbacks have a standard signature of callback(error, result); error is NULL if result is not and vice versa
   - Callbacks are used for actvities started from user application. Events are available for "native space" triggered activities
*/
// For illustration we will use the case of (1) Database Query (2) Execute actions based on result

var query = 'FROM Vietnam SELECT * Food WHERE Food.Composition LIKE Soup'

// Synchronous way - not supported in Node. In a Node library, dbQuery() will return immediately without the result

function CheckSomethingInDB_Sync (query){
	if(dbQuery(query) == true){
		SomePrivateWork();
		return true
	}
	else{
		SomeOtherPrivateWork();
		return false
	}
}

function Application_Sync (){
    console.log("==== Trying a Synchronous blocking operation ====\n");

	if (CheckSomethingInDB_Sync(query) == true )
		Action();
	else
        ErrorAction();
    
    console.log("===================================================\n");
}

// Default asynchronous way using chained callbacks => fugly. 
// more: http://callbackhell.com/

function CheckSomethingInDB_ChainedCB (query, application_cb){
	dbQuery(query, 
        function PrivateWorkCBHandler(error, result){
            if(error){
                SomeOtherPrivateWork();
                application_cb(error, null);
            }
            else {
                SomePrivateWork(result);
                application_cb(null, result);
            }
        }
	);
}

function ApplicationAsync_ChainedCB (){
    console.log("==== Trying Asynchronous Chained Callbacks ====\n");
    CheckSomethingInDB_ChainedCB(query, 
        function (error, result){
            if (result)
                Action(result);
            else
                ErrorAction(error);
            // Notice how the end banner is inside the calback and in the main function
            console.log("===================================================\n");
        }
    )
}

// Promises - https://www.datchley.name/es6-promises/
/* 
    The input to a Promise() is the "operation" function or the "long running task". The signature of this task is 
   predefined to take two other functions as parameters - called the "resolve" and "reject" functions
   i.e. Promise(function Task(resolve, reject)) and we expect the Task to do the following:
   function Task(resolve, reject){
       // Wrap the normal Node IO operation within a Task(resolve, reject) structure
       do_normal_node_async_io(options, function cb(err, result){
        if(err) reject(err)
        if(result) resolve(result)
       }
   }

   p = new Promise(Task);

   Note that at this point the actual "resolve" and "reject" functions are not defined yet, but you still have a Promise that can be passed around
   but *not* resolved or rejected. Q: Will the do_stuff() be executed in the background and control wait for the resolution/rejection ??
   To consume the promise, you have to attach a resolve and reject handler to the .then() and .catch() methods of the Promise object
   p.then(on_success(val)).catch(on_failure(val))

   => It's better to use a single catch statement while chaining promises

   A neater way to write this is to have a function that RETURNS the promise

   function PTask(){
       return new Promise(function Task(resolve, reject){
            do_normal_node_async_io(options, function cb(err, result){
                if(err) reject(err)
                if(result) resolve(result)
            }
        } );
   }
*/
// Wrap the DB query inside a promise, and include any application unaware business logic inside
function CheckSomethingInDB_Promise (query){
    return new Promise(function (resolve, reject){
        dbQuery(query, 
            function PrivateWorkCBHandler(error, result){
                if(error){
                    SomeOtherPrivateWork();
                    reject(error);
                }
                else {
                    SomePrivateWork(result);
                    resolve(result);
                }
            }
        )}
    );
}

function ApplicationAsync_Promise (){
    console.log("==== Trying Promises ====\n");
    /* Notice how you use then() to chain promises and print out the termination string
      ==> An error in the first then() will cause the *first* catch [ErrorAction()] to be invoked followed by the next then()
    */
    CheckSomethingInDB_Promise().then(Action).then( _ => console.log("===================================================\n"))
    .catch(ErrorAction).then( _ => console.log("++++++++++++++++++++++++++++++++++++++++++++++\n"));
}

// Using async/await: https://javascript.info/async-await
async function ApplicationAsync_async (){
    console.log("==== Trying async/await ====\n");
    /* Note the use of try/catch. 
       ==> Promise.reject() will **automatically** result in an EXCEPTION being thrown at the await condition.
       ==> So we can keep the flow pseudo synchronous
    */
    try{
        result = await CheckSomethingInDB_Promise();
        Action(result);
        console.log("===================================================\n");
    } catch(err){
        ErrorAction(err);
        console.log("+++++++++++++++++++++++++++++++++++++++++++++++++++\n");
    }
}

// time-series / parallel

// --------- Simulation Code START ------------------------
function SomePrivateWork(){
    console.log("Done with our private work");
}

function SomeOtherPrivateWork(){
    console.log("Done with our other private work");
}

function Action(result){
    console.log(`Lets do our %% SUCCESS %% action = ${result}`);
}

function ErrorAction(error){
    console.log(`Lets do our !! ERROR !! action = ${error}`);
}

function makeSoup(callback) {
  // at this point we have the result of the DB query, let's give it to the application
  console.log(" ++ Pho PHO Pho ++ ");
  // Success
  //callback(null, 'Here have some Pho');
  // Error
  callback("Not enough beef", null);
  
}

// Simulate a DB query that returns immediately with result available after 1.5 seconds
function dbQuery(something, callback){
    if(callback === undefined){
        console.log("====== No callback so NOOOO soup for you! ======= ");
        return false;
    }

    console.log(" ++ Mamma's going to make some soup for you ++ ");
    // Our psudo DB query
    setTimeout(makeSoup, 1500, callback);
    
    return true;
    
}
// --------- Simulation Code END ------------------------


callback = function(response) {
  var str = ''
  response.on('data', function(chunk){
    str += chunk
  })

  response.on('end', function(){
    console.log(str)
  })
}

// Dictionaries
// In JS all objects are dictionaries and ALL keys in dictionaries are STRINGS
var testObj = {a: 28, b: 82, c: "hello", d: 983, e: 'lara', o: "key", f: '82828', g: 8};
Object.keys(testObj)
// [ 'a', 'b', 'c', 'd', 'e', 'o', 'f', 'g' ]

// Difference between x[key] and x.key (not always the same) ??
// delete optOutList.topics.state.objects[objects[i]]; != delete optOutList.topics.state.objects.objects[i];


// Benchmarking JS
// http://jsben.ch/WqlIl
// https://www.typescriptlang.org/docs/handbook/declaration-files/deep-dive.html

var body = JSON.stringify({ "version": "1",
"region": "us-east-1",
"userPoolId": "us-east-1_dhBFHegeY",
"userName": "govind@brtchip.com",
"callerContext": { "awsSdkVersion": "aws-sdk-unknown-unknown", "clientId": null },
"triggerSource": "PostConfirmation_ConfirmSignUp",
"request": 
{ "userAttributes": 
{ "sub": "a0f50086-a53e-4179-a748-0796e6ecf3e7",
"cognito:user_status": "CONFIRMED",
"email_verified": "false",
"email": "govind@brtchip.com" } },
"response": {} });
// http.request(options, callback).end(body);

