#!/usr/bin/node
const { argv } = require('process');
const numbss = parseInt(argv[2]);
console.log(Number.isInteger(numbss) ? `My number: ${numbss}` : 'Not a number');
