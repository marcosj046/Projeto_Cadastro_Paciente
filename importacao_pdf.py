from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

#Criando a classe relatorio que ira conter duas funções a função para abrir o pdf no navegador automáticamente
# e a função que irá gerar o relatório em pdf.

class relatorio():
    #Função que realiza a abertura do documento pdf no navegador de forma automática
    #def print(self):
    #    webbrowser.open("banco.pdf")
    #Função que irá gerar o relatório
    def gerarelatorio(self):
        self.c = canvas.Canvas("banco.pdf")

        self.codrel = self.entry_codigo.get()
        self.nomerel = self.entry_nome.get()
        self.sexorel = self.entry_sexo.get()
        self.nascrel = self.entry_d_nascimento.get()
        self.telrel = self.entry_telefone.get()
        self.maerel = self.entry_mae.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Cadastro de Pacientes')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 640, 'Sexo: ')
        self.c.drawString(50, 610, 'Data de Nascimento: ')
        self.c.drawString(50, 580, 'Contato: ')
        self.c.drawString(50, 550, 'Nome da Mãe: ')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(120, 700, self.codrel)
        self.c.drawString(120, 670, self.nomerel)
        self.c.drawString(120, 640, self.sexorel)
        self.c.drawString(120, 610, self.nascrel)
        self.c.drawString(120, 580, self.telrel)
        self.c.drawString(120, 550, self.maerel)

        self.c.showPage()
        self.c.save()
        #self.print()
