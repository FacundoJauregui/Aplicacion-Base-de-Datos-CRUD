import tkinter as tk
from styles import style
from components.MainMenu import MainMenu

class TestFinishedScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.results = tk.StringVar(self)
        
        self.configure(
            background = style.BACKGROUND
        )
        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "El examen a finalizado!",
            justify = tk.CENTER,
            **style.STYLE #Desempaquetamos el diccionario desde el modulo para usar STYLE
        ).pack(
            **style.PACK
        )
        
        tk.Label(
            self,
            textvariable = self.results,
            justify = tk.CENTER,
            **style.STYLE #Desempaquetamos el diccionario desde el modulo para usar STYLE
        ).pack(
            **style.PACK
        )

        MainMenu(
            self,
            self.manager
        ).pack(
            **style.PACK2
        )