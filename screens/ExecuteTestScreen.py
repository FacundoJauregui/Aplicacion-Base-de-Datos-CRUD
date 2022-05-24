import tkinter as tk
from styles import style
from components.MainMenu import MainMenu

class ExecuteTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = style.BACKGROUND
        )
    
    def init_widgets(self, question):
        self.manager.num_questions += 1
        self.helper_frame = tk.Frame(
            self
        )
        self.helper_frame.configure(background = style.BACKGROUND)
        self.helper_frame.pack(**style.PACK)
        
        self.question_text = tk.StringVar(self, question.question_text)
        self.selected_answer = tk.IntVar(self, question.answers[0].answer_id)
        
        
        tk.Label(
            self.helper_frame,
            textvariable = self.question_text,
            justify = tk.CENTER,
            **style.STYLE #Desempaquetamos el diccionario desde el modulo para usar STYLE
        ).pack(
            **style.PACK
        )

        id = -1
        for answer in question.answers:
            if answer.is_correct:
                id = answer.answer_id
            tk.Radiobutton(
                self.helper_frame,
                text = answer.answer_text,
                variable = self.selected_answer,
                value = answer.answer_id,
                activebackground = style.BACKGROUND,
                activeforeground = style.TEXT,
                **style.STYLE
            ).pack(
                **style.PACK
            )
            
        tk.Button(
            self.helper_frame,
            text = "Siguiente Pregunta",
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,
            **style.STYLE,
            command = lambda: self.next_question(id)
        ).pack(
                **style.PACK
        )

        MainMenu(
            self.helper_frame,
            self.manager
        ).pack(
            **style.PACK
        )
        
    def check_answer(self, correct_id):
        if self.selected_answer.get() == correct_id:
            self.manager.num_aciertos += 1
            
    def next_question(self, correct_id):
        try:
            self.helper_frame.pack_forget()
            self.helper_frame.destroy()
            self.check_answer(correct_id)
            self.init_widgets(next(self.manager.questions))
        except StopIteration:
            print("No Mas Preguntas")
            self.manager.execute_to_finish()