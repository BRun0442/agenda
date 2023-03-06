from argparse import ArgumentDefaultsHelpFormatter
from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

app = QtWidgets.QApplication([])
agenda = uic.loadUi('agenda.ui')

agenda.show()
app.exec()

db = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = 'root',
  database = 'agenda'
)

id = agenda.lineEdit.text()
nome = agenda.lineEdit_2.text()
email = agenda.lineEdit_3.text()
telefone = agenda.lineEdit_4.text()
