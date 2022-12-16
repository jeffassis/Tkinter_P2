from tkinter import*

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
        largura = 910
        altura = 520
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) 

        # Criando widgets raiz
        self.tela_principal = Frame(root, bg=co0)
        self.tela_principal.place(x=0, y=0, width=910, height=520)

        # Criando Widgets...
        # Criação dos LABEL
        lb_nome = Label(self.tela_principal, text='NOME*: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_endereco = Label(self.tela_principal, text='ENDEREÇO*: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_cep = Label(self.tela_principal, text='CEP: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_telefone = Label(self.tela_principal, text='TELEFONE: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_data_nasc = Label(self.tela_principal, text='NASCIMENTO: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_sangue = Label(self.tela_principal, text='TIPO SANGUENEO: ', font =('Arial Black', 12), bg=co0, fg="white")

        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_nome.place(x=20, y=30)
        lb_endereco.place(x=20, y=60)
        lb_cep.place(x=20, y=90)
        lb_telefone.place(x=20, y=120)
        lb_data_nasc.place(x=20, y=150)
        lb_sangue.place(x=20, y=180)


        root.mainloop()

