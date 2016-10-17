from Handler import Handler
from Calculo import Calculo
import matplotlib.pyplot as plt
from threading import Thread


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 230, 171, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.botaoBrowseFiles = QtGui.QPushButton(self.verticalLayoutWidget)
        self.botaoBrowseFiles.setObjectName(_fromUtf8("botaoBrowseFiles"))
        self.verticalLayout.addWidget(self.botaoBrowseFiles)
        self.botao_calculaEnergiaCoesao = QtGui.QPushButton(self.verticalLayoutWidget)
        self.botao_calculaEnergiaCoesao.setObjectName(_fromUtf8("botao_calculaEnergiaCoesao"))
        self.verticalLayout.addWidget(self.botao_calculaEnergiaCoesao)
        self.botao_calculaEnergiaFormacao = QtGui.QPushButton(self.verticalLayoutWidget)
        self.botao_calculaEnergiaFormacao.setObjectName(_fromUtf8("botao_calculaEnergiaFormacao"))
        self.verticalLayout.addWidget(self.botao_calculaEnergiaFormacao)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 641, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 140, 81, 751))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_1 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_1.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(130, 140, 61, 751))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(480, 410, 131, 111))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.metodoCalculo_A = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.metodoCalculo_A.setEnabled(True)
        self.metodoCalculo_A.setObjectName(_fromUtf8("metodoCalculo_A"))
        self.verticalLayout_3.addWidget(self.metodoCalculo_A)
        self.metodoCalculo_B = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.metodoCalculo_B.setObjectName(_fromUtf8("metodoCalculo_B"))
        self.verticalLayout_3.addWidget(self.metodoCalculo_B)
        self.metodoCalculo_C = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.metodoCalculo_C.setObjectName(_fromUtf8("metodoCalculo_C"))
        self.verticalLayout_3.addWidget(self.metodoCalculo_C)
        self.entrada_1Descricao = QtGui.QLabel(self.centralwidget)
        self.entrada_1Descricao.setGeometry(QtCore.QRect(60, 120, 46, 20))
        self.entrada_1Descricao.setObjectName(_fromUtf8("entrada_1Descricao"))
        self.entrada_2Descricao = QtGui.QLabel(self.centralwidget)
        self.entrada_2Descricao.setGeometry(QtCore.QRect(130, 120, 61, 20))
        self.entrada_2Descricao.setObjectName(_fromUtf8("entrada_2Descricao"))
        self.radioButtons_Descricao = QtGui.QLabel(self.centralwidget)
        self.radioButtons_Descricao.setGeometry(QtCore.QRect(450, 380, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtons_Descricao.setFont(font)
        self.radioButtons_Descricao.setObjectName(_fromUtf8("radioButtons_Descricao"))
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.entrada_1Descricao.raise_()
        self.entrada_2Descricao.raise_()
        self.radioButtons_Descricao.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSoftware = QtGui.QAction(MainWindow)
        self.actionSoftware.setObjectName(_fromUtf8("actionSoftware"))
        self.actionProgramador = QtGui.QAction(MainWindow)
        self.actionProgramador.setObjectName(_fromUtf8("actionProgramador"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.botaoBrowseFiles.setText(_translate("MainWindow", "Abrir arquivo", None))
        self.botao_calculaEnergiaCoesao.setText(_translate("MainWindow", "Calcular energia de coesão", None))
        self.botao_calculaEnergiaFormacao.setText(_translate("MainWindow", "Calcular energia de formação", None))
        self.label.setText(_translate("MainWindow", "Calculadora CeF", None))
        self.metodoCalculo_A.setText(_translate("MainWindow", "MétodoA", None))
        self.metodoCalculo_B.setText(_translate("MainWindow", "MétodoB", None))
        self.metodoCalculo_C.setText(_translate("MainWindow", "MétodoC", None))
        self.entrada_1Descricao.setText(_translate("MainWindow", "Atomos", None))
        self.entrada_2Descricao.setText(_translate("MainWindow", "Quantidade", None))
        self.radioButtons_Descricao.setText(_translate("MainWindow", "Selecione o método de Cálculo", None))
        self.actionSoftware.setText(_translate("MainWindow", "Software", None))
        self.actionProgramador.setText(_translate("MainWindow", "Programador", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

