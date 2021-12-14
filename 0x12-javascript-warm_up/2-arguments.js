#!/usr/bin/node
let num_args = process.argv.length - 2;
if (num_args === 0) {
    console.log('No argument');
}
else if (num_args === 1) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}