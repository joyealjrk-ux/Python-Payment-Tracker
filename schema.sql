CREATE TABLE IF NOT EXISTS pay_history (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    PRODUCT VARCHAR(50),
    MODE VARCHAR(20),
    CITY VARCHAR(20)
);

INSERT OR IGNORE INTO pay_history (ID, NAME, PRODUCT, MODE, CITY) VALUES 
(101, 'joyee', 'cold drink', 'netbanking', 'moraco'),
(102, 'shreya', 'catchup', 'cash', 'india'),
(103, 'anand', 't-shirt', 'netbanking', 'india'),
(104, 'rahul', 'water bottle', 'net banking', 'scotland'),
(105, 'avi', 'shoes', 'net banking', 'moraco'),
(106, 'mayank', 'crocks', 'cash', 'india'),
(107, 'miles', 'chocolate', 'net banking', 'US'),
(108, 'tom', 'chocolates', 'cash', 'US'),
(109, 'peter', 'cold drink', 'net banking', 'edinburgh'),
(110, 'cruise', 'shoes', 'cash', 'moraco'),
(111, 'natasha', 'dress', 'cash', 'new york'),
(112, 'merinda', 'crocks', 'cash', 'new york'),
(113, 'robert', 't-shirt', 'net banking', 'wakada'),
(114, 'rose', 'flowers', 'cash', 'new york'),
(115, 'drownie', 'flowers', 'net banking', 'moraco');