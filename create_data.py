import sqlite3

# Creating data base of owners

connection = sqlite3.connect('owners.db')

# query to create Best Buy Owners Table
connection.execute(''' CREATE TABLE bestbuy
                    (NAME VARCHAR    NOT NULL,
                   PAYMENT INT      NOT NULL,
                   DATE VARCHAR      NOT NULL);
'''
)

# Inserting data in the above table

connection.execute("INSERT INTO bestbuy VALUES ('Otavio',71,'07/31/2024')")
connection.execute("INSERT INTO bestbuy VALUES ('Otavio',71,'08/27/2024')")
connection.execute("INSERT INTO bestbuy VALUES ('Otavio',71,'09/25/2024')")
connection.execute("INSERT INTO bestbuy VALUES ('Otavio',71,'10/11/2024')")
connection.execute("INSERT INTO bestbuy VALUES ('Wagner',40,'11/07/2024')")
connection.execute("INSERT INTO bestbuy VALUES ('Otavio',71,'11/11/2024')")

cursor = connection.execute("SELECT * FROM bestbuy")

for row in cursor:
    print(row)