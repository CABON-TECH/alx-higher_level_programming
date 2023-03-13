#!/usr/bin/node
const argv = require('process').argv;

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

const num = Number(argv[2]);
console.log(factorial(num));
