#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using
the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mySQLi
    import re
    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    state_name = ' '.join(argv[4].split())
    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid name state (example: California)')
        exit(1)

    try:
        db = mySQLi.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)
    curs = db.cursor()
    cuantity = curs.execute("""SELECT c.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      WHERE s.name = '{:s}'
                      ORDER BY c.id ASC;""".format(state_name))
    q_res = curs.fetchall()
    final = []

    for i in range(cuantity):
        final.append(q_res[i][0])

    print(', '.join(final))

    curs.close()
    db.close()
