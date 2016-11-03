-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.language IN('Slovene')
-- ORDER BY percentage DESC

-- SELECT countries.name, COUNT(cities.id)
-- FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- GROUP BY countries.id
-- ORDER BY COUNT(cities.id) DESC;

-- SELECT cities.name, cities.population
-- FROM countries
-- LEFT JOIN cities ON countries.id = cities.country_id
-- WHERE countries.name = 'Mexico' AND cities.population > 500000
-- ORDER BY cities.population DESC;

-- SELECT countries.name, languages.language, languages.percentage FROM countries
-- JOIN languages ON countries.id = languages.country_id
-- WHERE languages.percentage > 89.0
-- ORDER BY languages.percentage DESC

-- SELECT name, surface_area, population FROM countries
-- WHERE surface_area < 501 AND population > 100000

-- SELECT name, government_form, capital, life_expectancy FROM countries
-- WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75

-- SELECT countries.name, cities.name, cities.district, cities.population FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- WHERE cities.population > 5000 AND district = 'Buenos Aires'

-- SELECT region, COUNT(countries.id) FROM countries
-- GROUP BY region
-- ORDER BY COUNT(countries.id) DESC