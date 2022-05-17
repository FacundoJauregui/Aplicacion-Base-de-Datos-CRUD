import tkinter as tk
from styles import style

class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "Crea o realiza tests",
            justify = tk.CENTER,
            **style.STYLE #Desempaquetamos el diccionario desde el modulo para usar STYLE
        ).pack(
            **style.PACK
        )
