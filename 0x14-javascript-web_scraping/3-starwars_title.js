#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const movieId = myArgs[0];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const newBody = JSON.parse(body);
  console.log(newBody.title);
});
