#!/usr/bin/node
const numargs = process.argv.length - 2;
if (numargs === 0) {
  console.log('No argument');
} else if (numargs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
