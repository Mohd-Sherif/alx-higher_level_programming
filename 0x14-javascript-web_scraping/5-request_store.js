#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, res, body) => {
  if (err) throw err;
  fs.writeFile(filename, body, (err) => {
    if (err) throw err;
  });
});
