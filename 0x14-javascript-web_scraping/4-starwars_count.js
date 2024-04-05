#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  let ctr = 0;
  for (let i = 0; i < data.results.length; i++) {
    const characters = data.results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].endsWith('18/')) {
        ctr++;
      }
    }
  }
  console.log(ctr);
});
