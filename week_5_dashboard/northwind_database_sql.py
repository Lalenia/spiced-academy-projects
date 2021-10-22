CREATE TABLE employee_territories(
                                    employeeID  INTEGER,
                                    territoryID INTEGER not null
);
CREATE TABLE orders(
                        orderID         INT PRIMARY KEY,
                        customerID      CHAR(5),
                        employeeID      INTEGER,
                        orderDate       date,
                        requiredDate    date,
                        shippedDate     date,
                        shipVia         INTEGER,
                        freight         FLOAT,
                        shipName        VARCHAR(255),
                        shipAddress     VARCHAR(255),
                        shipCity        VARCHAR(255),
                        shipRegion      VARCHAR(255),
                        shipPostalCode  VARCHAR(255),
                        shipCountry     VARCHAR(255)
);
CREATE TABLE employees(      
                            employeeID       INT PRIMARY KEY,
                            lastName         VARCHAR(255),
                            firstName        VARCHAR(255),
                            title            VARCHAR(255),
                            titleOfCounrtesy VARCHAR(255),
                            birthDate        DATE,
                            hireDate         DATE,
                            address          VARCHAR(255),
                            city             VARCHAR(255),
                            region           VARCHAR(255),
                            postalCode       VARCHAR(255),
                            country          VARCHAR(255),
                            homePhone        VARCHAR(255),
                            extension        INT,
                            photo            TEXT,
                            notes            TEXT,
                            reportsTo        INT,
                            photoPath        VARCHAR(255)
);
CREATE TABLE categories(    
                            categoryID      INT PRIMARY KEY,
                            categoryName    VARCHAR(255),
                            description     VARCHAR(255),
                            picture         TEXT
);
CREATE TABLE customers(
                            customerID      CHAR(5),
                            companyName     VARCHAR(255),
                            contactName     VARCHAR(255),
                            contactTitle    VARCHAR(255),
                            address         VARCHAR(255),
                            city            VARCHAR(255),
                            region          VARCHAR(255),
                            postalCode      VARCHAR(255),
                            country         VARCHAR(255),
                            phone           VARCHAR(255),
                            fax             VARCHAR(255)
);
CREATE TABLE order_details(
                                orderID     INT,
                                productID   INT,
                                unitPrice   NUMERIC,
                                quantity    INT,
                                discount    NUMERIC
);
CREATE TABLE products(      productID    INT PRIMARY KEY,
                            productName  VARCHAR(255),
                            supplierID   INT,
                            categoryID   INT,
                            quantity     VARCHAR(255),
                            unitPrice    NUMERIC,
                            unitsInStock INT,
                            unitsOnOrder INT,
                            reorderLevel INT,
                            discontinued INT
);
CREATE TABLE regions(
                        regionID            INT PRIMARY KEY,
                        regioneDescription  VARCHAR(255)
);
CREATE TABLE shippers(
                        shipperID   INT PRIMARY KEY,
                        companyName VARCHAR(255),
                        phone       VARCHAR(255)
);
CREATE TABLE suppliers(
                        supplierID      INT PRIMARY KEY,
                        companyName     VARCHAR(255),
                        contactName     VARCHAR(255),
                        contactTitle    VARCHAR(255),
                        address         VARCHAR(255),
                        city            VARCHAR(255),
                        region          VARCHAR(255),
                        postalCode      VARCHAR(255),
                        country         VARCHAR(255),
                        phone           VARCHAR(255),
                        fax             VARCHAR(255),
                        homePage        VARCHAR(255)
);
CREATE TABLE territories(
                        territoryID             INT PRIMARY KEY,
                        territoryDescription    VARCHAR(255),
                        regionID                INT
);

\copy employee_territories FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/employee_territories.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy orders FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/orders.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy employees FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/employees.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy regions FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/regions.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy order_details FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/order_details.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy shippers FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/shippers.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy products FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/products.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy suppliers FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/suppliers.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy customers FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/customers.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';
\copy categories FROM '/Users/Narges/desktop/spiced/Week_5/northwind_data_clean-master/data/categories.csv' WITH DELIMITER ',' CSV HEADER NULL 'NULL';