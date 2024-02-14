#!/usr/bin/node

const { dict } = require('./101-data');

// Function to compute a dictionary of user ids by occurrence
function computeUserIdsByOccurrence(inputDict) {
    let userIdsByOccurrence = {};

    for (let userId in inputDict) {
        let occurrences = inputDict[userId];
        
        if (!userIdsByOccurrence[occurrences]) {
            userIdsByOccurrence[occurrences] = [];
        }
        
        userIdsByOccurrence[occurrences].push(userId);
    }

    return userIdsByOccurrence;
}

// Compute the dictionary of user ids by occurrence
const userIdsByOccurrence = computeUserIdsByOccurrence(dict);

// Print the new dictionary
console.log(userIdsByOccurrence);
