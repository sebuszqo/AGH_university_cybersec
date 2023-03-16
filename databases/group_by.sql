

select OrderID, max(UnitPrice) as max_price from [Order Details]
group by OrderID



