#!/usr/bin/node
const firstarg = parseInt(process.argv[2]);
if (!firstarg) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstarg; i++) {
    console.log('C is fun');
  }
}
