#!/usr/bin/python3
"""
0-select_states module
Script that lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    mysql_username, mysql_pwd, db_name = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_pwd,
        db=db_name
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
