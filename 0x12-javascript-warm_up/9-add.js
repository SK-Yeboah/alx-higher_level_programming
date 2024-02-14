#!/usr/bin/node

function add(a, b){
  return eval(a+b);
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));