#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || isNaN(Number(args[0]))) {
  console.log('Missing number of occurrences');
} else if (Number(args[0]) > 0) {
  for (let i = 0; i < Math.floor(Number(args[0])); i++) {
    console.log('C is fun');
  }
}
