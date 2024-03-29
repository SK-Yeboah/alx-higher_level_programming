#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1); // Exit with error
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if occurred
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  
  // Write the body response to the file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err); // Print error if occurred while writing to file
      return;
    }
    
    console.log(`Data successfully written to ${filePath}`); // Print success message
  });
});
