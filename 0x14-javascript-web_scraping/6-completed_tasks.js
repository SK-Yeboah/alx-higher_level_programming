#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1); // Exit with error
}

const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if occurred
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  
  const todos = JSON.parse(body);
  
  // Count completed tasks by user ID
  const completedTasksByUser = todos.reduce((completedTasks, todo) => {
    if (todo.completed) {
      completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
    }
    return completedTasks;
  }, {});
  
  console.log(completedTasksByUser); // Print the number of completed tasks by user ID
});
