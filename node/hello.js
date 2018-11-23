

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

// Yet abother way to do this. This is pretty much wnat module.exports does
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

    Application_Sync();
    ApplicationAsync_ChainedCB();

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

// Using async/await

// Promises - https://www.datchley.name/es6-promises/

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

function myFunc(callback) {
  // at this point we have the result of the DB query, let's give it to the application
  console.log(" ++ Pho PHO Pho ++ ");
  callback(null, 'Here have some Pho');
  
}

// Simulate a DB query that returns immediately with result available after 1.5 seconds
function dbQuery(something, callback){
    if(callback === undefined){
        console.log("====== No callback so NOOOO soup for you! ======= ");
        return false;
    }

    console.log(" ++ Mamma's going to make some soup for you ++ ");
    // Our psudo DB query
    setTimeout(myFunc, 1500, callback);
    
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

