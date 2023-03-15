#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    let row;
    if (c === undefined) {
      row = 'X';

      for (let i = 1; i < this.width; i++) {
        row = row + 'X';
      }
    } else {
      row = c;
      for (let i = 1; i < this.width; i++) {
        row = row + c;
      }
    }

    // Print the square
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
