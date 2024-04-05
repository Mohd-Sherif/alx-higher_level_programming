#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  const usrTasks = {};
  for (const task of data) {
    if (task.completed) {
      usrTasks[task.userId] = (usrTasks[task.userId] || 0) + 1;
    }
  }
  console.log(usrTasks);
});
