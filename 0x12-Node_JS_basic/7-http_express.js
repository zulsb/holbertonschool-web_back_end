const express = require('express');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = express().get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((data) => {
      res.end(data);
    })
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(port);

module.exports = app;
