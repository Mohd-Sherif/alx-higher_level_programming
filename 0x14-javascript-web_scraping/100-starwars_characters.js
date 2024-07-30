#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (err, res, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
