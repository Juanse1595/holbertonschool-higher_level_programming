#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const request = require('request');
request.get(url).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
