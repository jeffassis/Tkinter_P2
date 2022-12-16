from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import model.model_login as m_login
from menu import menu_window

################# cores ###############
co0 = "#353535"  # Cor da Janela
co1 = "#B00857"  # Cor botão entrar
co2 = "#918F2B"  # Cor botão fechar   

class login_window:
    # INTERFACE GRAFICA LOGIN
    def __init__(self):
        self.window = Tk()
        root = self.window
        root.title("Tela de Login")
        # ========== Centralizar Janela ==========
        largura = 600
        altura = 240
        # resolução do nosso sistema
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()
        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        # definir a geometry
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

        # Criando variáveis que armazena texto inserido
        self.txt_usuario = StringVar()
        self.txt_senha = StringVar()

        # Criando widgets raiz
        self.tela_principal = Frame(root, bg=co0)
        self.tela_principal.place(x=0, y=0, width=600, height=240)

        # Separador 
        ttk.Separator(self.tela_principal, orient=VERTICAL).place(x=225, y=8,  height=217)

        # Criando Widgets...
        #lb_escola = Label(self.tela_principal, image=img_escola, bg="#353535", bd=0)
        lb_dev = Label(self.tela_principal, text='JeffAssis©', font='arial 10 underline', bg=co0, fg="white")
        lb_titulo = Label(self.tela_principal, text="Seja bem-vindo", font=("Arial Black",25), bg=co0, fg="white")
        lb_usuario = Label(self.tela_principal, text='Usuário: ', font =('Arial Black', 12), bg=co0, fg="white")
        lb_senha = Label(self.tela_principal, text='Senha: ', font =('Arial Black', 12), bg=co0, fg="white")
        self.e_usuario = Entry(self.tela_principal, textvariable=self.txt_usuario, width=25, font=1)
        self.e_senha = Entry(self.tela_principal, textvariable=self.txt_senha, width=25, font=1, show='*')
        self.bt_entrar = Button(self.tela_principal, text="Entrar", command=self.login_entrar, cursor="hand2", font='arial', bg=co1, fg="white", width=8)
        self.bt_fechar = Button(self.tela_principal, text="Fechar", command=self.window.destroy, cursor="hand2", font='arial', bg=co2, fg="white", width=8)
        
        # Associando Widgets na janela...
        #lb_escola.place(x=30,y=30)
        lb_dev.place(x=70,y=210)
        lb_titulo.place(x=270, y=20)
        lb_usuario.place(x=235, y=85)
        lb_senha.place(x=235, y=120)
        self.e_usuario.place(x=320, y=90)
        self.e_senha.place(x=320, y=125)
        self.bt_entrar.place(x=320, y=160)
        self.bt_fechar.place(x=410, y=160)
        root.mainloop()

    def login_entrar(self):
        if self.txt_usuario.get().strip() == "" or self.txt_senha.get().strip() == "":
            messagebox.showerror("Error", "Os campos não podem ser vazios")
        else:    
            param1 = self.txt_usuario.get().strip()
            param2 = self.txt_senha.get().strip()
            result = m_login.logar(param1, param2)
            if result:
                self.window.destroy()
                menu_window()

            else:
                messagebox.showerror("error", "Usuário ou senha inválido!")

login_window()
