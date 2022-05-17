from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import *

if __name__ == "__main__":
    engine = create_engine("sqlite:///C://Users//facu-//Documents//Python Projects//ProyectoApp//database//tests.db")
    Session = sessionmaker(bind = engine)
    session = Session()
    
    questions = [
        Question(
            question_text = "Como se define una lista?",
            answers = [
                Answer(
                    answer_text = "lista = [1,2,3]",
                    is_correct = True
                ),
                Answer(
                    answer_text = "lista = (1,2,3)",
                    is_correct = False
                ),
                Answer(
                    answer_text = "iter(1,2,3)",
                    is_correct = False
                )
            ]
        ),
        
        Question(
            question_text = "Se puede modificar los elementos de una tupla?",
            answers = [
                Answer(
                    answer_text = "Si",
                    is_correct = False
                ),
                Answer(
                    answer_text = "No",
                    is_correct = True
                )  
            ]
        )
    ]
    
    test = Test(test_name = "Python", questions = questions)
    session.add(test)
    session.commit()