#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function fetchData(character) {
  return new Promise((resolve, reject) => {
    request(character, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function main() {
  try {
    const response = await new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });
    const data = JSON.parse(response);
    const characters = data.characters;
    for (let i = 0; i < characters.length; i++) {
      const characterName = await fetchData(characters[i]);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
