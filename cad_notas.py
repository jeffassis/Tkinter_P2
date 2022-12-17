from tkinter import*
from tkinter import ttk

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#A31319"  # Cor botão salvar
co2 = "#FFCA18"  # Cor botão editar 
co3 = "#00E9CC"  # Cor botão inserir
co4 = "#B00857"  # Cor botão deletar
co5 = "#969696"  # Cor botão fechar

class Notas:
    # INTERFACE GRAFICA NOTAS
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Lançamento de Notas")
        root.resizable(False, False)
        # ========== Centralizar Janela ==========
        largura = 520
        altura = 418
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        # OPÇÕES COMBOBOX
        lista_bimestre = ["Primeiro Ano", "Segundo Ano", "Terceiro Ano", "Quarto Ano", "Quinto Ano", "Sexto Ano"]

        # Criando widgets raiz
        self.tela_principal = Frame(root, bg=co0)
        self.tela_principal.place(x=0, y=0, width=520, height=418)

        # Criando Widgets...
        # Criação dos LABEL
        lb_aluno = Label(self.tela_principal, text='Aluno: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_bimestre = Label(self.tela_principal, text='Bimestre: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_materia = Label(self.tela_principal, text='Materia: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_nota = Label(self.tela_principal, text='NOTA: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_aluno = Entry(self.tela_principal, width=18, font=1)
        self.e_bimestre = ttk.Combobox(self.tela_principal, values=lista_bimestre, width=26)
        self.e_materia = ttk.Combobox(self.tela_principal, width=26)
        self.e_nota = Entry(self.tela_principal, width=5, font=1)
        # Criação dos BUTTON
        self.bt_lancar = Button(self.tela_principal, command=self, text="LANÇAR",cursor="hand2", font='arial 9', bg=co1, fg="white", width=7)
        self.bt_salvar = Button(self.tela_principal, command=self, text="SALVAR",cursor="hand2", font='arial 9', bg=co3, fg="white", width=8)
        self.bt_editar = Button(self.tela_principal, command=self, text="EDITAR",cursor="hand2", font='arial 9', bg=co2, fg="white", width=8)
        self.bt_deletar = Button(self.tela_principal, command=self, text="DELETAR",cursor="hand2", font='arial 9', bg=co4, fg="white", width=8)
        self.bt_fechar = Button(self.tela_principal, command=self._close_window, text="FECHAR",cursor="hand2", font='arial 9', bg=co5, fg="white", width=8)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "aluno", "materia", "bimestre", "nota"), show='headings')
        self.tv.place(x=25,y=145)
        # coluna
        self.tv.column('id', minwidth=0, width=50)
        self.tv.column('aluno', minwidth=0, width=160)
        self.tv.column('materia', minwidth=0, width=100)
        self.tv.column('bimestre', minwidth=0, width=100)
        self.tv.column('nota', minwidth=0, width=60)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('aluno', text='ALUNO')
        self.tv.heading('materia', text='MATERIA')
        self.tv.heading('bimestre', text='BIMESTRE')
        self.tv.heading('nota', text='NOTA')
        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_aluno.place(x=45, y=23)
        lb_bimestre.place(x=18, y=58)
        lb_materia.place(x=28, y=93)
        lb_nota.place(x=325, y=23)
        # Associação dos CAMPOS DE TEXTOS
        self.e_aluno.place(x=115, y=25)
        self.e_bimestre.place(x=115, y=63)
        self.e_materia.place(x=115, y=95)
        self.e_nota.place(x=390, y=25)
        # Associação dos BUTTON
        self.bt_lancar.place(x=391, y=60)       
        self.bt_salvar.place(x=25, y=382)       
        self.bt_editar.place(x=100, y=382)       
        self.bt_deletar.place(x=175, y=382)       
        self.bt_fechar.place(x=432, y=382)       

        root.mainloop()

    def _close_window(self):

        """
        -> Fecha a janela
        """
        self.window.destroy()
        
           