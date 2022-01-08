#!/usr/bin/python3
"""14th module - this module works with two tables:
State and City
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for s, c in session.query(State, City).join(City).order_by(City.id).all():
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
    session.close()
