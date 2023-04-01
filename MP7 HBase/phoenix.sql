CREATE VIEW "powers" ( pk VARCHAR PRIMARY KEY, "personal"."hero" VARCHAR, "personal"."power" VARCHAR, "professional"."name" VARCHAR, "professional"."xp" VARCHAR, "custom"."color" VARCHAR);
SELECT p."name" AS "Name1", p1."name" AS "Name2", p."power" AS "Power"
FROM "powers" AS p
INNER JOIN "powers" AS p1
ON p."power" = p1."power"
WHERE p."hero" = 'yes' AND p1."hero" = 'yes';
