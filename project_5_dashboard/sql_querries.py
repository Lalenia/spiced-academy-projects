1. Get the names and the quantities in stock for each product.

SELECT "productName", "unitsInStock"
FROM products;

2. Get a list of current products (Product ID and name).

SELECT "productID", "productName"
FROM products
WHERE discontinued = 0;

3. Get a list of the most and least expensive products (name and unit price).

SELECT "productName", "unitPrice"
FROM products
WHERE "unitPrice" IN (
(SELECT MIN("unitPrice") FROM products),
(SELECT MAX("unitPrice") FROM products)
);

4. Get products that cost less than $20

SELECT "productName", "unitPrice"
FROM products
WHERE "unitPrice" < 20;


5. Get products that cost between $15 and $25.

SELECT "productName", "unitPrice"
FROM products
WHERE "unitPrice" BETWEEN 15 AND 25;

6. Get products above average price.

SELECT * FROM products where unitprice >= (select avg(unitprice) FROM products);

7. Find the ten most expensive products.

SELECT "productName", "unitPrice"
FROM products
ORDER BY "unitPrice" DESC
LIMIT 10 ;

8. Get a list of discontinued products (Product ID and name)

SELECT "productID", "productName"
FROM products
WHERE discontinued = 1;

9. Count current and discontinued products.

SELECT discontinued,count(*) from products group by discontinued;


10. Find products with less units in stock than the quantity on order.

SELECT "productName", "unitsOnOrder", "unitsInStock"
FROM products
WHERE "unitsInStock" < "unitsOnOrder";

11. Find the customer who had the highest order amount

SELECT SUM(order_details."unitPrice") AS sales, orders."customerID"
FROM orders
JOIN order_details
ON orders."orderID" = order_details."orderID"
GROUP BY "customerID"
ORDER BY sales DESC
LIMIT 1;

12. Get orders for a given employee and the according customer

SELECT "employeeID", "customerID", "orderID"
FROM orders
ORDER BY "employeeID", "customerID"
;


13. Find the hiring age of each employee

SELECT firstname,lastname,age(hiredate,birthdate) FROM employees;