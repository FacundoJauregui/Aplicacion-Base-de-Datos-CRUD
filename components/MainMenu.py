import tkinter as tk
from styles import style

class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.configure(
            background = style.BACKGROUND
        )
        self.manager = manager
        self.init_widgets()
        
    def init_widgets(self):
        tk.Button(
            self,
            text = "Crear Test",
            command = lambda: self.manager.home_to_create(),
            **style.STYLE,
            relief = tk.RAISED,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            **style.PACK
        )
        
        tk.Button(
            self,
            text = "Editar Test",
            command = lambda: print("Has hecho click en Editar Test"),
            **style.STYLE,
            relief = tk.RAISED,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            **style.PACK
        )
        
        tk.Button(
            self,
            text = "Eliminar Test",
            command = lambda: print("Has hecho click en Elimnar Test"),
            **style.STYLE,
            relief = tk.RAISED,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            **style.PACK
        )