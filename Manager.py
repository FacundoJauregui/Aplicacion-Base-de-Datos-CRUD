import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen
from screens.AddTestScreen import AddTestScreen
from screens.SelectTestScreen import SelectTestScreen
from screens.UpdateTestScreen import UpdateTestScreen
from screens.ExecuteTestScreen import ExecuteTestScreen
from screens.TestFinishedScreen import TestFinishedScreen
from screens.DeleteTestScreen import DeleteTestScreen
from styles import style


#Configuracion del manager que se va a encargar de posicionar el frame que queramos
class Manager(tk.Tk):
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.title("Examenes de Programacion")
        self.controller = Controller()
        self.selected_test = ""
        self.num_questions = 0
        self.num_aciertos = 0
        self.questions = ""
        self.container = tk.Frame(self)
        self.container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        self.container.configure(
            background = style.BACKGROUND
        )
        self.container.grid_columnconfigure(0,weight = 1)
        self.container.grid_rowconfigure(0,weight = 1)
        self.frames = {}
        screens = (HomeScreen, AddTestScreen, UpdateTestScreen,SelectTestScreen, ExecuteTestScreen, TestFinishedScreen, DeleteTestScreen ) 
        
        for F in screens:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.show_frame(HomeScreen)
        
    def show_frame(self, container): #Coloca el frame delante de todo para mostrarlo
        frame = self.frames[container]
        frame.tkraise()
        
#Ahora empezamos con la transicion y cambio de pantallas

    def home_to_create(self):
        self.show_frame(AddTestScreen)
        
    def home_to_update(self):
        new_options = self.get_test_names()
        self.frames[UpdateTestScreen].options.update_options(new_options)
        self.show_frame(UpdateTestScreen)
        
    def home_to_select(self):
        new_options = self.get_test_names()
        self.frames[SelectTestScreen].options.update_options(new_options)
        self.show_frame(SelectTestScreen)
        
        
    def select_to_execute(self):
        self.selected_test = self.frames[SelectTestScreen].options.selected.get()
        self.get_test()
        self.show_frame(ExecuteTestScreen)
        
    def execute_to_finish(self):
        self.frames[TestFinishedScreen].results.set(f"{self.num_aciertos} / {self.num_questions}")
        self.num_aciertos = 0
        self.num_questions = 0
        self.show_frame(TestFinishedScreen)
        
    def home_to_delete(self):
        new_options = self.get_test_names()
        self.frames[DeleteTestScreen].options.update_options(new_options)
        self.show_frame(DeleteTestScreen)
        
        
#Aquie empiezan los metodos de las bases de datos

    def get_test_names(self):
        return self.controller.get_test_names()
    
    def add_test_questions(self, _test_name, _question_text, _question_choices, _correct_choice):
        self.controller.add_test_questions(_test_name, _question_text, _question_choices, _correct_choice)
        
    def get_test(self):
        if self.selected_test != "":
            _questions = self.controller.get_test_questions(self.selected_test)
            self.questions = iter(_questions)
            self.frames[ExecuteTestScreen].init_widgets(next(self.questions))
            
    def delete_test(self, _test_name):
        self.controller.delete_test(_test_name)
        
        
            