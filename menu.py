from tkinter import*
from cad_funcionario import *

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#918F2B"  # Cor botão fechar 

class menu_window:
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Menu Principal")
        root.resizable(False, False)
        # ========== Centralizar Janela ==========
        largura = 900
        altura = 500
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))



        # ========== MenuBar ==========
        barra_menu = Menu(root)        
        root.config(menu=barra_menu)
        menu_item = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Cadastro", menu=menu_item)
        menu_item.add_command(label='Funcionário', command=self.call_funcionario)
        menu_item.add_separator()
        menu_item.add_command(label='Sair', command=root.quit)

        # ==========Frames Principal==========
        menu_frame = Frame(root, bg=co0)
        menu_frame.place(x=0, y=0, width=900, height=500)

        root.mainloop()    
        

    def call_funcionario(self):
        funcionario()
        
