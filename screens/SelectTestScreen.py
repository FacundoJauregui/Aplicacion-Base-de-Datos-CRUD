import tkinter as tk   
from styles import style
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption

class SelectTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = style.BACKGROUND)
        self.option_list = self.manager.get_test_names()
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text = "Seleccione el test que quieras realizar",
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
        
        tk.Button(
            self,
            text = "Empezar Test",
            relief = tk.RAISED,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,
            **style.STYLE,
            command = self.manager.select_to_execute()
        ).pack(**style.PACK)
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **style.PACK
        )
        