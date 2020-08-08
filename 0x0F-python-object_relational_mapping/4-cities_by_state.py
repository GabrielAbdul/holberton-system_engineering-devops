#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''
import MySQLdb
from sys import argv


if __name__ == '__main__':

    # our unput values to connect to the database
    uname = argv[1]
    pass_word = argv[2]
    data_base = argv[3]

    # creating our database object
    db = MySQLdb.connect('localhost', uname, pass_word, data_base)

    # create a cursor
    cur = db.cursor()

    # execute our sql command
    cur.execute("SELECT c.id, c.name, s.name FROM cities c INNER JOIN\
                states s ON c.state_id=s.id;")

    # feth our data
    data = cur.fetchall()

    # print out our data
    for data in data:
        print(data)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()
