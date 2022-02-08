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
#        Sobrenome text,
#        Sexo text,
#        Telefone text,
#        Origem text,
#        Cidade text,
#        Estado text
#        )
#       ''')

#conexao.commit()
#conexao.close()
#-----------------------------------------------
#Criando as funções que serão utilizadas nos botões

def cadastrar_paciente():
    conexao = sqlite3.connect('Banco.db')
    c = conexao.cursor()
    c.execute("INSERT INTO pacientes VALUES (:nome,:sobrenome,:sexo,:telefone, :origem, :cidade, :estado)",
         {
        'nome': entry_nome.get(),
        'sobrenome': entry_sobrenome.get(),
        'sexo': entry_sexo.get(),
        'telefone': entry_telefone.get(),
        'origem': entry_origem.get(),
        'cidade': entry_cidade.get(),
        'estado': entry_estado.get()
            }
              )

    conexao.commit()
    conexao.close()

    #criando uma função para limpar a tela após inserir registros
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_sexo.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_origem.delete(0, "end")
    entry_cidade.delete(0, "end")
    entry_estado.delete(0, "end")

#Criando a função para exportar as informações do banco em formato xlxs
def exportar_pacientes():
    conexao = sqlite3.connect('Banco.db')
    c = conexao.cursor()

    c.execute("SELECT *, oid FROM pacientes") #Criando um select da tabela clientes
    clientes_cadastrados = c.fetchall() #Onde eu utilizo a estrutura fetchall para retornar todos os dados da mesma
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['Nome','Sobrenome','Sexo','Telefone', 'Origem', 'Cidade', 'Estado','Id_banco']) #em seguida transformo a variável em um Dataframe
    clientes_cadastrados.to_excel('banco_pacientes.xlsx') #Para que assim eu possa exportar como Excel

    conexao.commit()
    conexao.close()
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

        #Criando os Labels e entrada do codigo
        # Criando a Label de código
        label_codigo = Label(self.frame_1, text="Código")
        label_codigo.place(relx=0, rely=0.05)
        #Criando a Label de nome
        label_nome = Label(self.frame_1, text="Nome")
        label_nome.place(relx=0.2, rely=0.05)
        # Criando a Label de Telefone
        #label_telefone = Label(tela, text="Telefone")
        #label_telefone.grid(row=2, column=0, padx=10, pady=10)



#Criando as Labels:






label_origem = Label(tela, text="Origem")
label_origem.grid(row=4, column=0, padx=10, pady=10)

label_cidade = Label(tela, text="Cidade")
label_cidade.grid(row=5, column=0, padx=10, pady=10)

label_estado = Label(tela, text="Estado")
label_estado.grid(row=6, column=0, padx=10, pady=10)
#-------------------------------------------------------
#Entrys
entry_nome = Entry(tela, text="Nome", width=30)
entry_nome.grid(row=0, column=2, padx=10, pady=10)

entry_sobrenome = Entry(tela, text="Sobrenome", width=30)
entry_sobrenome.grid(row=1, column=2, padx=10, pady=10)

entry_sexo = Entry(tela, text="Sexo", width=30)
entry_sexo.grid(row=2, column=2, padx=10, pady=10)

entry_telefone = Entry(tela, text="Telefone", width=30)
entry_telefone.grid(row=3, column=2, padx=10, pady=10)

entry_origem = Entry(tela, text="Origem", width=30)
entry_origem.grid(row=4, column=2, padx=10, pady=10)

entry_cidade = Entry(tela, text="Cidade", width=30)
entry_cidade.grid(row=5, column=2, padx=10, pady=10)

entry_estado = Entry(tela, text="Estado", width=30)
entry_estado.grid(row=6, column=2, padx=10, pady=10)

Application() #chamando a classe Application