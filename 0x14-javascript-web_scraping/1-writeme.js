#!/usr/bin/node
const fs = require('fs');


if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> "<string_to_write>"');
  process.exit(1); // Exit with error
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];


fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err); 
    return;
  }
  
 
});
