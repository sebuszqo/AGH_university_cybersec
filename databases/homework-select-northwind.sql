-- noinspection SpellCheckingInspectionForFile

use Northwind
-- Column selection exercises

-- 1. Select names and addresses of all customers.
select CompanyName, Address, City
from Customers;

-- 2. Select surnames and phone numbers of employees.
select LastName, HomePhone
from Employees

-- 3. Select names and prices of products.
select ProductName, UnitPrice
from Products

-- 4. Show all categories of products (names and descriptions).
select CategoryName, Description
from Categories

-- 5. Show names and home pages of suppliers.
select CompanyName, HomePage
from Suppliers


-- Row selection exercises


-- 1. Select the names and addresses of all customers based in London.
select CompanyName, Address
from Customers where City='London'

-- 2. Select the names and addresses of all customers based in France or Spain.
select CompanyName, Address
from Customers where Country='France' OR Country='Spain'

-- 3. Select the names and prices of products with a unit price between 20.00 and 30.00.
select ProductName, UnitPrice
from Products where UnitPrice > 20 AND UnitPrice < 30

-- 4. Select the names and prices of products in the 'meat' category.
select ProductName, UnitPrice
from Products where CategoryID = (
    select CategoryID from Categories where CategoryName = 'meat/poultry'
    )

select ProductName, UnitPrice
from Products where CategoryID = (
    select CategoryID from Categories where CategoryName like '%meat%'
    )

select Products.ProductName, Products.UnitPrice
from Products
join Categories on Products.CategoryID = Categories.CategoryID
where Categories.CategoryName = 'meat/poultry'

-- 5. Select the names of products and information on stock levels for products supplied by 'Tokyo Traders' company.
select ProductName, UnitsInStock
from Products where SupplierID =(
    select SupplierID
    from Suppliers where CompanyName='Tokyo Traders'
    )

-- 6. Select the names of products that are out of stock.
select ProductName
from Products where UnitsInStock <= 0


-- String comparison exercises


-- 1. Find information about products sold in bottles. ('bottle')
select ProductName
from Products where QuantityPerUnit like '%bottle%'

-- 2. Search for information about the job titles of employees whose last names start with a letter from B to L.
select FirstName, Title
from Employees where LastName like '[B-L]%'

select Title, LastName from Employees where LEFT(LastName, 1) between 'b' and 'l'

-- 3. Retrieve information about the job titles of employees whose last names start with the letter B or L.
select FirstName, Title
from Employees where LastName like '[BL]%'

-- 4. Find the names of categories that contain a comma in their description.
select CategoryName
from Categories where Description like '%,%'

-- 5. Find customers whose name contains the word 'Store' somewhere in it.
select CompanyName
from Customers where CompanyName like '%Store%'


SELECT productid, productname, supplierid, unitprice FROM products
WHERE (productname LIKE 'T%' OR productid = 46)
  AND  (unitprice >= 16.00)

SELECT productid, productname, supplierid, unitprice FROM products
WHERE (productname LIKE 'T%')
OR productid = 46 AND unitprice > 16.


-- range of values exercises


-- 1. Find information about products with prices less than 10 or greater than 20.
select * from Products where (UnitPrice < 10 OR UnitPrice > 20)
select * from Products where UnitPrice not between 10 and 20

-- 2. Select the names and prices of products with a unit price between 20.00 and 30.00.
select ProductName, UnitPrice from Products where UnitPrice between 20.00 and 30.00


-- Logical conditions exercises


-- 1. Select the names and countries of all customers located in Japan or Italy.
select CompanyName, Country from Customers where Country in ('Japan', 'Italy')

-- exercise

-- Write a SELECT statement to retrieve the order number, order date, and customer number
-- for all unfulfilled orders where the recipient's country is Argentina.
select OrderID, OrderDate, CustomerID from Orders where (ShipCountry ='Argentina' and ShippedDate is NULL)
select getdate()



-- ORDER BY exercises


SELECT productid, productname, categoryid, unitprice FROM products
ORDER BY 3,4 DESC

-- 1. Select the names and countries of all customers, sort the results by country, and within each country sort the company names alphabetically.
select CompanyName, Country from Customers order by 2,1

-- 2. Select information about products (category, name, price), sort the products by category and within each category sort them in descending order by price
select CategoryName, ProductName, UnitPrice
from Products
inner join Categories on Products.CategoryID = Categories.CategoryID
order by CategoryName asc , UnitPrice desc

