from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean

Base = declarative_base()

#CREAMOS LAS TABLAS
#CREATE THE TABLES
class Answer(Base):
    __tablename__ = "ANSWER"
    answer_id = Column(Integer, primary_key = True)
    answer_text = Column(String(200))
    is_correct = Column(Boolean, nullable = True)
    question_id = Column(Integer, ForeignKey("QUESTION.question_id", ondelete = "CASCADE"))#Al momento de eliminar una pregunta, se eliminan en "cascada" todas sus posibles respuestas
    
    def __repr__(self) -> str:
        return f"Answer object: Answer id: {self.answer_id}. Answer text: {self.answer_text}"
    
class Question(Base):
    __tablename__ = "QUESTION"
    question_id = Column(Integer, primary_key = True)
    question_text = Column(String(200))
    answers = relationship("Answer", cascade = "all,delete", backref = backref("QUESTION"))#Establece una relacion entre respuesta y pregunta para que de ambos lados se sepa a que pregunta o respuesta pertenece
    test_id = Column(Integer,ForeignKey("TEST.test_id", ondelete = "CASCADE"))
    
    def __repr__(self) -> str:
        return f"Question object: Question id: {self.question_id}. Question text: {self.question_text}"
    
class Test(Base):
    __tablename__ = "TEST"
    test_id = Column(Integer, primary_key = True)
    test_name = Column(String(100))
    questions = relationship("Question", cascade = "all,delete", backref = backref("TEST"))
    
    def __repr__(self) -> str:
        return f"Test object: Test id: {self.test_id}. Test text: {self.test_name}"
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///C://Users//facu-//Documents//Python Projects//ProyectoApp//database//tests.db", echo = True)
    Base.metadata.create_all(engine)#Agarra todos los atributos de las clases de arriba y crea las tablas