#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  let ctr = 0;
  for (const movie of data.results) {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      ctr++;
    }
  }
  console.log(ctr);
});
