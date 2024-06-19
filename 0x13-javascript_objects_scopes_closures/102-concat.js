#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');

fs.readFile(argv[0], (err, data1) => {
  if (err) {
    return console.error(err);
  }
  fs.readFile(argv[1], (err, data2) => {
    if (err) {
      return console.error(err);
    }
    const buffer = data1 + data2;
    fs.writeFile(argv[2], buffer, (err) => {
      if (err) {
        return console.error(err);
      }
    });
  });
});
