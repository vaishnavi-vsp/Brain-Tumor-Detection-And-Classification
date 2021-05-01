# create database using sqlite3
import sqlite3

db_local = 'patients.db'
conn = sqlite3.connect(db_local)
c = conn.cursor()

# c.execute(""" CREATE TABLE logindb
# (
# username TEXT PRIMARY KEY , password TEXT, fullname TEXT, emailid TEXT, hname TEXT, position TEXT
# )
# """)

c.execute(""" CREATE TABLE doctors
(
dId int PRIMARY KEY, name varchar(20), contact varchar(10), description TEXT, website TEXT, city varchar(20)
)
""")

# c.execute(""" DROP TABLE doctors """)

conn.commit()
conn.close()
