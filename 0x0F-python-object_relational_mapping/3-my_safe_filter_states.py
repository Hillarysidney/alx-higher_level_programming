#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
(Safe from SQL Injection)
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mySQLi
    import re

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    searches = ' '.join(argv[4].split())
    if (re.search('^[a-zA-Z ]+$', searches) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)
    try:
        db = mySQLi.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    curs = db.cursor()
    curs.execute("SELECT * FROM states \
                    WHERE name = '{:s}' ORDER BY id ASC;".format(searches))
    q_res = curs.fetchall()

    for row in q_res:
        print(row)
    curs.close()
    db.close()
