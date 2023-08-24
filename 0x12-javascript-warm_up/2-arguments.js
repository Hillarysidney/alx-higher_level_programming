#!/usr/bin/node

const { argv } = require('process');
const my_argc = argv.length;

if (my_argc === 2) {
  console.log('No argument');
} else if (my_argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
