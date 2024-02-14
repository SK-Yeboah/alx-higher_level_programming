#!/usr/bin/node


let count = 0; 

export function logMe (item) {
    // Print the number of arguments already printed and the current argument value
    console.log(`${count}: ${item}`);

    // Increment the count of printed arguments
    count++;
}
