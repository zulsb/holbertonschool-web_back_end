const fs = require('fs');

module.exports = function countStudents(path) {
  let s = [];

  try {
    s = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  } catch (err) {
    throw Error('Cannot load the database');
  }
  s = s.split('\n');
  const headers = s.shift().split(',');

  const groups = {};
  const studentsObjects = [];

  s.forEach((student) => {
    if (student) {
      const info = student.split(',');
      const studentObject = {};

      headers.forEach((header, index) => {
        studentObject[header] = info[index];
        if (header === 'field') {
          if (groups[info[index]]) {
            groups[info[index]].push(studentObject.firstname);
          } else {
            groups[info[index]] = [studentObject.firstname];
          }
        }
      });
      studentsObjects.push(studentObject);
    }
  });

  console.log(`Number of students: ${studentsObjects.length}`);

  for (const info in groups) {
    if (groups[info]) {
      const listStudents = groups[info];
      console.log(`Number of students in ${info}: ${listStudents.length}. List: ${listStudents.join(', ')}`);
    }
  }
};
