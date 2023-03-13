#!/usr/bin/node
const argv = require('process').argv;
const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
