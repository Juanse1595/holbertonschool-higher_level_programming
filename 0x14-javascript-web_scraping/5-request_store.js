#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const filePath = myArgs[1];
// Get content from url
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  // Write content to file
  const fs = require('fs');
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
    // File written succesfully
  });
});
