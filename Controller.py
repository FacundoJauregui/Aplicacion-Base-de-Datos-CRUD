from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import *
from sqlite3 import ProgrammingError

class Controller:
    def __init__(self) -> None:
        engine = create_engine("sqlite:///C://Users//facu-//Documents//Python Projects//ProyectoApp//database//tests.db")
        Session = sessionmaker(bind = engine)
        self.session = Session()
        
    def empty_test(self, _test_name):
        test = self.session.query(Test).filter(Test.test_name == _test_name).first()
        if test == None:
            new_test = Test(test_name = _test_name)
            self.session.add(new_test)
            self.session.commit()
        else:
            raise ProgrammingError("Test already exists")