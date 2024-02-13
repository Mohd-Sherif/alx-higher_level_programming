#!/usr/bin/node

const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    const ch = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
}

module.exports = Square;
