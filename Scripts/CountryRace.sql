DELETE FROM CountryRaceStats WHERE 1=1;

INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('AUS', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('AUS', '5');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('AUS', '6');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('CAN', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('CAN', '5');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('CAN', '6');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('HKG', '1');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('HKG', '2');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('HKG', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('MYS', '1');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('MYS', '2');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('MYS', '3');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('PHL', '3');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('PHL', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('PHL', '6');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('SGP', '1');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('SGP', '2');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('SGP', '3');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('THA', '1');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('THA', '2');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('THA', '3');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('GBR', '2');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('GBR', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('GBR', '6');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('USA', '4');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('USA', '5');
INSERT INTO CountryRaceStats(countryCode, raceId) VALUES ('USA', '6');

-- COUNT = 26
SELECT COUNT(1) FROM CountryRaceStats;