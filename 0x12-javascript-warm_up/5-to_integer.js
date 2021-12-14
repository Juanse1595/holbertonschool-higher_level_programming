#!/usr/bin/node
const myargnum = parseInt(process.argv[2]);
if (!myargnum) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myargnum);
}
