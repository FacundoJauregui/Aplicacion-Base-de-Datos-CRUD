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
        
    def get_test_names(self):
        tests = self.session.query().with_entities(Test.test_name).all()
        test_names = [test[0]for test in tests]
        return test_names
    
    def add_test_questions(self, _test_name, _question_text, _question_choices, _correct_choice):
        test = self.session.query(Test).filter(Test.test_name == _test_name).first()
        
        answer = [
            Answer(
                answer_text = choice,
                is_correct = _correct_choice == idx
            ) for idx, choice in enumerate(_question_choices)
        ]
        
        questions = Question(
            question_text = _question_text,
            answers = answer,
            test_id = test.test_id
        )
        
        self.session.add(questions)
        self.session.commit()