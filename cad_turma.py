from tkinter import*
from tkinter import ttk


################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#918F2B"  # Cor botão fechar 

class Turma:
    # INTERFACE GRAFICA TURMAS
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Lista de Turmas")
        root.resizable(False, False)
        # ========== Centralizar Janela ==========
        largura = 400
        altura = 380
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        # OPÇÕES COMBOBOX
        lista_turma = ["Primeiro Ano", "Segundo Ano", "Terceiro Ano", "Quarto Ano", "Quinto Ano", "Sexto Ano"]

        # Criando widgets raiz
        self.tela_principal = Frame(root, bg=co0)
        self.tela_principal.place(x=0, y=0, width=400, height=380)

        # Criando Widgets...
        # Criação dos LABEL
        lb_turma = Label(self.tela_principal, text='TURMAS: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_capacidade = Label(self.tela_principal, text='CAPACIDADE: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_vagaL = Label(self.tela_principal, text='VAGAS LIVRES: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_turma = ttk.Combobox(self.tela_principal, values=lista_turma, width=16, font=1)
        self.e_capacidade = Entry(self.tela_principal, width=4, font=1)
        self.e_vagaL = Entry(self.tela_principal, width=4, font=1)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "turma"), show='headings')
        self.tv.place(x=22,y=115)
        # coluna
        self.tv.column('id', minwidth=0, width=55)
        self.tv.column('turma', minwidth=0, width=300)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('turma', text='TURMA')
        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_turma.place(x=52, y=35)
        lb_capacidade.place(x=15, y=65)
        lb_vagaL.place(x=198, y=65)
        # Associação dos CAMPOS DE TEXTOS
        self.e_turma.place(x=142, y=35)
        self.e_capacidade.place(x=142, y=70)
        self.e_vagaL.place(x=340, y=70)

        root.mainloop()
      