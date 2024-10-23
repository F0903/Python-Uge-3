USE northwind;

/* opgave 2 */
SELECT * FROM products
ORDER BY UnitPrice DESC;

/* opgave 3 */
SELECT * FROM customers
WHERE Country = "UK" OR Country = "Spain";

/* opgave 4 */
SELECT * FROM products
WHERE UnitsInStock > 100 AND UnitPrice >= 25;

/* opgave 5 */
SELECT DISTINCT ShipCountry FROM orders;

/* opgave 6 */
SELECT * FROM orders
WHERE MONTH(OrderDate) = 10 AND YEAR(OrderDate) = 1996;

/* opgave 7 */
SELECT * FROM orders
WHERE ShipRegion IS NULL AND ShipCountry = "Germany" AND Freight >= 100 
AND EmployeeID = 1 AND YEAR(OrderDate) = 1996;

/* opgave 8 */
SELECT * FROM orders
WHERE ShippedDate > RequiredDate;

/* opgave 9 */
SELECT * FROM orders
WHERE YEAR(OrderDate) = 1997 AND MONTH(OrderDate) IN (01, 02, 03, 04) 
AND ShipCountry = "Canada";

/* opgave 10 */
SELECT * FROM orders
WHERE EmployeeID IN (2, 5, 8) AND ShipRegion != "" AND ShipVia IN (1, 3)
ORDER BY EmployeeID, ShipVia;

/* opgave 11 */
/* kan ikke laves da der er fejl i opgaven */