#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1); // Exit with error
}

const apiUrl = process.argv[2];

// Make a GET request to the provided Star Wars API endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if occurred
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  
  const filmsData = JSON.parse(body).results;
  
  // Filter films where "Wedge Antilles" character is present
  const filmsWithWedge = filmsData.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  
  console.log(filmsWithWedge.length); // Print the number of movies with Wedge Antilles
});
