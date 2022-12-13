from tkinter import*

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#918F2B"  # Cor botão fechar 


class menu_window:

    def call_funcionario():
        func = open('/funcionario.py')
        return func

    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.resizable(False, False)
        self.root.geometry("1280x720+0+0")

        # ==========Frames Principal==========
        menu_frame = Frame(self.root, bg=co0)
        menu_frame.place(x=0, y=0, width=1280, height=720)

        barra_menu = Menu(menu_frame)
        menu_cadastro = Menu(barra_menu, tearoff=0)
        menu_cadastro.add_command(label="Aluno")
        menu_cadastro.add_command(label="Turma")
        menu_cadastro.add_command(label="Funcionário", command=self.call_funcionario)
        menu_cadastro.add_separator()
        menu_cadastro.add_command(label="Fechar", command=self.root.quit)
        barra_menu.add_cascade(label="Cadastro", menu=menu_cadastro)

        root.config(menu=barra_menu)

root = Tk()
obj = menu_window(root)
root.mainloop()
