SELECT TOP 1 ShipVia, COUNT(OrderID) AS TotalOrders
FROM ORDERS
WHERE year(ShippedDate) = '1997'
GROUP BY ShipVia
ORDER BY TotalOrders DESC



SELECT * FROM Orders WHERE OrderID IN (
SELECT OrderID FROM [Order Details] GROUP BY OrderID HAVING COUNT(*) > 5
);



SELECT OrderID, count(*)
FROM [Order Details] GROUP BY OrderID HAVING COUNT(*) > 5



select CustomerID, count(*) as CountProduct
from Orders where year(OrderDate) = '1998'
group by CustomerID
having count(*) > 8
order by CountProduct


select count(*) as product_count, orderID
from [Order Details]
group by orderID
having count(*) > 5

select CustomerID, count(*) as counter from Orders
inner join [Order Details] "[O D]" on Orders.OrderID = "[O D]".OrderID
where year(OrderDate) = '1998'
group by CustomerID











