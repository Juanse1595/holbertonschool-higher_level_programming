#!/usr/bin/python3
'''5-filter_cities.py module'''
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT name
                FROM cities
                WHERE state_id =
                (SELECT id
                FROM states
                WHERE name LIKE BINARY %s)
                ORDER BY id ASC""", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(', '.join(row[0] for row in query_rows))
    cur.close()
    conn.close()
