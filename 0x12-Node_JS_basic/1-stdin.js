process.stdin.setEncoding('utf8');
console.log('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const n = process.stdin.read();
  if (n !== null) {
    process.stdout.write(`Your name is: ${n}`);
  }
});
process.stdin.on('end', () => {
  console.log('This important software is now closing\n');
});
