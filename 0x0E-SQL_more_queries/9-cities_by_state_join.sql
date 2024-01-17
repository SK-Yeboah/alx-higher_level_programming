-- Select all cities with associated state names
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON states.id = cities.state_id 
ORDER BY cities.id;