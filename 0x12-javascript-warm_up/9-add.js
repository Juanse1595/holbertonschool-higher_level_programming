#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const firstarg = parseInt(process.argv[2]);
const secondarg = parseInt(process.argv[3]);
add(firstarg, secondarg);
