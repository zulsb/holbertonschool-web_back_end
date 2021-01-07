process.stdin.setEncoding('utf8');

console.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const yourName = process.stdin.read();
  if (yourName !== null) {
    process.stdout.write(`Your name is: ${yourName}`);
  }
});

process.stdin.on('end', () => {
  console.write('This important software is now closing\n');
});
