import sqlite3
import tkinter as tk
import pandas as pd

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
#Criando as funções

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
tela = tk.Tk() #estartando a janela
tela.title("Cadastro de Pacientes") #Inserindo um título na janela

#Criando as Labels:
label_nome = tk.Label(tela, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(tela, text="Sobrenome")
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_sexo = tk.Label(tela, text="Sexo")
label_sexo.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(tela, text="Telefone")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

label_origem = tk.Label(tela, text="Origem")
label_origem.grid(row=4, column=0, padx=10, pady=10)

label_cidade = tk.Label(tela, text="Cidade")
label_cidade.grid(row=5, column=0, padx=10, pady=10)

label_estado = tk.Label(tela, text="Estado")
label_estado.grid(row=6, column=0, padx=10, pady=10)
#-------------------------------------------------------
#Entrys
entry_nome = tk.Entry(tela, text="Nome", width=30)
entry_nome.grid(row=0, column=2, padx=10, pady=10)

entry_sobrenome = tk.Entry(tela, text="Sobrenome", width=30)
entry_sobrenome.grid(row=1, column=2, padx=10, pady=10)

entry_sexo = tk.Entry(tela, text="Sexo", width=30)
entry_sexo.grid(row=2, column=2, padx=10, pady=10)

entry_telefone = tk.Entry(tela, text="Telefone", width=30)
entry_telefone.grid(row=3, column=2, padx=10, pady=10)

entry_origem = tk.Entry(tela, text="Origem", width=30)
entry_origem.grid(row=4, column=2, padx=10, pady=10)

entry_cidade = tk.Entry(tela, text="Cidade", width=30)
entry_cidade.grid(row=5, column=2, padx=10, pady=10)

entry_estado = tk.Entry(tela, text="Estado", width=30)
entry_estado.grid(row=6, column=2, padx=10, pady=10)

#Botões
botao_Cadastrar = tk.Button(tela, text="Cadastrar Paciente", command = cadastrar_paciente)
botao_Cadastrar.grid(row=7, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(tela, text="Exportar Informações", command = exportar_pacientes)
botao_exportar.grid(row=7, column=2, padx=10, pady=10, columnspan=2, ipadx=80)

#Obs: ipadx=80 - Basicamente serve para alargar uma estrutura especifíca
tela.mainloop()