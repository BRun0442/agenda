from argparse import ArgumentDefaultsHelpFormatter
from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

app = QtWidgets.QApplication([])
agenda = uic.loadUi('agenda.ui')
contatos = uic.loadUi('userSignedUp.ui')

db = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = 'root',
  database = 'agenda'
)

def cadastrarContato():
    nome = agenda.nome.text()
    email = agenda.email.text()
    telefone = agenda.telefone.text()

    if agenda.residencial.isChecked():
        tipoTelefone = 'residencial'
    elif agenda.celular.isChecked():
        tipoTelefone = 'celular'
    else:
        tipoTelefone = 'nao informado'

    cursor = db.cursor()

    querySQL = 'insert into contatos(nome, email, telefone, tipoTelefone)  values(%s, %s, %s, %s);'
    dados = (str(nome), str(email), str(telefone), tipoTelefone)
    cursor.execute(querySQL, dados)
    db.commit()

def consultarContato():
    contatos.show()

    cursor = db.cursor()

    querySQL = 'select nome, email, telefone, tipoTelefone from contatos'
    cursor.execute(querySQL)
    dados = cursor.fetchall()
    # db.commit()

    contatos.listaContatos.setRowCount(len(dados))
    contatos.listaContatos.setColumnCount(4)

    for i in range(len(dados)):
        for j in range(0, 4):
            contatos.listaContatos.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

def gerarPDF():
    pass

def excluirContato():
    pass

agenda.cadastrarContatos.clicked.connect(cadastrarContato)
agenda.consultarContatos.clicked.connect(consultarContato)

# contatos.gerarPDF.clicked.connect(gerarPDF)
# contatos.excluirContato.clicked.connect(excluirContato)

agenda.show()
app.exec()