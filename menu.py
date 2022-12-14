from tkinter import*
from tkinter import messagebox
from cad_aluno import Aluno
from cad_funcionario import Funcionario
from cad_materia import Materia
from cad_turma import Turma
from cad_notas import Notas

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
        menu_cad = Menu(barra_menu, tearoff=0)
        menu_matricula = Menu(barra_menu, tearoff=0)
        menu_notas = Menu(barra_menu, tearoff=0)
        menu_turma = Menu(barra_menu, tearoff=0)
        menu_sobre = Menu(barra_menu, tearoff=0)
        # ========== CADASTRO ==========
        barra_menu.add_cascade(label="Cadastro", menu=menu_cad)
        menu_cad.add_command(label='Funcionário', command=self._call_funcionario)
        menu_cad.add_command(label='Aluno', command=self._call_aluno)
        menu_cad.add_separator()
        menu_cad.add_command(label='Sair', command=self.window.destroy)
        # ========== MATRICULA ==========
        barra_menu.add_cascade(label="Matriculas", menu=menu_matricula)
        # ========== LANCAMENTO DE NOTAS ==========
        barra_menu.add_cascade(label="Notas", menu=menu_notas)
        menu_notas.add_command(label='Lançamento de Notas', command=self._call_notas)
        menu_notas.add_separator()
        menu_notas.add_command(label='Consulta de Média', command=self)
        menu_notas.add_command(label='Consulta de Trimestre', command=self)
        menu_notas.add_command(label='Consulta de Detalhada', command=self)
        # ========== TURMA ==========
        barra_menu.add_cascade(label="Turma", menu=menu_turma)
        menu_turma.add_command(label='Lista de Turma', command=self._call_turma)
        menu_turma.add_command(label='Matéria', command=self._call_materia)
        # ========== SOBRE ==========
        barra_menu.add_cascade(label="Sobre", menu=menu_sobre)
        menu_sobre.add_command(label='Sobre', command=self._sobreNos)

        # ==========Frames Principal==========
        menu_frame = Frame(root, bg=co0)
        menu_frame.place(x=0, y=0, width=900, height=500)

        root.mainloop()

    # Funcao para minimizar a janela Menu Principal
    def _minimizar(self):
        """
        -> Minimiza janela Menu Principal
        """
        self.window.state(newstate='iconic')
        ...
    # END def _minimizar         
        
    # Funcao para chamada de Cadastro de Funcionario
    def _call_funcionario(self):
        """
        -> Chama a Janela de Cadastro de Funcionário.
        """
        self._minimizar()
        Funcionario()
        ...
    # END def _call_funcionario

    # Funcao para chamada de Cadastro de Aluno
    def _call_aluno(self):
        """
        -> Chama a janela de Cadastro de Aluno
        """
        self._minimizar()
        Aluno()
        ...
    # END def _call_aluno

     # Menu: Sobre nós
    def _sobreNos(self):
        """
        -> Informação do Desenvolvedor do Sistema.
        """
        messagebox.showinfo("Sobre nós",
                            """Este software facilita o gerenciamento de alunos.\nFoi criado por: Jefferson Assis de Souza 
                            \n\nProgramador: Python\n\nEmail: jeff-assis@hotmail.com""")
    # END def _sobreNos

    # Funcao para chamada de Cadastro de Materia
    def _call_materia(self):
        """
        -> Chama a janela de Cadastro de Materia
        """
        self._minimizar()
        Materia()
        ...
    # END def _call_materia

    # Funcao para chamada de Turma
    def _call_turma(self):
        """
        -> Chama a janela de Turma
        """
        self._minimizar()
        Turma()
        ...
    # END def _call_turma

    # Funcao para chamada de Turma
    def _call_notas(self):
        """
        -> Chama a janela de Notas
        """
        self._minimizar()
        Notas()
        ...
    # END def _call_notas