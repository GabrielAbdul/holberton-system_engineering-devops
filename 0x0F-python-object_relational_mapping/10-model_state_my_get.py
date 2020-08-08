#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''


if __name__ == '__main__':
    import sqlalchemy
    import sys
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker as sm

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
                           '.format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # define parameters for session
    Session = sm(bind=engine)

    # create session
    session = Session()

    # query our results
    result = session.query(State).filter(State.name == sys.argv[4])

    # print our result, formatted correctly
    flag = 0
    for results in result:
        print(results.id)
        flag = 1

    if flag == 0:
        print("Not found")
