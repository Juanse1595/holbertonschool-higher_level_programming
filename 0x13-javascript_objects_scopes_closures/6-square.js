#!/usr/bin/node
/** Define Rectangle class */
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let block = 'X';
    if (c) {
      block = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(block.repeat(this.width));
    }
  }
};
