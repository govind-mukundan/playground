# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:19:19 2018

@author: Govind
"""

import sqlite3 as db

conn = db.connect("example.db")  # sqlite3.connect(":memory:") --> Creates an in memory database
c = conn.cursor()

# Executing SQL
c.execute("DROP TABLE IF EXISTS Students")
c.execute("CREATE TABLE Students (gtid INTEGER, name TEXT)")
c.execute("INSERT INTO Students VALUES (123, 'Vuduc')")

# Commit to make the changes visible to *other* connections, note that the changes are already visible in your connection
conn.commit()


con = db.connect(":memory:")
cur = con.cursor()
cur.execute("create table characters(c)")

# Parameter Substitution should always be used instead of string concatenation when creating queries

# Execute the command for all elements in the parameter sequence
cur.executemany("insert into characters(c) values (?)", ['a', 'b', 'c'])
# cur.execute("insert into characters(c) values (?)", ['a', 'b', 'c'])  # Wont work

cur.execute("select c from characters")
print(cur.fetchall())