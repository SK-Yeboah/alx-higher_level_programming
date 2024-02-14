#!/usr/bin/node

import { readFile, writeFile } from 'fs';

// Extract command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read content from the first source file
readFile(sourceFilePath1, 'utf8', (err, data1) => {
    if (err) {
        console.log(`Error reading file ${sourceFilePath1}: ${err.message}`);
        return;
    }

    // Read content from the second source file
    readFile(sourceFilePath2, 'utf8', (err, data2) => {
        if (err) {
            console.log(`Error reading file ${sourceFilePath2}: ${err.message}`);
            return;
        }

        // Concatenate the content of both files
        const concatenatedContent = data1 + data2;

        // Write the concatenated content to the destination file
        writeFile(destinationFilePath, concatenatedContent, 'utf8', (err) => {
            if (err) {
                console.log(`Error writing to file ${destinationFilePath}: ${err.message}`);
                return;
            }

            console.log(`Files ${sourceFilePath1} and ${sourceFilePath2} concatenated successfully to ${destinationFilePath}.`);
        });
    });
});
