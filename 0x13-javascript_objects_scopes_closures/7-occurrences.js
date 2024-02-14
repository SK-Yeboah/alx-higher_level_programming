#!/usr/bin/node


export function nbOccurences (list, searchElement) {
  // Counter to keep track of occurrences
  let count = 0;

  // Loop through the list to count occurrences
  for (let element of list) {
      if (element === searchElement) {
          count++;
      }
  }

  // Return the count of occurrences
  return count;
}

