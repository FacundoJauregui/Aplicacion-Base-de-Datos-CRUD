import tkinter as tk
from Controller import Controller
from screens.HomeScreen import HomeScreen
from screens.AddTestScreen import AddTestScreen
from screens.UpdateTestScreen import UpdateTestScreen
from styles import style


#Configuracion del manager que se va a encargar de posicionar el frame que queramos
class Manager(tk.Tk):
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.title("Examenes de Programacion")
        self.controller = Controller()
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
        screens = (HomeScreen, AddTestScreen, UpdateTestScreen, ) 
        
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
        
#Aquie empiezan los metodos de las bases de datos

    def get_test_names(self):
        return self.controller.get_test_names()
    
    def add_test_questions(self, _test_name, _question_text, _question_choices, _correct_choice):
        self.controller.add_test_questions(_test_name, _question_text, _question_choices, _correct_choice)