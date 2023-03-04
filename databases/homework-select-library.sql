-- exercise 1
use library
-- 1. Write a select statement that retrieves the title and book number.
select isbn, title
from title
         inner join item on title.title_no = item.title_no

-- 2. Write a select statement that retrieves the title with a book number of 10.
select title
from title
where title_no = 10

-- 3. Write a select statement that retrieves the book number and author from the title table for all books whose author is Charles Dickens or Jane Austen.
select title_no, author
from title
where author in ('Charles Dickens', 'Jane Austen')

-- exercise 2
-- 1. Write a statement that selects the title number and title for all books whose titles contain the word "adventure".
select title, title_no
from title
where title like '%adventure%'

-- 2. Write a statement that selects the reader number and their paid fee.
select member_no, fine_paid
from loanhist
where fine_paid is not null

-- 3. Write a statement that selects all unique pairs of cities and states from the adult table.
select distinct city, state
from adult

-- 4. Write a statement that selects all titles from the title table and displays them in alphabetical order.
select title
from title
order by title asc

-- exercise 3
-- 1. Write a command that:
--0
-- selects the member number (member_no), book ISBN (isbn), and the value of the assessed fine (fine_assessed) from the loanhist table for all loans that have an assessed fine (a non-NULL value in the fine_assessed column).
-- creates a computed column containing double the value of the fine_assessed column
-- creates an alias 'double fine' for this computed column

select member_no, isbn, fine_assessed, fine_assessed * 2 as 'double fine'
from loanhist
where fine_assessed is not null

-- exercise 4
select lower(firstname + middleinitial + substring(lastname, 1, 2)) as 'email_name'
from member

select lower(concat(firstname, middleinitial, substring(lastname, 1, 2))) as 'email_name'
from member

-- exercise 5
select concat('The title is: ', title, ', title number ', title_no) as result
from title;