-- 3. Select the names and countries of all customers whose headquarters are in Japan or Italy, sort the results as in point 1.
select CompanyName, Country
from Customers
where Country in ('Japan', 'Italy')
order by Country, CompanyName


-- eliminate duplicates
SELECT distinct country
FROM suppliers
ORDER BY country

-- changing name of columns
SELECT firstname AS First, lastname AS Last ,employeeid AS 'Employee ID:'
FROM employees

-- ??
SELECT firstname, lastname ,'Identification number:', employeeid
FROM employees

SELECT orderid, unitprice * 1.05 as newunitprice
FROM [order details]

SELECT firstname + ' ' + lastname as imie_nazwisko FROM employees

-- exercises
select *, (1-Discount) * UnitPrice * Quantity as orderamount
from [Order Details] where OrderID=10250

select Fax + ',' + Phone as 'fax and phone'
from Suppliers

select Fax + ',' + Phone as 'fax and phone'
from Suppliers where Fax is not null and Phone is not null

-- Napisz polecenie które dla każdego dostawcy (supplier) pokaże pojedynczą kolumnę zawierającą nr telefonu i nr faksu w formacie
-- (numer telefonu i faksu mają być oddzielone przecinkiem)
select CompanyName, concat(Fax, ',', Phone) as 'Fax + Phone' from Suppliers


SELECT IIF(Fax IS NULL, Phone, CONCAT(Phone, ',', Fax)) AS formatted FROM Suppliers

-- isnull change first parameter to the second one when the first one is null
select isnull(null, 9) from Suppliers

SELECT CONCAT(Phone, ISNULL(',' + Fax, '')) AS formatted FROM Suppliers


-- Homework

-- pokaż zamówienia złożone w marcu 97
select OrderDate
from Orders where DATEPART(year,OrderDate) = '1997' and DATEPART(month, OrderDate) = '3'

select OrderDate
from Orders where MONTH(OrderDate) = 3 and YEAR(OrderDate) = 1997;

SELECT OrderDate,* FROM Orders WHERE OrderDate BETWEEN '1997-03-01' AND '1997-03-31';

-- Dla każdego zamówienia wyświetl ile dni upłynęło od daty zamówienia do daty wysyłki
SELECT DATEDIFF(day,OrderDate, ShippedDate), OrderDate, ShippedDate AS dni_do_wysylki
FROM Orders

-- Pokaz przeterminowane zamówienia
select RequiredDate, ShippedDate
from Orders WHERE ShippedDate > RequiredDate

-- How many years has each employee worked for the company?
-- For each employee, display their first name, last name, and age.
select FirstName,LastName, DATEDIFF(year ,HireDate, GETDATE()) as 'years of being hired' from Employees

-- Display all employees who are now over 25 years old.
select *, DATEDIFF(year, BirthDate, GETDATE()) as year from Employees where DATEDIFF(year, BirthDate, GETDATE()) > 25

SELECT FirstName, LastName, BirthDate,
DATEDIFF(YEAR, BirthDate, GETDATE()) AS age
FROM employees
WHERE DATEADD(YEAR, 25, BirthDate) <= GETDATE()

-- Calculate the average number of months each employee has worked for the company.
SELECT AVG(DATEDIFF(MONTH, HireDate, GETDATE())) AS avg_months_worked
FROM employees

-- Display data for all employees who have worked for the company for at least 320 months but no more than 333 months.
select * from Employees where DATEDIFF(month, HireDate, GETDATE()) between 320 and 333

-- For each employee, display their first name, last name, year of birth, year in which they were hired, and the number of years they were when hired.
SELECT FirstName, LastName, YEAR(BirthDate) AS year_of_birth,
YEAR(HireDate) AS year_of_hire, DATEDIFF(YEAR, BirthDate, HireDate) AS age_when_hired
FROM employees;


-- For each employee, display their first name, last name, date of birth (year, month, and day), and the day of the week they were born.
SELECT FirstName, LastName,
YEAR(BirthDate) AS birth_year, MONTH(BirthDate) AS birth_month, DAY(BirthDate) AS birth_day,
DATENAME(WEEKDAY, BirthDate) AS birth_weekday
FROM employees;

-- Count how many letters the shortest employee name consists of.
SELECT MIN(LEN(FirstName)) as shortest_firstName
FROM employees

-- Display how many years have passed since January 1, 1990.

select DATEDIFF(year, '1990-01-01', GETDATE())

-- select GETDATE() as CurrentDate;