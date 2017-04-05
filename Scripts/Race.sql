DELETE FROM Race WHERE 1=1;

INSERT INTO Race(raceId, raceDesc) VALUES (0, 'Generic');
INSERT INTO Race(raceId, raceDesc) VALUES (1, 'Chinese');
INSERT INTO Race(raceId, raceDesc) VALUES (2, 'Indian');
INSERT INTO Race(raceId, raceDesc) VALUES (3, 'Malay');
INSERT INTO Race(raceId, raceDesc) VALUES (4, 'American');
INSERT INTO Race(raceId, raceDesc) VALUES (5, 'African');
INSERT INTO Race(raceId, raceDesc) VALUES (6, 'French');

-- COUNT = 7
SELECT COUNT(1) FROM Race;
