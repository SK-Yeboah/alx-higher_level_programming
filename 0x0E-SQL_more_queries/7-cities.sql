-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- create database hbtn_0d_usa if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to specified database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    state_id INT NOT NULL, 
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
    );