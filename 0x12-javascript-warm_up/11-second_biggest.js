#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < argv.length; i++) {
    arr[i] = Number.parseInt(argv[i]);
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
