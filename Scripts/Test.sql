-- COUNTRY
DELETE FROM "Country" WHERE 1=1;
INSERT INTO "Country" VALUES ('AUS', 'Australia');
INSERT INTO "Country" VALUES ('CAN', 'Canada');
INSERT INTO "Country" VALUES ('HKG', 'Hong Kong');
INSERT INTO "Country" VALUES ('IDN', 'Indonesia');
INSERT INTO "Country" VALUES ('MYS', 'Malaysia');
INSERT INTO "Country" VALUES ('PHL', 'Philippines');
INSERT INTO "Country" VALUES ('SGP', 'Singapore');
INSERT INTO "Country" VALUES ('THA', 'Thailand');
INSERT INTO "Country" VALUES ('GBR', 'United Kingdom');
INSERT INTO "Country" VALUES ('USA', 'United States');
-- RACE
DELETE FROM "Race" WHERE 1=1;
INSERT INTO "Race" VALUES (0, 'Generic');
INSERT INTO "Race" VALUES (1, 'Chinese');
INSERT INTO "Race" VALUES (2, 'Indian');
INSERT INTO "Race" VALUES (3, 'Malay');
INSERT INTO "Race" VALUES (4, 'American');
INSERT INTO "Race" VALUES (5, 'African');
INSERT INTO "Race" VALUES (6, 'French');
-- COUNTRYRACE
DELETE FROM "CountryRace" WHERE 1=1;

-- FIRSTNAME
DELETE FROM "FirstName" WHERE 1=1;
INSERT INTO "FirstName" VALUES (1, 'Roger', 'M', 0);
INSERT INTO "FirstName" VALUES (2, 'Rebecca', 'F', 0);
INSERT INTO "FirstName" VALUES (3, 'Linda', 'F', 0);
INSERT INTO "FirstName" VALUES (4, 'Philip', 'M', 0);
INSERT INTO "FirstName" VALUES (5, 'An', 'M', 1);
INSERT INTO "FirstName" VALUES (6, 'Bing', 'M', 1);
INSERT INTO "FirstName" VALUES (7, 'Ah lam', 'F', 1);
INSERT INTO "FirstName" VALUES (8, 'An', 'F', 1);
INSERT INTO "FirstName" VALUES (9, 'Kers', 'M', 2);
INSERT INTO "FirstName" VALUES (10, 'Mog', 'M', 2);
INSERT INTO "FirstName" VALUES (11, 'Ketaki', 'F', 2);
INSERT INTO "FirstName" VALUES (12, 'Kusum', 'F', 2);
INSERT INTO "FirstName" VALUES (13, 'Acura', 'M', 4);
INSERT INTO "FirstName" VALUES (14, 'Audio', 'M', 4);
INSERT INTO "FirstName" VALUES (15, 'Apple', 'F', 4);
INSERT INTO "FirstName" VALUES (16, 'Atlanta', 'F', 4);
INSERT INTO "FirstName" VALUES (17, 'Dume', 'M', 5);
INSERT INTO "FirstName" VALUES (18, 'Ebi', 'M', 5);
INSERT INTO "FirstName" VALUES (19, 'Cleotha', 'F', 5);
INSERT INTO "FirstName" VALUES (20, 'Deka', 'F', 5);
INSERT INTO "FirstName" VALUES (21, 'Tremeur', 'M', 6);
INSERT INTO "FirstName" VALUES (22, 'Tugdual', 'M', 6);
INSERT INTO "FirstName" VALUES (23, 'Fifine', 'F', 6);
INSERT INTO "FirstName" VALUES (24, 'Fleur', 'F', 6);
-- LASTNAME
DELETE FROM "LastName" WHERE 1=1;
INSERT INTO "LastName" VALUES (1, 'Ang', 1);
INSERT INTO "LastName" VALUES (2, 'Tan', 1);
INSERT INTO "LastName" VALUES (3, 'Balakrishnan', 2);
INSERT INTO "LastName" VALUES (4, 'Krishnamurthy', 2);
INSERT INTO "LastName" VALUES (5, 'Baltimore', 4);
INSERT INTO "LastName" VALUES (6, 'Kinderman', 4);
INSERT INTO "LastName" VALUES (7, 'Sy', 5);
INSERT INTO "LastName" VALUES (8, 'Toure', 5);
INSERT INTO "LastName" VALUES (9, 'Sayegh', 6);
INSERT INTO "LastName" VALUES (10, 'Koury', 6);
-- -- ADDRESS
-- DELETE FROM "Address" WHERE 1=1;
-- INSERT INTO "Address" VALUES ('AUS',  '2609', '1/44-46 Maryborough St');
-- INSERT INTO "Address" VALUES ('AUS',  '2911', 'MITCHELL');
-- INSERT INTO "Address" VALUES ('CAN',  'T2J7E5', '12800 MacLeod Trail SE Alberta');
-- INSERT INTO "Address" VALUES ('CAN',  'T3L2Y6', '178 Tuscany Ravine Close NW');
-- INSERT INTO "Address" VALUES ('HKG',  '28', 'Room 1206 Hang Bong Commercial Centre');
-- INSERT INTO "Address" VALUES ('HKG',  '778', '2/F Harley House 776-778 Nathan Road');
-- INSERT INTO "Address" VALUES ('IDN',  '12870', 'Kav 74-75Kav 74-7 lantai 5 mezzanine, Jalan Jendral Gatot Subroto');
-- INSERT INTO "Address" VALUES ('IDN',  '17114', '1 Jl. Siaga 1, No. 1 RT.7/7, Jalan Siaga 1');
-- INSERT INTO "Address" VALUES ('MYS',  '52100 Kuala Lumpur', '1, Jalan Raja, City Centre');
-- INSERT INTO "Address" VALUES ('MYS',  '62000 Putrajaya', 'Alamanda Shopping Centre, Lg39, Jalan Alamanda, Presint 1');
-- INSERT INTO "Address" VALUES ('PHL',  '1112', '21 N. Romualdez, 34');
-- INSERT INTO "Address" VALUES ('PHL',  '1103', '18 Malakas, 148');
-- INSERT INTO "Address" VALUES ('SGP',  '127371', '#02-31, 154 West Coast Road');
-- INSERT INTO "Address" VALUES ('SGP',  '460084', '#01-23, 84 Bedok North Street 4');
-- INSERT INTO "Address" VALUES ('GBR',  'BT43 8JE', '325 Ballymenay Road');
-- INSERT INTO "Address" VALUES ('GBR',  'BT23 4EN', '35 West Street');
-- INSERT INTO "Address" VALUES ('THA',  '10200', '1 Khaosan Road, Taladyod Khwaeng Talat Yot, Khet Phra Nakhon, Krung Thep Maha Nakhon');
-- INSERT INTO "Address" VALUES ('THA',  '10700', '159 Charan Sanitwong Rd, Khwaeng Bang Bumru, Khet Bang Phlat, Krung Thep Maha Nakhon');
-- INSERT INTO "Address" VALUES ('USA',  '89521', '12663 Old Virginia Rd, Reno, NV');
-- INSERT INTO "Address" VALUES ('USA',  '97214', '107 SE Washington St, Portland, OR');

-- VERIFY
SELECT * FROM "Country";
SELECT * FROM "Race";
SELECT * FROM "CountryRace";
SELECT * FROM "FirstName";
SELECT * FROM "LastName";
-- SELECT * FROM "Address";