select top 1 *
from [Order Details]
order by Quantity desc


select top 5 OrderID, ProductID, Quantity
from [Order Details]
order by Quantity desc;


-- not rly 5 elements, but all of these that are = 5'th element
select top 5 with ties OrderID, ProductID, Quantity
from [Order Details]
order by Quantity desc;

select *
from Employees;

-- do count null's
select count(*)
from Employees;

-- do not count null's
select count(ReportsTo)
from Employees;

-- how many orders
select count(*)
from orders

-- count(*) = count(orderID) -- orderID never will be a null

-- how many shipped orders
select count(ShippedDate)
from orders

select avg(UnitPrice) as average_price
from Products

select sum(quantity)
from [Order Details]
where ProductID = 1

select *
from orderhist


select productid, sum(quantity) as total_quantity
from orderhist
group by productid


select productid, sum(quantity) as total_quantity, max(quantity) as max
from orderhist
where productid = 2
group by productid


select productid, sum(quantity) as total_quantity
from [Order Details]
where ProductID between 10 and 35
group by productid
order by ProductID


select OrderID, sum(UnitPrice * Quantity * (1 - Discount)) as value
from [Order Details]
where OrderID = 10250
group by OrderID


select productid, sum(quantity)
from orderhist
-- where orderid >= 2
group by productid
having productid >= 2
   and sum(quantity) > 30


select productid, sum(quantity)
from [Order Details]
group by productid
having sum(Quantity) > 1200


-- summing up
select productid, orderid, sum(quantity) as total_quantity
from orderhist
group by productid, orderid
with rollup
order by productid, orderid


-- summing up
select productid, orderid, sum(quantity) as total_quantity
from orderhist
group by productid, orderid
with cube
order by productid, orderid

--  LABS Order By
SELECT TOP 1 ShipVia, COUNT(OrderID) AS TotalOrders
FROM ORDERS
WHERE year(ShippedDate) = '1997'
GROUP BY ShipVia
ORDER BY TotalOrders DESC


SELECT *
FROM Orders
WHERE OrderID IN (SELECT OrderID
                  FROM [Order Details]
                  GROUP BY OrderID
                  HAVING COUNT(*) > 5);



SELECT OrderID, count(*)
FROM [Order Details]
GROUP BY OrderID
HAVING COUNT(*) > 5


select CustomerID, count(*) as CountProduct
from Orders
where year(OrderDate) = '1998'
group by CustomerID
having count(*) > 8
order by CountProduct


select count(*) as product_count, orderID
from [Order Details]
group by orderID
having count(*) > 5

select CustomerID, count(*) as counter
from Orders
         inner join [Order Details] "[O D]" on Orders.OrderID = "[O D]".OrderID
where year(OrderDate) = '1998'
group by CustomerID















