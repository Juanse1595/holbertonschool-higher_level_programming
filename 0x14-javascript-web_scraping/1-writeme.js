#!/usr/bin/node
// myArgs retrieve the passed args, ignoring first 2
const myArgs = process.argv.slice(2);
const filePath = myArgs[0];
const content = myArgs[1];
const fs = require('fs');
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
  // File written succesfully
});
