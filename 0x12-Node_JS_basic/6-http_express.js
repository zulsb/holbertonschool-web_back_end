const express = require('express');

const port = 1245;

const app = express().get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port);

module.exports = app;
