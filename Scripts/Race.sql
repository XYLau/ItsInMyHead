DELETE FROM "Race" WHERE 1=1;

INSERT INTO "Race" VALUES (0, 'Generic');
INSERT INTO "Race" VALUES (1, 'Chinese');
INSERT INTO "Race" VALUES (2, 'Indian');
INSERT INTO "Race" VALUES (3, 'Malay');
INSERT INTO "Race" VALUES (4, 'American');
INSERT INTO "Race" VALUES (5, 'African');
INSERT INTO "Race" VALUES (6, 'French');

-- COUNT = 7
SELECT COUNT(1) FROM "Race";

-- QUERY = 'Chinese'
SELECT "raceDesc" FROM "Race" WHERE "raceId" = 1;
