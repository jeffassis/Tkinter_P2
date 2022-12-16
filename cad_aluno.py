from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão deletar
co2 = "#918F2B"  # Cor botão fechar 
co3 = "#00E9CC"  # Cor botão inserir
co4 = "#FFCA18"  # Cor botão editar
co5 = "#F1864F"  # Cor botão pesquisar
co6 = "#3962F7"  # Cor botão limpar

class Aluno:
    def __init__(self):
        self.window = Tk()
        root = self.window        
        root.title("Cadastro de Aluno")
        root.resizable(False, False)
        # ========== Centralizar Janela ==========
        largura = 740
        altura = 480
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        # OPÇÕES COMBOBOX
        lista_sangue = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        # Criando widgets raiz
        self.tela_principal = Frame(root, bg=co0)
        self.tela_principal.place(x=0, y=0, width=740, height=480)

        # Criando Widgets...
        # Criação dos LABEL
        lb_nome = Label(self.tela_principal, text='NOME*: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_endereco = Label(self.tela_principal, text='ENDEREÇO*: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_cep = Label(self.tela_principal, text='CEP: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_telefone = Label(self.tela_principal, text='TELEFONE: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_data_nasc = Label(self.tela_principal, text='NASCIMENTO: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_sangue = Label(self.tela_principal, text='TIPO SANGUENEO: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_nome = Entry(self.tela_principal, width=48, font=1)
        self.e_endereco = Entry(self.tela_principal, width=48, font=1)
        self.e_cep = Entry(self.tela_principal, width=48, font=1)
        self.e_telefone = Entry(self.tela_principal, width=48, font=1)
        self.e_data_nasc = DateEntry(self.tela_principal, width=16, background='darkblue', foreground='white', borderwidth=2, font=1)
        self.e_sangue = ttk.Combobox(self.tela_principal, values=lista_sangue, width=6, font=1)
        self.e_pesquisa = Entry(self.tela_principal, width=22, bg=co0, bd=0, fg="white", insertbackground="white", font=1)
        # Criação dos BUTTON
        self.bt_inserir = Button(self.tela_principal, command=self, text="INSERIR",cursor="hand2", font='arial 10', bg=co3, fg="white", width=7)
        self.bt_deletar = Button(self.tela_principal, command=self, text="DELETAR", cursor="hand2", font='arial 10', bg=co1, fg="white", width=7)
        self.bt_editar = Button(self.tela_principal, command=self, text="EDITAR", cursor="hand2", font='arial 10', bg=co4, fg="white", width=7)
        self.bt_confirmar = Button(self.tela_principal, command=self, text="OK",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        self.bt_pesquisa = Button(self.tela_principal, command=self, text="CONSULTAR",cursor="hand2", font='arial 8', bg=co5, fg="white", width=10)
        self.bt_limpar = Button(self.tela_principal, command=self, text="LIMPAR",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "nome", "endereco", "cep", "telefone", "nascimento", "sangue"), show='headings')
        self.tv.place(x=15,y=230)
        # coluna
        self.tv.column('id', minwidth=0, width=35)
        self.tv.column('nome', minwidth=0, width=160)
        self.tv.column('endereco', minwidth=0, width=155)
        self.tv.column('cep', minwidth=0, width=92)
        self.tv.column('telefone', minwidth=0, width=90)
        self.tv.column('nascimento', minwidth=0, width=90)
        self.tv.column('sangue', minwidth=0, width=85)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('nome', text='NOME')
        self.tv.heading('endereco', text='ENDEREÇO')
        self.tv.heading('cep', text='CEP')
        self.tv.heading('telefone', text='TELEFONE')
        self.tv.heading('nascimento', text='NASCIMENTO')
        self.tv.heading('sangue', text='SANGUE')    

        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_nome.place(x=20, y=30)
        lb_endereco.place(x=20, y=60)
        lb_cep.place(x=20, y=90)
        lb_telefone.place(x=20, y=120)
        lb_data_nasc.place(x=20, y=150)
        lb_sangue.place(x=340, y=150)
        # Associação dos CAMPOS DE TEXTOS
        self.e_nome.place(x=155, y=35)
        self.e_endereco.place(x=155, y=65)
        self.e_cep.place(x=155, y=95)
        self.e_telefone.place(x=155, y=125)
        self.e_data_nasc.place(x=155, y=155)
        self.e_sangue.place(x=515, y=155)
        self.e_pesquisa.place(x=235, y=192)
        self.e_pesquisa.focus()
        ttk.Separator(self.tela_principal, orient=HORIZONTAL).place(x=235,y=212,  width=200)
        # Associação dos BUTTON
        self.bt_inserir.place(x=630, y=35)
        self.bt_deletar.place(x=630, y=75)
        self.bt_editar.place(x=630, y=115)
        self.bt_confirmar.place(x=630, y=155)
        self.bt_pesquisa.place(x=155, y=192)
        self.bt_limpar.place(x=440, y=189)

        root.mainloop()
