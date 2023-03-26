SELECT companyname, customers.customerid, orderdate
FROM customers
         LEFT OUTER JOIN orders
                         ON customers.customerid = orders.customerid

SELECT companyname, customers.customerid, orderdate
FROM customers
         JOIN orders
              ON customers.customerid = orders.customerid

--
-- select distinct [O D].OrderID,
--                 O.OrderID,
--                 ShipName,
--                 ShipAddress,
--                 ShipCity,
--                 ShipPostalCode,
--                 ShipCountry,
--                 UnitPrice
-- from [Order Details] [O D]
--          inner join Orders O on O.OrderID = [O D].OrderID
-- where UnitPrice between 20 and 30

-- Wybierz nazwy i ceny produktów (baza northwind) o cenie jednostkowej pomiędzy 20.00 a 30.00, dla każdego produktu podaj dane adresowe dostawcy
select ProductName, UnitPrice, suppliers.address
from Products
         inner join Suppliers
                    on Products.SupplierID = suppliers.SupplierID
where UnitPrice between 20 and 30



select *
from [Order Details]
where OrderID = 10598

-- Wybierz nazwy produktów oraz inf. o stanie magazynu dla produktów dostarczanych przez firmę ‘Tokyo Traders’
select S.SupplierID, P.SupplierID, P.UnitsInStock, P.ProductName
from Suppliers S
         inner join Products P on S.SupplierID = P.SupplierID
where CompanyName = 'Tokyo Traders'

select ProductName, UnitsInStock, S.companyname
from Products P
         inner join Suppliers S
                    on P.SupplierID = S.SupplierID
where CompanyName = 'Tokyo Traders'

select *
from Suppliers
where CompanyName = 'Tokyo Traders'

select *
from Products
where SupplierID = 4

-- Czy są jacyś klienci którzy nie złożyli żadnego zamówienia w 1997 roku, jeśli tak to pokaż ich dane adresowe

select customers.CustomerID, customers.address
from Customers
         left outer join Orders
                         on Orders.CustomerID = Customers.CustomerID and year(OrderDate) = 1997
where Orders.OrderID is null

select CustomerID, CompanyName, Address
from Customers C
where C.CustomerID not in (select CustomerID
                           from Orders
                           where year(OrderDate) = 1997)
select *
from orders

-- Wybierz nazwy i numery telefonów dostawców, dostarczających produkty, których aktualnie nie ma w magazynie
select ProductName, CompanyName, UnitsInStock, phone
from Products
         left join Suppliers S on S.SupplierID = products.SupplierID
where UnitsInStock = 0

select ProductName, CompanyName, UnitsInStock, phone
from Products
    join Suppliers S on S.SupplierID = Products.SupplierID
where UnitsInStock = 0

select companyname, phone, unitsinstock, ProductID, Products.SupplierID
from Suppliers
         left outer join Products
                         on Suppliers.SupplierID = Products.SupplierID
where UnitsInStock = 0
   or UnitsInStock is null

select *
from Products


use library2
-- Napisz polecenie, które wyświetla listę dzieci będących członkami biblioteki (baza library). Interesuje nas imię, nazwisko i data urodzenia dziecka.
select m.firstname, m.lastname, j.birth_date
from juvenile j
         inner join member m on m.member_no = j.member_no

select firstname, lastname, birth_date
from member
         inner join juvenile
                    on member.member_no = juvenile.member_no

-- Napisz polecenie, które podaje tytuły aktualnie wypożyczonych książek
select loan.title_no, t.title, loan.due_date
from loan
         inner join title t on t.title_no = loan.title_no;

-- Podaj informacje o karach zapłaconych za przetrzymywanie książki o tytule ‘Tao Teh King’. Interesuje nas data oddania książki, ile dni była przetrzymywana i jaką zapłacono karę
select out_date, in_date, due_date, datediff(day, due_date, in_date) as 'amount of days', fine_paid, title
from loanhist L
         inner join title T
                    on L.title_no = T.title_no
where title = 'Tao Teh King'
  and fine_paid > 0



select in_date, due_date, datediff(day, due_date, in_date) as days, fine_paid
from loanhist
         inner join title t on t.title_no = loanhist.title_no
where t.title = 'Tao Teh King'
  and due_date < loanhist.in_date






select * from loanhist where fine_assessed is not null
select title_no, fine_paid from loanhist where title_no = 24

select title, title_no from title where title = 'Tao Teh King'
select *
from loanhist;

-- Napisz polecenie które podaje listę książek (mumery ISBN) zarezerwowanych przez osobę o nazwisku: Stephen A. Graff
select isbn
from reservation
         inner join member m on m.member_no = reservation.member_no
where lastname = 'Graff'
  and firstname = 'Stephen'
  and middleinitial = 'A'

select *
from member
where firstname = 'Stephen'
  and lastname = 'Graff'
select *
from reservation
where member_no = 205

use Northwind
-- Wybierz nazwy i ceny produktów (baza northwind) o cenie jednostkowej pomiędzy 20.00 a 30.00, dla każdego produktu podaj dane adresowe dostawcy, interesują nas tylko produkty z kategorii ‘Meat/Poultry’
select ProductName, UnitPrice, S.country, S.City, S.Address
from Products
         inner join Categories C on C.CategoryID = Products.CategoryID
         inner join Suppliers S on Products.SupplierID = S.SupplierID
where (UnitPrice between 20 and 30)
  and CategoryName = 'Meat/Poultry'

select *
from Categories
select *
from Products
where CategoryID = 6


-- Wybierz nazwy i ceny produktów z kategorii ‘Confections’ dla każdego produktu podaj nazwę dostawcy.

select UnitPrice, ProductName, S.CompanyName
from Products
         join Categories C on Products.CategoryID = C.CategoryID
         join Suppliers S on Products.SupplierID = S.SupplierID
where CategoryName = 'Confections'

select ProductName, UnitPrice, CompanyName, CategoryName
from Products P
         inner join Suppliers S
                    on P.SupplierID = S.SupplierID
         inner join Categories C
                    on P.CategoryID = C.CategoryID
where CategoryName = 'Confections'

select *
from Categories
select *
from Products
where CategoryID = 3

-- Wybierz nazwy i numery telefonów klientów , którym w 1997 roku przesyłki
-- dostarczała firma ‘United Package’

select distinct C.CompanyName, C.Phone
from Customers C
         inner join Orders O
                    on C.CustomerID = O.CustomerID
         inner join Shippers S
                    on O.ShipVia = S.ShipperID
where S.CompanyName = 'United Package'
  and YEAR(ShippedDate) = 1997