#!/usr/bin/node
const request = require('request');


if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1); // Exit with error
}

const url = process.argv[2];

// Make a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    console.error(error); // Print error if occurred
    return;
  }
  
  console.log(`code: ${response.statusCode}`); // Print the status code
});
