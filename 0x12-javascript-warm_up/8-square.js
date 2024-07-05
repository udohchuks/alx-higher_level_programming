#!/usr/bin/node
const args = process.argv.slice(2);
const size = Math.floor(Number(args[0]));
if (args.length === 0 || isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
