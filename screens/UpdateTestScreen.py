import tkinter as tk   
from styles import style
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption

class UpdateTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = style.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.question_text = tk.StringVar(self)
        self.question_choices = tk.StringVar(self)
        self.question_choice = tk.IntVar(self, 0)
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text = "Seleccione el test a modificar",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            **style.PACK
        )
        
        self.options = SelectOption(
            self,
            self.manager,
            self.option_list
        )
        
        self.options.pack(
            **style.PACK
        )
        