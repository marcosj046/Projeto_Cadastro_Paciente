import sqlite3
import pandas as pd
from tkinter import *
from tkinter import ttk

#----------------------------------------------
#Para criação do banco de dados retira o comentário (#) da linha 11 à 25 somente a primeira vez que rodar o cód,
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

class Funcs():
    # criando uma função para limpar a tela após inserir registros
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_sexo.delete(0, END)
        self.entry_d_nascimento.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_mae.delete(0, END)

    # criando uma função para inserir registros
    def cadastrar_paciente(self):
        conexao = sqlite3.connect('Banco.db')
        c = conexao.cursor()
        c.execute("INSERT INTO pacientes VALUES (:nome,:sexo,:d_nascimento, :telefone, :mae)",
                  {
                      'nome': self.entry_nome.get(),
                      'sexo': self.entry_sexo.get(),
                      'd_nascimento': self.entry_d_nascimento.get(),
                      'telefone': self.entry_telefone.get(),
                      'mae': self.entry_mae.get()
                  }
                  )
        conexao.commit()
        conexao.close()

    # criando uma função para exportar os registros em formato xlsx(Excel)
    def exportar_pacientes(self):
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


class Application(Funcs):
    def __init__(self):
        self.tela = tela
        self.janela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
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

        #------------------------------------------------------------------------------
        # Criando a função para o botão exportar, onde as informações do banco será exportada em formato xlxs

        #-----------------------------------------------------------------------------------------
        #Criando os botões:
        # Criação do Botão Limpar
        self.bt_Limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#107db2', fg='white',
                                    font=('verdana', 8), command=self.limpa_tela)
        self.bt_Limpar.place(relx=0.02, rely=0.8, relwidth=0.08, relheight=0.15)
        # Criação do Botão Cadastrar
        self.bt_Cadastrar = Button(self.frame_1, text="Cadastrar", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.cadastrar_paciente)
        self.bt_Cadastrar.place(relx=0.15, rely=0.8, relwidth=0.1, relheight=0.15)
        # Criação do Botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.cadastrar_paciente)
        self.bt_buscar.place(relx=0.25, rely=0.8, relwidth=0.1, relheight=0.15)
        # Criação do Botão Exportar
        self.bt_exportar = Button(self.frame_1, text="Exportar Informações", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.exportar_pacientes)
        self.bt_exportar.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.15)
        # Criação do Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar Informações", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.exportar_pacientes)
        self.bt_alterar.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)
        # Criação do Botão Excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir Informações", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.exportar_pacientes)
        self.bt_excluir.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.15)
        #---------------------------------------------------------------------------------
        #Criando os Labels e entrada do codigo (Entrys)

        # Criando a Label de código
        self.label_codigo = Label(self.frame_1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.label_codigo.place(relx=0, rely=0.05)
        #Criando a Label de nome
        self.label_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.label_nome.place(relx=0.2, rely=0.05)
        # Criando a Label de sexo
        self.label_sexo = Label(self.frame_1, text="Sexo", bg='#dfe3ee', fg='#107db2')
        self.label_sexo.place(relx=0, rely=0.2)
        # Criando a Label de data de nascimento
        self.label_dtn = Label(self.frame_1, text="Data de Nascimento", bg='#dfe3ee', fg='#107db2')
        self.label_dtn.place(relx=0.2, rely=0.2)
        # Criando a Label de Telefone
        self.label_telefone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.label_telefone.place(relx=0.5, rely=0.2)
        # Criando a Label de nome da mãe
        self.label_nome_mae = Label(self.frame_1, text="Mãe", bg='#dfe3ee', fg='#107db2')
        self.label_nome_mae.place(relx=0, rely=0.35)

        #Entrys
        #Entrys de Código
        self.entry_codigo = Entry(self.frame_1, text="Cód", width=10)
        self.entry_codigo.place(relx=0.08, rely=0.05)
        # Entrys de Nome
        self.entry_nome = Entry(self.frame_1, text="Nome", width=70)
        self.entry_nome.place(relx=0.28,rely= 0.05)
        # Entrys de Sexo
        self.entry_sexo = Entry(self.frame_1, text="Sexo", width=12)
        self.entry_sexo.place(relx=0.06, rely=0.2)
        # Entrys de Data de Nascimento
        self.entry_d_nascimento = Entry(self.frame_1, text="D_Nascimento", width=10)
        self.entry_d_nascimento.place(relx=0.39, rely=0.2)
        # Entrys de Telefone
        self.entry_telefone = Entry(self.frame_1, text="Telefone", width=25)
        self.entry_telefone.place(relx=0.59, rely=0.2)
        # Entrys do Nome da Mãe
        self.entry_mae = Entry(self.frame_1, text="Mae", width=70)
        self.entry_mae.place(relx=0.06, rely=0.35)

    def lista_frame2(self):
        #Informando a quantidade de colunas em nossa treeview(tabela) que será mostrada na parte inferior
        self.lista_pac = ttk.Treeview(self.frame_2, height= 3, column=("col1", "col2", "col3", "col4",
                                                                       "col5", "col6"))
        #Informando o nome de cada coluna. Obs: lembrando que toda lista começa com o valor zero que nesse caso
        #será uma coluna em branco.
        self.lista_pac.heading("#0", text="")
        self.lista_pac.heading("#1", text="Código")
        self.lista_pac.heading("#2", text="Nome")
        self.lista_pac.heading("#3", text="Sexo")
        self.lista_pac.heading("#4", text="Nascimento")
        self.lista_pac.heading("#5", text="Contato")
        self.lista_pac.heading("#6", text="Mãe")
        #informando o tamanho de cada coluna
        self.lista_pac.column("#0", width=1, stretch=NO) #o parâmetro stretch=NO, permite que oculte a coluna vazia
        self.lista_pac.column("#1", width=40)
        self.lista_pac.column("#2", width=125)
        self.lista_pac.column("#3", width=35)
        self.lista_pac.column("#4", width=75)
        self.lista_pac.column("#5", width=100)
        self.lista_pac.column("#6", width=125)
        #Informando a posição no frame
        self.lista_pac.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        #Criando uma barra de rolagem para a lista
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.lista_pac.configure(yscroll=self.scroolLista.set)#Obs: se atentar para a forma de escrita, o correto é:
                                                              # yscroll e não yscrooll.
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)



#Rodar a aplicação
Application() #chamando a classe Application