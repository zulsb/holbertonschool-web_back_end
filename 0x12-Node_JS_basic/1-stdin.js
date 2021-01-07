process.stdin.setEncoding('utf8');
console.log('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const yourname = process.stdin.read();
  if (yourname !== null) {
    process.stdout.write(`Your name is: ${yourname}`);
  }
});
process.stdin.on('end', () => {
  console.log('This important software is now closing\n');
});
