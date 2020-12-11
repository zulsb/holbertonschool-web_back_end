const taskconst = require('./0-constants.js');

test('Constants', () => {
  expect(taskconst.taskFirst() + ' ' + taskconst.taskNext()).toBe('I prefer const when I can. But sometimes let is okay');
});
