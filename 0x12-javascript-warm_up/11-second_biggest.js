#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2);
let count = 0;
let finalArray = [];

if (args.length > 1) {
  finalArray = [...new Set(args.map((e) => parseInt(e)).sort((a, b) => b - a))];
  count = finalArray.length > 1 ? finalArray[1] : finalArray[0];
}

console.log(count);
