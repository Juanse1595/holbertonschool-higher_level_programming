#!/usr/bin/python3
"""Start link class to table in database """
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
    first_object = session.query(State
                                 ).order_by(State.id).first()
    if (first_object is not None):
        print("{}: {}".format(first_object.id, first_object.name))
    else:
        print("Nothing")
    session.close()
