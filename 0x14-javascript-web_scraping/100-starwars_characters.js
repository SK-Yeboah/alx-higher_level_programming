#!/usr/bin/node
const request = require('request');


if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1); 
}

const apiUrl = process.argv[2];


request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); 
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }
  
  const todos = JSON.parse(body);
  
  const completedTasksByUser = todos.reduce((completedTasks, todo) => {
    if (todo.completed) {
      completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
    }
    return completedTasks;
  }, {});
  
  console.log(completedTasksByUser); 
});
