import sqlite3
import pandas as pd
from tkinter import *
from tkinter import ttk

from importacao_pdf import relatorio

tela = Tk() #estartando a janela


class Funcs():
    #Criando uma função para conectar ao banco
    def conecta_bd(self):
        self.conexao = sqlite3.connect('Banco.db')
        self.c = self.conexao.cursor()
    # Criando uma função para desconectar ao banco
    def desconecta_db(self):
        self.conexao.close()
    # Criando uma função para criar a tabela no banco
    def cria_tabela(self):
        self.conecta_bd();
        print("Conectando ao Banco de Dados")
        # Criando a tabela do Bando de dados
        self.c.execute(''' 
        CREATE TABLE IF NOT EXISTS pacientes (
                COD INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Sexo TEXT,
                D_nascimento TEXT,
                Telefone INTEGER(20),
                Mae TEXT NOT NULL
                );
               ''')
        self.conexao.commit();
        print("Banco de dados Criado")
        self.desconecta_db()
    # criando uma função para limpar a tela após inserir registros
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_sexo.delete(0, END)
        self.entry_d_nascimento.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_mae.delete(0, END)
    #Criando uma função para criação de variáveis que serão utilziadas em outras funções
    def variaveis(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.sexo = self.entry_sexo.get()
        self.nascimento = self.entry_d_nascimento.get()
        self.telefone = self.entry_telefone.get()
        self.mae = self.entry_mae.get()
    # criando uma função para inserir registros
    def cadastrar_paciente(self):
        self.variaveis()
        self.conecta_bd()
        self.c.execute("""INSERT INTO pacientes (Nome, Sexo, D_Nascimento, Telefone, Mae)
                    VALUES(?, ?, ?, ?, ?)""", (self.nome, self.sexo, self.nascimento, self.telefone, self.mae))
        self.conexao.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()
    #Criando uma função para selecionar as informações preenchidas
    def select_lista(self):
        self.lista_pac.delete(*self.lista_pac.get_children())
        self.conecta_bd()
        lista = self.c.execute('''SELECT COD, Nome, Sexo, D_Nascimento, Telefone, Mae FROM pacientes
                                ORDER BY Nome ASC''')
        for i in lista:
            self.lista_pac.insert("", END, values=i)
        self.desconecta_db()
    #Criando uma função para capturar as informações com um evento de duplo clique do mouse
    def doubleclick(self, event):
        self.limpa_tela()
        self.lista_pac.selection()
        for n in self.lista_pac.selection():
            col1, col2, col3, col4, col5, col6 = self.lista_pac.item(n, "values")
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_sexo.insert(END, col3)
            self.entry_d_nascimento.insert(END, col4)
            self.entry_telefone.insert(END, col5)
            self.entry_mae.insert(END, col6)

    # Criando a função para buscar registros
    def buscapac(self):
        self.conecta_bd()
        self.lista_pac.delete(*self.lista_pac.get_children())

        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        # criando um select para retornar as informações que eu quero do banco
        self.c.execute(
            """ SELECT COD, Nome, Sexo, D_Nascimento, Telefone, Mae FROM pacientes
             WHERE Nome LIKE '%s' ORDER BY Nome ASC""" % nome)
        buscanomepac = self.c.fetchall() #criando uma variável para receber todos os valores do banco
        for i in buscanomepac: #criando um for para percorrer esses valores e mostrar na tela
            self.lista_pac.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_db()
    # criando uma função para excluir registros
    def delete(self):
        self.variaveis()
        self.conecta_bd()
        self.c.execute("""DELETE FROM pacientes WHERE COD = ?""", (self.codigo))
        self.conexao.commit()
        self.desconecta_db()
        self.limpa_tela()
        self.select_lista()
    #Criando a função para alterar as informações dos registros (UPDATE)
    def altera(self):
        self.variaveis()
        self.conecta_bd()
        self.c.execute("""UPDATE pacientes SET Nome = ?, Sexo = ?, D_Nascimento = ?, Telefone = ?, Mae = ?
                        WHERE COD = ?""", (self.nome, self.sexo, self.nascimento,self.telefone, self.mae, self.codigo))
        self.conexao.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()
    # criando uma função para exportar os registros em formato xlsx(Excel)
    def exportar_pacientes(self):
        conexao = sqlite3.connect('Banco.db')
        c = conexao.cursor()
        c.execute("SELECT *, oid FROM pacientes")  # Criando um select da tabela clientes
        clientes_cadastrados = c.fetchall()  # Onde eu utilizo a estrutura fetchall para retornar todos os dados da mesma
        clientes_cadastrados = pd.DataFrame(clientes_cadastrados,
                                            columns=['COD','Nome', 'Sexo', 'D_Nascimento', 'Telefone', 'Mae',
                                                     'Id_banco'])  # em seguida transformo a variável em um Dataframe
        clientes_cadastrados.to_excel('banco_pacientes.xlsx')  # Para que assim eu possa exportar como Excel
        conexao.commit()
        conexao.close()

    # Criando uma função de barra de menu
    def menu(self):
        menubar = Menu(self.tela)
        self.tela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.tela.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Paciente", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpa Tela", command=self.limpa_tela)

        filemenu2.add_command(label="Exportar Cadastro para PDF", command=self.gerarelatorio)
        filemenu2.add_command(label="Exportar Cadastros para xlsx", command=self.exportar_pacientes)


class Application(Funcs, relatorio):
    def __init__(self):
        self.tela = tela
        self.janela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.cria_tabela()
        self.select_lista()
        self.menu()
        self.gerarelatorio()
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
                                   font=('verdana', 8), command=self.buscapac)
        self.bt_buscar.place(relx=0.25, rely=0.8, relwidth=0.1, relheight=0.15)
        #Criação do Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar Informações", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.altera)
        self.bt_alterar.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)
        # Criação do Botão Excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir Informações", bd=3, bg='#107db2', fg='white',
                                   font=('verdana', 8), command=self.delete)
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
        self.lista_pac.bind("<Double-1>", self.doubleclick) #Chamando o evento de duplo clique



#Rodar a aplicação
Application() #chamando a classe Application