#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const request = require('request');
// Object with results
const result = {};
// Get list of user from url
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const listTasksObjs = JSON.parse(body);
  // Create result object with users with at least one completed
  listTasksObjs.forEach((task) => {
    if (task.completed === true) {
      result[task.userId] = 0;
    }
  });
  // Fill in result object
  listTasksObjs.forEach((task) => {
    if (task.completed === true) {
      result[task.userId]++;
    }
  });
  console.log(result);
});
