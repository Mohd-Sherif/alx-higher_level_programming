#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  console.log('code:', res.statusCode);
});
