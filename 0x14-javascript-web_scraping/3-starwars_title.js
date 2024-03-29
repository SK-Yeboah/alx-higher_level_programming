#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie_ID>');
  process.exit(1); // Exit with error
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if occurred
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  
  const movieData = JSON.parse(body);
  console.log(movieData.title); // Print the title of the movie
});
