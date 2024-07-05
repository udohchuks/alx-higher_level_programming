#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
    console.log('Not a number');
} else if (isNaN(Number(args[0]))) {
    console.log('Not a number');
} else {
    console.log('My number: ', Math.floor(Number(args[0])));
}
