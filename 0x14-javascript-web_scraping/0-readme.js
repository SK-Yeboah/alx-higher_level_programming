#!/usr/bin/node
const fs  = require('fs')
const filepath = process.argv[2]


fs.readFile(filepath,'utf-8', (err,data) =>{
    if(err){
        if(err.code === 'ENOENT'){
            console.error(`{Error: ${err.code}: no such  firle or directory} `);
        }else{
            console.error(err)
        }
        
        return
    }
    console.log(data)
});