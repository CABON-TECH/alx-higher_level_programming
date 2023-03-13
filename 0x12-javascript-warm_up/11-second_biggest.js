#!/usr/bin/node
const argv = require('process').argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  //    Convert all the args to numbers and store in a new array
  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    arr[i - 2] = Number(argv[i]);
  }
  //    Sort the array in descending order
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] < arr[j + 1]) {
        const tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
    }
  }
  console.log(arr[1]);
}
