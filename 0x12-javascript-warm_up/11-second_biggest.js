#!/usr/bin/node

// Accessing command line arguments using process.argv
const args = process.argv.slice(2); // Exclude 'node' and the script file name

// Check the number of arguments
const numArgs = args.length;

// Check if no arguments are passed or only one argument is passed
if (numArgs === 0 || numArgs === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and sort them in descending order
  const sortedIntegers = args.map(Number).sort((a, b) => b - a);

  // Find the second biggest integer
  const secondBiggest = sortedIntegers[1];

  // Print the result
  console.log(secondBiggest);
}
