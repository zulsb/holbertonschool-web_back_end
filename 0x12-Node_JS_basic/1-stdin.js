process.stdin.setEncoding('utf8');
console.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const yourName = process.stdin.read();
  if (yourName !== null) {
    process.stdout.write(`Your name is: ${yourName}`);
  }
});
process.stdin.on('end', () => {
  console.stdout.write('This important software is now closing\n');
});
