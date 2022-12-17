from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import model.model_aluno as m_func
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
        lb_telefone = Label(self.tela_principal, text='TELEFONE: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_cep = Label(self.tela_principal, text='CEP: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_data_nasc = Label(self.tela_principal, text='NASCIMENTO*: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_sangue = Label(self.tela_principal, text='TIPO SANGUÍNEO: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_nome = Entry(self.tela_principal, width=40, font=1)
        self.e_endereco = Entry(self.tela_principal, width=40, font=1)
        self.e_telefone = Entry(self.tela_principal, width=16, font=1)
        self.e_cep = Entry(self.tela_principal, width=17, font=1)
        self.e_data_nasc = DateEntry(self.tela_principal, width=14, background='darkblue', foreground='white', borderwidth=2, font=1)
        self.e_sangue = ttk.Combobox(self.tela_principal, values=lista_sangue, width=6, font=1)
        self.e_pesquisa = Entry(self.tela_principal, width=22, bg=co0, bd=0, fg="white", insertbackground="white", font=1)
        # Criação dos BUTTON
        self.bt_inserir = Button(self.tela_principal, command=self.insert_command, text="INSERIR",cursor="hand2", font='arial 10', bg=co3, fg="white", width=7)
        self.bt_deletar = Button(self.tela_principal, command=self.del_command, text="DELETAR", cursor="hand2", font='arial 10', bg=co1, fg="white", width=7)
        self.bt_editar = Button(self.tela_principal, command=self.getSelectedRow, text="EDITAR", cursor="hand2", font='arial 10', bg=co4, fg="white", width=7)
        self.bt_confirmar = Button(self.tela_principal, command=self.update_command, text="OK",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        self.bt_pesquisa = Button(self.tela_principal, command=self.search_command, text="CONSULTAR",cursor="hand2", font='arial 8', bg=co5, fg="white", width=10)
        self.bt_limpar = Button(self.tela_principal, command=self.view_command, text="LIMPAR",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "nome", "endereco", "telefone", "cep", "nascimento", "sangue"), show='headings')
        self.tv.place(x=15,y=230)
        # coluna
        self.tv.column('id', minwidth=0, width=35)
        self.tv.column('nome', minwidth=0, width=160)
        self.tv.column('endereco', minwidth=0, width=155)
        self.tv.column('telefone', minwidth=0, width=92)
        self.tv.column('cep', minwidth=0, width=90)
        self.tv.column('nascimento', minwidth=0, width=90)
        self.tv.column('sangue', minwidth=0, width=85)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('nome', text='NOME')
        self.tv.heading('endereco', text='ENDEREÇO')
        self.tv.heading('telefone', text='TELEFONE')
        self.tv.heading('cep', text='CEP')
        self.tv.heading('nascimento', text='NASCIMENTO')
        self.tv.heading('sangue', text='SANGUE')    
        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_nome.place(x=20, y=30)
        lb_endereco.place(x=20, y=60)
        lb_telefone.place(x=20, y=100)
        lb_cep.place(x=350, y=100)
        lb_data_nasc.place(x=20, y=135)
        lb_sangue.place(x=340, y=135)
        # Associação dos CAMPOS DE TEXTOS
        self.e_nome.place(x=160, y=30)
        self.e_endereco.place(x=160, y=65)
        self.e_telefone.place(x=160, y=100)
        self.e_cep.place(x=411, y=100)
        self.e_data_nasc.place(x=160, y=135)
        self.e_sangue.place(x=513, y=135)
        self.e_pesquisa.place(x=235, y=192)
        self.e_pesquisa.focus()
        ttk.Separator(self.tela_principal, orient=HORIZONTAL).place(x=235,y=215,  width=220)
        # Associação dos BUTTON
        self.bt_inserir.place(x=630, y=30)
        self.bt_deletar.place(x=630, y=75)
        self.bt_editar.place(x=630, y=115)
        self.bt_pesquisa.place(x=158, y=192)
        self.view_command()
        root.mainloop()

    # Adiciona dados no DB
    def insert_command(self):
        """
        -> Cria um novo cadastro de funcionario na tabela.
        :return: Sem retorno.
        """
        param = self.e_nome.get()
        result = m_func.search_name(param)
        if result:
            self.limpar_dados()
            self.bt_confirmar.place_forget()
            messagebox.showerror('Error', 'Inserir dados diferentes')
        else:
            if self.e_nome.get().strip() == "" or self.e_endereco.get().strip() == "" or self.e_data_nasc.get().strip() == "":
                messagebox.showerror("Error", "Os campos com (*) não podem ser vazios!")
            else:    
                m_func.insert(self.e_nome.get(), self.e_endereco.get(), self.e_telefone.get(), self.e_cep.get(), self.e_data_nasc.get(), self.e_sangue.get())
                # Limpa os dados dos campos de texto
                self.limpar_dados()
                self.view_command()
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')
        ...        
    # END def insert_command

    # Popula a Table
    def view_command(self):
        """
        -> Mostra uma listagem na tabela de funcionario.
        :return: Retorna dados funcionario.
        """
        self.bt_limpar.place_forget()
        self.bt_confirmar.place_forget()
        rows = m_func.view()
        self.tv.delete(*self.tv.get_children())
        for row in rows:
            self.tv.insert("", "end", values=row)
        self.limpar_dados()
        ...   
    # END def view_command

    # Pesquisa na Table
    def search_command(self,event=None):
        """
        -> Faz um busca pelos pelos dados do funcionario solicitado pelo nome.
        :param nome: Passa o nome do funcionario a ser solicitado.
        :return: Retorna uma lista com os dados do funcionario selecionado.
        """
        like = self.e_pesquisa.get()
        if(like == ""):
            messagebox.showinfo("Status", "Digite a consulta!")
        else:
            param = self.e_pesquisa.get().strip()
            rows = m_func.search(param)
            self.tv.delete(*self.tv.get_children())
            for row in rows:
                self.tv.insert("", "end", values=row)
            self.limpar_dados()    
            self.bt_limpar.place(x=465, y=189)
            ...
    # END def search_command

    # Exclui dados no DB
    def del_command(self):
        """
        -> Exclui o cadastro do funcionario solicitado.
        :param id: Id do funcionario solicitado.
        """
        try:
            tv_dados = self.tv.focus()
            tv_dicionario = self.tv.item(tv_dados)
            tv_lista = tv_dicionario['values']
            valor_id = [tv_lista[0]]
            result = messagebox.askquestion('Remover dados?', 'Tem certeza que deseja remover dados?')
            if result == 'yes':
                m_func.delete(valor_id)
                messagebox.showinfo('Sucesso', 'Os dados foram removidos com sucesso')
                # Limpa os dados dos campos de texto
                self.limpar_dados()
            self.view_command()
        except IndexError:
            messagebox.showerror('Error', 'Selecione um registro na tabela')
        ...
    # END def del_command

    # Atualiza dados no DB    
    def update_command(self):
        nome = self.e_nome.get()
        endereco = self.e_endereco.get()
        telefone = self.e_telefone.get()
        cep = self.e_cep.get()
        nascimento = self.e_data_nasc.get()
        sangue = self.e_sangue.get()

        valor_id = self.getSelectedRow()
        lista = [nome, endereco, telefone, cep, nascimento, sangue, valor_id]
        #VERIFICA SE OS CAMPOS ESTÃO VAZIOS
        if self.e_nome.get().strip() == "" or self.e_endereco.get().strip() == "" or self.e_data_nasc.get().strip() == "":
            messagebox.showerror("Error", "Os campos com (*) não podem ser vazios!")
        else:
            m_func.update(lista)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')  
            # Limpa os dados dos campos de texto
            self.limpar_dados()
        self.bt_confirmar.place_forget()   
        self.bt_limpar.place_forget()   
        self.view_command()
        ...
    # END def update_command 
    
    # Pega os dados da Table e adiciona nos widgets
    def getSelectedRow(self):
        """
        -> Seleciona um dado na tabela e popula os campos.
        :return: valor_id.
        """
        tv_dados = self.tv.focus()
        tv_dicionario = self.tv.item(tv_dados)
        tv_lista = tv_dicionario['values']

        if tv_lista == "":
            valor_id = None
            messagebox.showerror('Erro', 'Selecione um registro na tabela')
        else:    
            valor_id = tv_lista[0]
            self.limpar_dados()                
            self.bt_confirmar.place(x=630, y=155)
            self.bt_limpar.place(x=465, y=189)

            self.e_nome.insert(0, tv_lista[1])
            self.e_endereco.insert(0, tv_lista[2])
            self.e_telefone.insert(0, tv_lista[3])
            self.e_cep.insert(0, tv_lista[4])
            self.e_data_nasc.insert(0, tv_lista[5])
            self.e_sangue.insert(0, tv_lista[6])
        return valor_id
    # END def getSelectedRow

    # Limpa os dados dos campos de texto
    def limpar_dados(self):
        """
        -> Limpa os dados nos campos de texto.
        :return: Sem retorno.
        """
        self.e_nome.delete(0, 'end')
        self.e_endereco.delete(0, 'end')
        self.e_telefone.delete(0, 'end')
        self.e_cep.delete(0, 'end')
        self.e_data_nasc.delete(0, 'end')
        self.e_sangue.delete(0, 'end')            
        self.e_pesquisa.delete(0, 'end')
        ...
    # END def limpar_dados
