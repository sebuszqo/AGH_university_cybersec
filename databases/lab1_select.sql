use Northwind
select * from products where SupplierID=4;
-- select * from suppliers;

select *
from Categories;


select *
from Products where Discontinued=1;


select *
from Customers where CustomerID='HANAR';

select * from orders where OrderID=10250;

select *
from "Order Details" where OrderID=10250;

SELECT EmployeeID,LastName, FirstName, Title
from Employees
where EmployeeID = 5 OR  EmployeeID = 7

select LastName,Country,City
from Employees where Country='USA'

select OrderDate, OrderID, CustomerID from Orders
where OrderDate < '1996-08-01'