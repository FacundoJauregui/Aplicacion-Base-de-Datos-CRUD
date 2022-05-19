import tkinter as tk
from styles import style
from components.MainMenu import MainMenu

class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = style.BACKGROUND
        )
        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "MENU TEST",
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