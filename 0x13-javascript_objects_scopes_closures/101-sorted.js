#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

for (const userId in dict) {
  const occurence = dict[userId];
  if (!sortedDict[occurence]) {
    sortedDict[occurence] = [];
  }
  sortedDict[occurence].push(userId);
}
console.log(sortedDict);
