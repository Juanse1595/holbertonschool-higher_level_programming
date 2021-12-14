#!/usr/bin/node
const Squareparent = require('./5-square');

module.exports = class Square extends Squareparent {
  charPrint (c) {
    let block;
    if (!c) {
      block = 'X';
    } else {
      block = c;
    }
    for (let i = 0; i < this.heigth; i++) {
      console.log(block.repeat(this.width));
    }
  }
};
