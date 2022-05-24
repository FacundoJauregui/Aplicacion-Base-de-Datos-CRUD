import tkinter as tk   
import tkinter.messagebox
from styles import style
from components.MainMenu import MainMenu
from components.SelectOption import SelectOption


class DeleteTestScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = style.BACKGROUND)
        self.option_list = self.manager.get_test_names() 
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            text = "Seleccione el test que quieras eliminar",
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
            text = "Eliminar Test",
            relief = tk.RAISED,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,
            **style.STYLE,
            command = lambda: self.delete_test()
        ).pack(**style.PACK)
        
        MainMenu(
            self,
            self.manager
        ).pack(
            **style.PACK
        )
        
    def delete_test(self):
        _test_name = self.options.selected.get()
        tk.messagebox.showinfo(
            title = "WARNING",
            message = f"Seguro que quieres eliminar {_test_name}"
        )
        
        self.manager.delete_test(self.options.selected.get())
        
        tk.messagebox.showinfo(
            title = "WARNING",
            message = f"El test {_test_name} a sido eliminado"
        )
        test_names = self.manager.get_test_names()
        self.options.update_options(test_names)