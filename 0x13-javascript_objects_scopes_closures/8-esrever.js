#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  while (list.length) {
    revList.push(list.pop());
  }
  return revList;
};
