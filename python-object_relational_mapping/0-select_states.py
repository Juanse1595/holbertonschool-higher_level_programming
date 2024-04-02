#!/usr/bin/python3
"""
0th task module: lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_user, mysql_passwd, db_name = argv[1], argv[2], argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_passwd, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    print(query_rows)
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
