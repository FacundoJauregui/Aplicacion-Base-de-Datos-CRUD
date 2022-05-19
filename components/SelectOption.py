import tkinter as tk
from styles import style

#Menu desplegable que permite seleccionar que test queremos hacer
class SelectOption(tk.Frame):
    def __init__(self, parent, manager, option_list):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = style.BACKGROUND)
        self.option_list = option_list
        self.selected = tk.StringVar(self)
        self.init_widgets()
        
    def init_widgets(self):
        self.options = tk.OptionMenu(
            self,
            self.selected,
            *self.option_list
        )
        
        self.options.config(**style.STYLE)
        self.options["menu"].config(**style.STYLE)
        self.options.pack(
            **style.PACK
        )
        
    def update_options(self, new_options):
        menu = self.options["menu"]
        menu.delete(0, "end") #Borramos el desplegable para que no tenga ninguna opcion
        
        for option in new_options: #Y iteramos el nuevo menu desplegable aniadiendo opcion por opcion
            menu.add_command(
                Label = option,
                command = lambda value = option: self.selected.set(value)
            )