#!/usr/bin/node
const argv = require('process').argv;
const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let square = 'X';
  for (let i = 1; i < num; i++) {
    square = square + 'X';
  }
  for (let j = 0; j < num; j++) {
    console.log(square);
  }
}
