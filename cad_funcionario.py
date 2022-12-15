from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import model.model_funcionario as m_func
from tkcalendar import Calendar, DateEntry

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão deletar
co2 = "#918F2B"  # Cor botão fechar 
co3 = "#00E9CC"  # Cor botão inserir
co4 = "#FFCA18"  # Cor botão editar
co5 = "#F1864F"  # Cor botão pesquisar
co6 = "#3962F7"  # Cor botão limpar

class funcionario(Toplevel):
        # Popula a Table
    def view_command(self):
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
        like = self.txt_pesquisa.get()
        if(like == ""):
            messagebox.showinfo("Status", "Digite a consulta!")
        else:
            param = self.txt_pesquisa.get().strip()
            rows = m_func.search(param)
            self.tv.delete(*self.tv.get_children())
            for row in rows:
                self.tv.insert("", "end", values=row)
            self.limpar_dados()    
            self.bt_limpar.place(x=529, y=235)
            ...
    # END def search_command

    # Adiciona dados no DB
    def insert_command(self):
        param = self.txt_nome.get()
        result = m_func.search_name(param)
        if result:
            self.limpar_dados()
            self.bt_confirmar.place_forget()
            messagebox.showerror('Error', 'Inserir dados diferentes')
        else:
            if self.txt_nome.get().strip() == "" or self.txt_endereco.get().strip() == "" or self.txt_funcao.get().strip() == "":
                messagebox.showerror("Error", "Os campos com (*) não podem ser vazios!")
            else:    
                m_func.insert(self.txt_cpf.get(), self.txt_nome.get(), self.txt_endereco.get(), self.txt_email.get(), self.txt_telefone.get(), self.txt_data_nasc.get(), self.txt_funcao.get(), self.txt_disciplina.get())
                # Limpa os dados dos campos de texto
                self.limpar_dados()
                self.view_command()
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')
        ...        
    # END def insert_command

    # Exclui dados no DB
    def del_command(self):
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
        self.cpf = self.e_cpf.get()
        self.nome = self.e_nome.get()
        self.endereco = self.e_endereco.get()
        self.email = self.e_email.get()
        self.telefone = self.e_telefone.get()
        self.nascimento = self.e_data_nasc.get()
        self.funcao = self.e_funcao.get()
        self.disciplina = self.e_disciplina.get()

        self.valor_id = self.getSelectedRow()

        lista = [self.cpf, self.nome, self.endereco, self.email, self.telefone, self.nascimento, self.funcao, self.disciplina, self.valor_id]
        #VERIFICA SE OS CAMPOS ESTÃO VAZIOS
        if self.txt_nome.get().strip() == "" or self.txt_endereco.get().strip() == "" or self.txt_funcao.get().strip() == "":
            messagebox.showerror("Error", "Os campos com (*) não podem ser vazios!")
        else:
            m_func.update(lista)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')  
            # Limpa os dados dos campos de texto
            self.limpar_dados()
        self.bt_confirmar.place_forget()    
        self.view_command()
        ...
    # END def update_command                      

    # Pega os dados da Table e adiciona nos widgets
    def getSelectedRow(self):
        tv_dados = self.tv.focus()
        tv_dicionario = self.tv.item(tv_dados)
        tv_lista = tv_dicionario['values']

        valor_id = tv_lista[0]
        if valor_id == "":
            messagebox.showerror('Erro', 'Selecione um registro na tabela')
        else:    
            self.limpar_dados()                
            self.bt_confirmar.place(x=410, y=235)

            self.e_cpf.insert(0, tv_lista[1])
            self.e_nome.insert(0, tv_lista[2])
            self.e_endereco.insert(0, tv_lista[3])
            self.e_email.insert(0, tv_lista[4])
            self.e_telefone.insert(0, tv_lista[5])
            self.e_data_nasc.insert(0, tv_lista[6])
            self.e_funcao.insert(0, tv_lista[7])
            self.e_disciplina.insert(0, tv_lista[8]) 
        return valor_id
    # END def getSelectedRow
                     
    # Limpa os dados dos campos de texto
    def limpar_dados(self):
        self.e_cpf.delete(0, 'end')
        self.e_nome.delete(0, 'end')
        self.e_endereco.delete(0, 'end')
        self.e_email.delete(0, 'end')
        self.e_telefone.delete(0, 'end')
        self.e_data_nasc.delete(0, 'end')
        self.e_funcao.delete(0, 'end')
        self.e_disciplina.delete(0, 'end')            
        self.e_pesquisa.delete(0, 'end')
        ...
    # END def limpar_dados        

    def __init__(self, master: Tk):
        super().__init__(master=master)
        
        self.title("Cadastro de Funcionário")
        self.resizable(False, False)
        self.geometry("910x520+200+50")
        
        # OPÇÕES COMBOBOX
        lista_funcao = ["Professor(a)", "Secretário(a)", "Aux. Secretaria", "Diretor(a)", "Servente", "Ajudante"]
        lista_disciplina = ["Nenhuma", "Português", "Matemática"]

        # Criando variáveis que armazena texto inserido
        self.txt_cpf = StringVar()
        self.txt_nome = StringVar()
        self.txt_endereco = StringVar()
        self.txt_email = StringVar()
        self.txt_telefone = StringVar()
        self.txt_data_nasc = StringVar()
        self.txt_funcao = StringVar()
        self.txt_disciplina = StringVar()
        self.txt_pesquisa = StringVar()

        # Criando widgets raiz
        self.tela_principal = Frame(self, bg=co0)
        self.tela_principal.place(x=0, y=0, width=910, height=520)

        #SEPARADOR
        ttk.Separator(self.tela_principal, orient=HORIZONTAL).place(x=20, y=220,  width=870)

        # Criando Widgets...
        # Criação dos LABEL
        #self.lb_professor = Label(self.tela_principal, image=img_func, bg="#353535", bd=0)
        self.lb_titulo = Label(self.tela_principal, text="Cadastro de Funcionários", font=("Arial Black",14),bg=co0, fg="white")
        self.lb_cpf = Label(self.tela_principal, text='CPF: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_nome = Label(self.tela_principal, text='NOME*: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_endereco = Label(self.tela_principal, text='ENDEREÇO*: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_email = Label(self.tela_principal, text='EMAIL: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_telefone = Label(self.tela_principal, text='TELEFONE: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_data_nasc = Label(self.tela_principal, text='NASCIMENTO: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_funcao = Label(self.tela_principal, text='FUNÇÃO*: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.lb_disciplina = Label(self.tela_principal, text='DISCIPLINA: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_cpf = Entry(self.tela_principal, textvariable=self.txt_cpf, width=18, font=1)
        self.e_nome = Entry(self.tela_principal, textvariable=self.txt_nome, width=48, font=1)
        self.e_endereco = Entry(self.tela_principal, textvariable=self.txt_endereco, width=48, font=1)
        self.e_email = Entry(self.tela_principal, textvariable=self.txt_email, width=48, font=1)
        self.e_telefone = Entry(self.tela_principal, textvariable=self.txt_telefone, width=18, font=1)
        self.e_data_nasc = DateEntry(self.tela_principal, textvariable=self.txt_data_nasc, width=18, background='darkblue', foreground='white', borderwidth=2)
        self.e_funcao = ttk.Combobox(self.tela_principal, values=lista_funcao, textvariable=self.txt_funcao, width=16, font=1)
        self.e_disciplina = ttk.Combobox(self.tela_principal, values=lista_disciplina, textvariable=self.txt_disciplina, width=12,font=1)
        self.e_pesquisa = Entry(self.tela_principal, textvariable=self.txt_pesquisa, width=22, bg=co0, bd=0, fg="white", insertbackground="white", font=1)
        # Criação dos BUTTON
        self.bt_inserir = Button(self.tela_principal, command=self.insert_command, text="INSERIR",cursor="hand2", font='arial 10', bg=co3, fg="white", width=7)
        self.bt_deletar = Button(self.tela_principal, command=self.del_command, text="DELETAR", cursor="hand2", font='arial 10', bg=co1, fg="white", width=7)
        self.bt_editar = Button(self.tela_principal, command=self.getSelectedRow, text="EDITAR", cursor="hand2", font='arial 10', bg=co4, fg="white", width=7)
        self.bt_pesquisa = Button(self.tela_principal, command=self.search_command, text="CONSULTAR",cursor="hand2", font='arial 8', bg=co5, fg="white", width=10)
        self.bt_limpar = Button(self.tela_principal, command=self.view_command, text="LIMPAR",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        self.bt_confirmar = Button(self.tela_principal, command=self.update_command, text="OK",cursor="hand2", font='arial 10', bg=co6, fg="white", width=7)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "cpf", "nome", "endereco", "email", "telefone", "nascimento", "funcao", "disciplina"), show='headings')
        self.tv.place(x=15,y=280)
        # coluna
        self.tv.column('id', minwidth=0, width=35)
        self.tv.column('cpf', minwidth=0, width=75)
        self.tv.column('nome', minwidth=0, width=160)
        self.tv.column('endereco', minwidth=0, width=155)
        self.tv.column('email', minwidth=0, width=130)
        self.tv.column('telefone', minwidth=0, width=90)
        self.tv.column('nascimento', minwidth=0, width=82)
        self.tv.column('funcao', minwidth=0, width=75)
        self.tv.column('disciplina', minwidth=0, width=80)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('cpf', text='CPF')
        self.tv.heading('nome', text='NOME')
        self.tv.heading('endereco', text='ENDEREÇO')
        self.tv.heading('email', text='EMAIL')
        self.tv.heading('telefone', text='TELEFONE')
        self.tv.heading('nascimento', text='NASCIMENTO')
        self.tv.heading('funcao', text='FUNCAO')
        self.tv.heading('disciplina', text='DISCIPLINA')        
        # Associando Widgets na janela...
        # Associação dos LABEL
        #self.lb_professor.place(x=680, y=60)
        self.lb_titulo.place(x=610, y=30)
        self.lb_cpf.place(x=20, y=30)
        self.lb_nome.place(x=20, y=60)
        self.lb_endereco.place(x=20, y=90)
        self.lb_email.place(x=20, y=120)
        self.lb_telefone.place(x=20, y=150)
        self.lb_data_nasc.place(x=323, y=150)
        self.lb_funcao.place(x=20, y=180)
        self.lb_disciplina.place(x=323, y=180)
         # Associação dos CAMPOS DE TEXTOS
        self.e_cpf.place(x=155, y=35)
        self.e_nome.place(x=155, y=65)
        self.e_endereco.place(x=155, y=95)
        self.e_email.place(x=155, y=125)
        self.e_telefone.place(x=155, y=155)
        self.e_data_nasc.place(x=460, y=155)
        self.e_funcao.place(x=155, y=185)
        self.e_disciplina.place(x=460, y=185)
        self.e_pesquisa.place(x=689, y=240)
        ttk.Separator(self.tela_principal, orient=HORIZONTAL).place(x=688,y=260,  width=200)
        # Associação dos BUTTON
        self.bt_inserir.place(x=155, y=235)
        self.bt_deletar.place(x=240, y=235)
        self.bt_editar.place(x=325, y=235)
        self.bt_pesquisa.place(x=613, y=236)
        self.view_command()
        self.mainloop()
