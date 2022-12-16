from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão deletar
co2 = "#918F2B"  # Cor botão fechar 
co3 = "#00E9CC"  # Cor botão inserir
co4 = "#FFCA18"  # Cor botão editar
co5 = "#F1864F"  # Cor botão pesquisar
co6 = "#3962F7"  # Cor botão limpar

class Aluno(Toplevel):

    def __init__(self, master: Tk):
        super().__init__(master=master)
        
        self.title("Cadastro de Funcionário")
        self.resizable(False, False)
        self.geometry("910x520+200+50")

        

        self.mainloop()
