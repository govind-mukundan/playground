
/* Help */
/* https://www.techonthenet.com/sql/index.php */


/* Drop */
DROP TABLE People, Prizes

/* Create */
CREATE TABLE People (
ID int NOT NULL identity(1,1),
Name varchar(255 ) NOT NULL, 
Address varchar(255 ) NOT NULL
)

CREATE TABLE Prizes (
ID int NOT NULL identity(1,1),
Name varchar(255 ) NOT NULL, 
Prize varchar(255 ) NOT NULL
)

/* Insert */
INSERT INTO People (Name, Address)
VALUES ('Govind', 'AMK'), ('Anisha', 'Orchard'), ('Kafka', 'Vietnam')

INSERT INTO Prizes (Name, Prize)
VALUES ('Govind', 'Nobel'), ('Anisha', 'Oscar'), ('Sachin', 'World Cup')

/* View a subset of table entries 
SELECT * FROM People LIMIT 5   ==> SQLite / MySQL
*/
SELECT TOP(2) * FROM People 

/* ======== Cartesian Product ========== */
SELECT * FROM People, Prizes

/* ===== Joins ========= */

/* Joining is basically concerned with "joining" or "combining" rows in two different tables. 
Typically you want to generate a single row for "matching" rows in different tables, joins help with that. 
Depending on how the operation handles rows that *do not* match, joins are sub-classified */

/* Inner */
SELECT * 
FROM People, Prizes 
WHERE People.Name = Prizes.Name

SELECT * 
FROM People INNER JOIN Prizes ON 
People.Name = Prizes.Name

/* Left and Right */
SELECT * 
FROM People LEFT JOIN Prizes ON 
People.Name = Prizes.Name

SELECT * 
FROM People RIGHT JOIN Prizes ON 
People.Name = Prizes.Name

/* Outer / Full Outer */
SELECT * 
FROM People FULL OUTER JOIN Prizes ON 
People.Name = Prizes.Name

/*	To find exclusions, you just have to "select" the entries with NULL Keys */
/* eg: Left Excluding Join */
SELECT * 
FROM People LEFT JOIN Prizes ON 
People.Name = Prizes.Name
WHERE Prizes.Name IS NULL

/* ======== GROUPING =========== */
/* SELECT column1, column2FROM table_nameWHERE [ conditions ]GROUP BY column1, column2ORDER BY column1, column2
*/

INSERT INTO People (Name, Address)
VALUES ('Govind', 'Delhi')

SELECT Name, count(*) 
FROM People GROUP BY Name

/* Filter using LIKE */
SELECT Name
FROM People
WHERE Address LIKE '%AMK%'

/* Not valid because Address is not equal between the various Name groups
SELECT Name, Address 
FROM People GROUP BY Name 
*/

/* Ascending and Descending Ordering */
SELECT *
FROM People ORDER BY Name DESC

SELECT *
FROM People ORDER BY Name ASC

SELECT Name, count(*) 
FROM People GROUP BY Name ORDER BY Name

/* Get Unique elements */
SELECT DISTINCT Name AS UniqueNames
FROM People

/* Get the count of rows in a table */
SELECT count(*) AS TotalPeople
FROM People

/* Case Insensitive filtering, and rejecting samples */
INSERT INTO People (Name, Address)
VALUES ('govind', 'Mumbai')

SELECT Name COLLATE Latin1_General_CS_AS as name, count(name) 
FROM People GROUP BY Name 


/* ============= OPERATORS ====================== */

/* Logical */

/* IN - with subquery or list */
Select *
From People
Where Name IN ('Govind', 'Sam')

/* ANY - with subquery only (cannot be used with a list) */
/* https://docs.microsoft.com/en-us/sql/t-sql/language-elements/some-any-transact-sql?view=sql-server-2017 */
Select *
From People
Where Name = ANY(SELECT Name FROM Prizes)

/* ALL: All elements of the subquery must satisfy the condition - with subquery only (cannot be used with a list) */
Select *
From People
Where Name > ALL(SELECT Name FROM Prizes)



/* TO DO */



/* Subqueries and Common Table Expressions */
/* refer: https://blog.expensify.com/2015/09/25/the-simplest-sqlite-common-table-expression-tutorial/ */

/* CTEs are basically "named subqueries", they have to be defined first, before the actual usage */
WITH my_cte AS ( SELECT * FROM Prizes )
SELECT Name FROM my_cte;

