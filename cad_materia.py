from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import model.model_materia as m_mat 

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#969696"  # Cor botão fechar
co3 = "#00E9CC"  # Cor botão inserir 


class Materia:
    # INTERFACE GRAFICA MATERIA
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Registro de Matérias")
        root.resizable(False, False)
        # ========== Centralizar Janela ==========
        largura = 400
        altura = 390
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
        self.tela_principal.place(x=0, y=0, width=400, height=390)

        # Criando Widgets...
        # Criação dos LABEL
        lb_titulo = Label(self.tela_principal, text="Registro de Matérias", font=("Arial Black",14),bg=co0, fg="white")
        lb_materia = Label(self.tela_principal, text='MATÉRIA: ', font =('Arial Black', 12), bg=co0, fg="white")
        # Criação dos CAMPOS DE TEXTOS
        self.e_materia = Entry(self.tela_principal, width=21, font=1)
        # Criação dos BUTTON
        self.bt_inserir = Button(self.tela_principal, command=self.insert_command, text="INSERIR",cursor="hand2", font='arial 10', bg=co3, fg="white", width=8)
        self.bt_deletar = Button(self.tela_principal, command=self.del_command, text="DELETAR",cursor="hand2", font='arial 10', bg=co1, fg="white", width=8)
        self.bt_fechar = Button(self.tela_principal, command=self._close_window, text="FECHAR",cursor="hand2", font='arial 10', bg=co2, fg="white", width=8)
        # Criação da TABLE
        self.tv = ttk.Treeview(self.tela_principal, columns=("id", "materia"), show='headings')
        self.tv.place(x=20,y=105)
        # coluna
        self.tv.column('id', minwidth=0, width=55)
        self.tv.column('materia', minwidth=0, width=300)
        # cabeçalho
        self.tv.heading('id', text='ID')
        self.tv.heading('materia', text='MATERIA')

        # Associando Widgets na janela...
        # Associação dos LABEL
        lb_titulo.place(x=80, y=15)
        lb_materia.place(x=20, y=65)
        # Associação dos CAMPOS DE TEXTOS
        self.e_materia.place(x=120, y=65)
        # Associação dos BUTTON
        self.bt_inserir.place(x=20, y=345)
        self.bt_deletar.place(x=110, y=345)
        self.bt_fechar.place(x=305, y=345)
        self.view_command()
        root.mainloop()

    def _close_window(self):
        """
        -> Fecha a janela
        """
        self.window.destroy()

    def insert_command(self):
        """
        -> Cria um novo cadastro de funcionario na tabela.
        """
        if self.e_materia.get().strip() == "":
            messagebox.showerror("Error", "Os campos com (*) não podem ser vazios!")
        else:
            materia = self.e_materia.get()
            lista = [materia]
            m_mat.insert(lista)
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')
            # Limpa os dados dos campos de texto
            self.e_materia.delete(0, 'end')
            self.view_command()

    def view_command(self):
        """
        -> Mostra uma listagem na tabela de funcionario.
        :return: Retorna dados funcionario.
        """
        rows = m_mat.view()
        self.tv.delete(*self.tv.get_children())
        for row in rows:
            self.tv.insert("", "end", values=row)

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
                m_mat.delete(valor_id)
                messagebox.showinfo('Sucesso', 'Os dados foram removidos com sucesso')
                # Limpa os dados dos campos de texto
                self.e_materia.delete(0, 'end')
            self.view_command()
        except IndexError:
            messagebox.showerror('Error', 'Selecione um registro na tabela')               
    
        