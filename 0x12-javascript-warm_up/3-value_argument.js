#!/usr/bin/node
const { argv } = require('process');
let n = 0;

argv.forEach(() => n++);

console.log(n === 2 ? 'No argument' : argv[2]);
