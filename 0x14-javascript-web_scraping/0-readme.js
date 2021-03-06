#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.readFile(myArgs[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
