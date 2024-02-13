#!/usr/bin/node

function add(a, b){
  return eval(a+b);
}
const first = process.argv[2]
const second = process.argv[3]

if(!isNaN(first) && !isNaN(second)){
    console.log(add(first, second))
}else{
  console.log("Invalid input, Please enter two numbers")
}
