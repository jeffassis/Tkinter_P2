from tkinter import*
from cad_funcionario import funcionario

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#918F2B"  # Cor botão fechar 

class menu_window:
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Menu")
        root.resizable(False, False)
        
        barra_menu = Menu(root)        
        root.config(menu=barra_menu)
        menu_item = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Cadastro", menu=menu_item)
        menu_item.add_command(label='Funcionário', command=self.call_funcionario)

        root.mainloop()    
        

    def call_funcionario(self):
        funcionario(master=self.window)
