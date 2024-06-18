#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  console.log(a + b);
}

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log(NaN);
} else {
  add(Number.parseInt(argv[2]), Number.parseInt(argv[3]));
}
