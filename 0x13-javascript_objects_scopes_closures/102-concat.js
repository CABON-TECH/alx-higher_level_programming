#!/usr/bin/node
const { argv, exit } = require('process');
const fs = require('fs');

if (argv.length < 3) {
  console.log('Usage: ./102-concat [fileA] [fileB] [fileC]');
  exit();
}

const contentA = fs.readFileSync(argv[2], 'utf8', function (err, result) {
  if (err) console.log('error', err);
});
const contentB = fs.readFileSync(argv[3], 'utf8', function (err, result) {
  if (err) console.log('error', err);
});

const contentC = contentA.concat(contentB);

fs.writeFile(argv[4], contentC, 'utf8', function (err, result) {
  if (err) console.log('error', err);
});
