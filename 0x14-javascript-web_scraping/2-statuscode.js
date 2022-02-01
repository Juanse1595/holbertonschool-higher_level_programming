#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ', response.statusCode);
});
