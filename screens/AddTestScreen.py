import tkinter as tk
import tkinter.messagebox
from sqlite3 import ProgrammingError
from styles import style
from components.MainMenu import MainMenu

class AddTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.manager = manager
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text = "Introduce el nombre del nuevo test",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            **style.PACK
        )
        
        self.test_entry = tk.Entry(
            self,
            justify = tk.CENTER,
            **style.STYLE
        )
        
        self.test_entry.pack(
            **style.PACK
        )
        self.test_entry.bind("<Return>", self.add_test)
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **style.PACK
        )    
    def add_test(self, event):
        test_name = self.test_entry.get()
        if test_name == "":
            tk.messagebox.showinfo(
                title = "ERROR",
                message = "El nombre del test no puede estar vacio"
            )
        else:
            try:
                self.manager.controller.empty_test(test_name)
                tk.messagebox.showinfo(
                title = "SUCCESS",
                message = f"El test {test_name} a sido creado"
            )
            except ProgrammingError:
                tk.messagebox.showinfo(
                title = "ERROR",
                message = f"El test {test_name} ya existe"
            )
            finally:
                print(test_name)