#!/usr/bin/node
const argument = process.argv[2];
const x = parseInt(argument);
if(!isNaN(x)){
    console.log("Missing number of occurance");
}else{
    for(let i = 0; i< x; i++){
        console.log("C is fun");
    }
}