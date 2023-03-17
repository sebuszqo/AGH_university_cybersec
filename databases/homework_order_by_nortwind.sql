-- difference between counting and no counting nulls
USE northwind
SELECT COUNT(*)
FROM employees

USE northwind
SELECT COUNT(reportsto)
FROM employees

-- Provide the number of products with prices less than $10 or greater than $20:
select count(*) as counter
from Products
where UnitPrice between 10 and 20

-- Provide the maximum price for products below $20:
select max(UnitPrice) as max_price_bellow_20$
from Products
where UnitPrice < 20

-- Provide the maximum, minimum, and average price for products sold in bottles:
SELECT MAX(UnitPrice) as max_price_bottle, MIN(UnitPrice) as min_price_bottle, AVG(UnitPrice) as avg_price_bottle
FROM products
WHERE QuantityPerUnit LIKE '%bottle%';

-- List information about all products with prices above average:
select *
from Products
where UnitPrice > (select avg(UnitPrice) from Products)

-- Provide the sum/order value for order number 10250:
select sum(Quantity * (UnitPrice - Discount))
from [Order Details]
where OrderID = 10250

-- Provide the maximum price of ordered product for each order:
select orderid, max(UnitPrice) as maxPrice
from [Order Details]
group by orderid

-- Sort orders by maximum product price:
SELECT OrderID, MAX(UnitPrice) as max_price
FROM [Order Details]
GROUP BY OrderID
ORDER BY max_price DESC;

-- Provide the maximum and minimum price of ordered product for each order:
select orderid, max(UnitPrice) as maxPrice, min(UnitPrice) as minPrice
from [Order Details]
group by orderid
order by maxPrice desc, minPrice asc

-- Provide the number of orders delivered by each shipper:
select ShipVia, Shippers.CompanyName, count(*) as numberOfOrders
from Orders,
     Shippers
where ShipVia = Shippers.shipperID
group by ShipVia, Shippers.CompanyName

-- Which shipper was the most active in 1997:
select ShipVia, Shippers.CompanyName, count(*)
from Orders,
     Shippers
where year(ShippedDate) = 1997
  and ShipVia = Shippers.shipperID
group by ShipVia, Shippers.CompanyName

-- Display orders for which the number of order items is greater than 5:
select OrderID, count(*) as amount
from [Order Details]
group by OrderID
having count(*) > 5

SELECT *
FROM orders
WHERE OrderID IN (SELECT OrderID
                  FROM [Order Details]
                  GROUP BY OrderID
                  HAVING COUNT(*) > 5);

-- Display customers for whom more than 8 orders were fulfilled in 1998 (sort results in descending order by total amount for each customer):
select C.CompanyName, O.CustomerID, count(*) as Orders, sum(Freight) as FreightSum
from Orders O
         inner join Customers C
                    on O.CustomerID = C.CustomerID
where year(ShippedDate) = 1998
group by O.CustomerID, C.CompanyName
having count(*) > 8
order by sum(Freight) desc

select C.CompanyName, count(C.CustomerID) as NumberOfOrders, sum(Freight) as cost
from Customers C
         inner join Orders o
                    on O.CustomerID = C.CustomerID
where year(O.ShippedDate) = '1998'
group by C.CustomerID, C.CompanyName
having count(*) > 8
order by sum(Freight) desc

-- select Orders.CustomerID, companyName
-- from Orders,
--      Customers,
--      [Order Details]
-- where Orders.CustomerID = Customers.CustomerID
--   and [Order Details].OrderID = Orders.OrderID
--   and year(Orders.ShippedDate) = 1998
-- group by Orders.CustomerID, CompanyName
-- having count(Orders.CustomerID) > 8
-- order by CustomerID




