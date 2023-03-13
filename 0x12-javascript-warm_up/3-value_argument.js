#!/usr/bin/node

const argv = require('process').argv;

if (!argv[2]) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
