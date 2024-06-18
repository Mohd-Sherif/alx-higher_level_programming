#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = Number.parseInt(argv[2]);
  let row = '';
  for (let i = 0; i < size; i++) {
    row += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
