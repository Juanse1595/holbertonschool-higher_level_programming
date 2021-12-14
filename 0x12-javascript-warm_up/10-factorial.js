#!/usr/bin/node
function factorial (num) {
  if (!num) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
const firstarg = parseInt(process.argv[2]);
const result = factorial(firstarg);
console.log(result);
