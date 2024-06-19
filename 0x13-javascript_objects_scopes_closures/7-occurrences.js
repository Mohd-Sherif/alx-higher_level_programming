#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ctr = 0;
  for (const element of list) {
    if (element === searchElement) {
      ctr++;
    }
  }
  return ctr;
};
