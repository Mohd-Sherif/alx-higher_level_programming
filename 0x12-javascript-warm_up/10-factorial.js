#!/usr/bin/node

const argv = process.argv;

function factorial (a) {
  if (isNaN(a) || a === 0 || a === 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}

console.log(factorial(Number.parseInt(argv[2])));
