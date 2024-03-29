#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
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
  const characters = movieData.characters;
  
  // Make requests to fetch character names
  const fetchCharacterNames = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          reject(`Failed to fetch character data. Status code: ${response.statusCode}`);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });
  
  // Wait for all requests to complete
  Promise.all(fetchCharacterNames)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});
