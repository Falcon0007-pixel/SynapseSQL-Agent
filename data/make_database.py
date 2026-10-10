import sqlite3
from pathlib import Path

DB_path = Path(__file__).parent / "shop.db"

con = sqlite3.connect(DB_path)
con.executescript( """ 
 DROP TABLE IF EXISTS orders;
 DROP TABLE IF EXISTS customers;

 CREATE TABLE customers (
    id  INTEGER PRIMARY KEY,
    name NOT NULL,
    country TEXT
 );

 CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    order_date TEXT,
    total_amount REAL 
 );

 INSERT INTO customers VALUES (1,'Ali','PK'), (2,'Sara','IT'), (3,'Omar','PK');

 INSERT INTO orders VALUES
 (1,1,'2022-01-10',100), (2,1,'2022-02-11',50),
 (3,2,'2022-03-05',200),
 (4,3,'2022-04-01',30), (5,3,'2022-05-09',40), (6,3,'2022-06-20',20);                  
""")
con.commit()
con.close()
print(f"Created {DB_path}")