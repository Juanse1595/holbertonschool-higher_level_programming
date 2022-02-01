#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const url = myArgs[0];

const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const newBody = JSON.parse(body);
  const filmObjs = newBody.results;
  let count = 0;
  filmObjs.forEach((film) => {
    film.characters.forEach((character) => {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    });
  });
  console.log(count);
});
