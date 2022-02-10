import sqlite3
import pandas as pd
from tkinter import *

#----------------------------------------------
#Para criação do banco de dados retira o comentário (#) da linha 9 à 23 somente a primeira vez que rodar o cód,
#depois, basta comentar novamente.

#Criando o Banco de Dados
#conexao = sqlite3.connect('Banco.db')

#c = conexao.cursor()

#c.execute(''' CREATE TABLE pacientes (
#        Nome text,
#        Sexo text,
#        D_nascimento text,
#        Telefone text,
#        Mae text
#        )
#       ''')

#conexao.commit()
#conexao.close()
#-----------------------------------------------

tela = Tk() #estartando a janela

class Application():
    def __init__(self):
        self.tela = tela
        self.janela()
        self.frames_da_tela()
        self.widgets_frame1()
        tela.mainloop()
#-----------------------------------------------
#Configuração para a tela
    def janela(self):
        tela.title("Cadastro de Pacientes") #Inserindo um título na janela
        tela.configure(background= '#4682B4')
        tela.geometry("688x588")
        tela.resizable(True, True)
        tela.maxsize(width=888, height=788)
        tela.minsize(width=488, height=388)
#-------------------------------------------
#Criando os frames
    def frames_da_tela(self):
        self.frame_1 = Frame(self.tela, bd=4, bg='#dfe3ee',highlightbackground='#759fe6',
                             highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.tela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                             highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # Criando as funções que serão utilizadas nos botões:
        def cadastrar_paciente():
            conexao = sqlite3.connect('Banco.db')
            c = conexao.cursor()
            c.execute("INSERT INTO pacientes VALUES (:nome,:sexo,:d_nascimento, :telefone, :mae)",
                      {
                          'nome': entry_nome.get(),
                          'sexo': entry_sexo.get(),
                          'd_nascimento': entry_d_nascimento.get(),
                          'telefone': entry_telefone.get(),
                          'mae': entry_mae.get()
                      }
                      )
            conexao.commit()
            conexao.close()
            # criando uma função para limpar a tela após inserir registros
            entry_nome.delete(0, "end")
            entry_sexo.delete(0, "end")
            entry_d_nascimento.delete(0, "end")
            entry_telefone.delete(0, "end")
            entry_mae.delete(0, "end")
        #------------------------------------------------------------------------------
        # Criando a função para o botão exportar, onde as informações do banco será exportada em formato xlxs
        def exportar_pacientes():
            conexao = sqlite3.connect('Banco.db')
            c = conexao.cursor()
            c.execute("SELECT *, oid FROM pacientes")  # Criando um select da tabela clientes
            clientes_cadastrados = c.fetchall()  # Onde eu utilizo a estrutura fetchall para retornar todos os dados da mesma
            clientes_cadastrados = pd.DataFrame(clientes_cadastrados,
                                                columns=['Nome', 'Sexo', 'D_Nascimento', 'Telefone', 'Mae',
                                                         'Id_banco'])  # em seguida transformo a variável em um Dataframe
            clientes_cadastrados.to_excel('banco_pacientes.xlsx')  # Para que assim eu possa exportar como Excel
            conexao.commit()
            conexao.close()
        #-----------------------------------------------------------------------------------------
        #Criando os botões:
        # Criação do Botão Cadastrar
        self.bt_Cadastrar = Button(self.frame_1, text="Cadastrar", command=cadastrar_paciente)
        self.bt_Cadastrar.place(relx=0.15, rely=0.8, relwidth=0.1, relheight=0.15)
        # Criação do Botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", command=cadastrar_paciente)
        self.bt_buscar.place(relx=0.25, rely=0.8, relwidth=0.1, relheight=0.15)
        # Criação do Botão Exportar
        self.bt_exportar = Button(self.frame_1, text="Exportar Informações", command=exportar_pacientes)
        self.bt_exportar.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.15)
        # Criação do Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar Informações", command=exportar_pacientes)
        self.bt_alterar.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)
        # Criação do Botão Excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir Informações", command=exportar_pacientes)
        self.bt_excluir.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.15)
        #---------------------------------------------------------------------------------
        #Criando os Labels e entrada do codigo (Entrys)
        
        # Criando a Label de código
        label_codigo = Label(self.frame_1, text="Código")
        label_codigo.place(relx=0, rely=0.05)
        #Criando a Label de nome
        label_nome = Label(self.frame_1, text="Nome")
        label_nome.place(relx=0.2, rely=0.05)
        # Criando a Label de sexo
        label_sexo = Label(self.frame_1, text="Sexo")
        label_sexo.place(relx=0, rely=0.2)
        # Criando a Label de data de nascimento
        label_dtn = Label(self.frame_1, text="Data de Nascimento")
        label_dtn.place(relx=0.2, rely=0.2)
        # Criando a Label de Telefone
        label_telefone = Label(self.frame_1, text="Telefone")
        label_telefone.place(relx=0.5, rely=0.2)
        # Criando a Label de nome da mãe
        label_nome_mae = Label(self.frame_1, text="Mãe")
        label_nome_mae.place(relx=0, rely=0.35)

        #Entrys
        #Entrys de Código
        entry_codigo = Entry(self.frame_1, text="Cód", width=10)
        entry_codigo.place(relx=0.08, rely=0.05)
        # Entrys de Nome
        entry_nome = Entry(self.frame_1, text="Nome", width=70)
        entry_nome.place(relx=0.28,rely= 0.05)
        # Entrys de Sexo
        entry_sexo = Entry(self.frame_1, text="Sexo", width=12)
        entry_sexo.place(relx=0.06, rely=0.2)
        # Entrys de Data de Nascimento
        entry_d_nascimento = Entry(self.frame_1, text="D_Nascimento", width=10)
        entry_d_nascimento.place(relx=0.39, rely=0.2)
        # Entrys de Telefone
        entry_telefone = Entry(self.frame_1, text="Telefone", width=25)
        entry_telefone.place(relx=0.59, rely=0.2)
        # Entrys do Nome da Mãe
        entry_mae = Entry(self.frame_1, text="Mae", width=70)
        entry_mae.place(relx=0.06, rely=0.35)


#Rodar a aplicação
Application() #chamando a classe Application