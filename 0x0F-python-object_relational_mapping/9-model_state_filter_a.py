#!/usr/bin/python3
'''script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    eng = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3],
                                                      pool_pre_ping=True)
    engine = create_engine(eng)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
