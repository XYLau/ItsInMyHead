SELECT firstName FROM FirstName LIMIT 10;

-- Name
SELECT f.firstName, l.lastName, f.raceId
FROM FirstName f, LastName l
WHERE f.raceId = l.raceId

-- Name + Gender
SELECT f.firstName, l.lastName, f.raceId, g.genderDesc
FROM FirstName f, LastName l, Gender g
WHERE f.raceId = l.raceId
AND f.gender = g.gender

-- Name + Country
SELECT f.firstName, l.lastName, f.raceId, g.genderDesc
FROM FirstName f, LastName l, Gender g
WHERE f.raceId = l.raceId
AND f.gender = g.gender
