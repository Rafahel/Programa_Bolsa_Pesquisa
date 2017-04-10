from Handler import Handler
from Calculo import Calculo
import matplotlib.pyplot as plt
import Interface
from Interface import _fromUtf8
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys
import Polinomio

class MainUIClass(QtGui.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.quantidadeEntradas = 1
        self.listaEntradasDeAtomos = []
        self.listaEntradasNumeroDeAtomos = []
        self.atomos = []
        self.quantidades = []
        self.energia = []
        self.volume = []
        self.ec = False
        self.ef = False
        self.metodoA = False
        self.metodoB = False
        self.metodoC = False
        self.metodoD = False
        self.arquivoLeitura = ""
        self.metodoEscolhido = -1
        self.listaEntradasDeAtomos.append(self.lineEdit)
        self.listaEntradasNumeroDeAtomos.append(self.lineEdit_2)
        self.botaoBrowseFiles.clicked.connect(self.selecionaArquivo)
        self.botao_calculaEnergiaCoesao.clicked.connect(self.calcularEnergiaCoesao)
        self.botao_calculaEnergiaFormacao.clicked.connect(self.calcularEnergiaFormacao)
        self.botao_calculaEnergiaCoesao.setEnabled(False)
        self.botao_calculaEnergiaFormacao.setEnabled(False)
        self.textBrowser.setVisible(False)
        self.resultadoLabel.setVisible(False)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.adicionarEntradas()

    '''
            Método responsável por adicionar as entryboxes na janela.
    '''

    def adicionarEntradas(self):
        for i in range(30):
            lineEdit = QtGui.QLineEdit()
            lineEdit.setObjectName(_fromUtf8("lineEdit"))
            self.listaEntradasDeAtomos.append(lineEdit)
            self.verticalLayout_1.addWidget(self.listaEntradasDeAtomos[self.quantidadeEntradas])

            lineEdit_2 = QtGui.QLineEdit()
            lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
            self.listaEntradasNumeroDeAtomos.append(lineEdit_2)
            self.verticalLayout_2.addWidget(self.listaEntradasNumeroDeAtomos[self.quantidadeEntradas])

            self.quantidadeEntradas += 1

    '''
            Método para salvar as entradas que foram escritas nas entryboxes duas listas, uma para atomos e outra para
            a quantidade de atomos.
    '''

    def leEntradas(self):
        for i in range(self.quantidadeEntradas):
            atomo = str(self.listaEntradasDeAtomos[i].text())
            if len(atomo):
                quantidade = str(self.listaEntradasNumeroDeAtomos[i].text())
                if len(quantidade):
                    self.atomos.append(str(self.listaEntradasDeAtomos[i].text()).capitalize())
                    self.quantidades.append(int(self.listaEntradasNumeroDeAtomos[i].text()))

    '''
            Método para selecionar arquivo para a leitura
    '''

    def selecionaArquivo(self):
        try:
            self.arquivoLeitura = QtGui.QFileDialog.getOpenFileName()
            try:
                self.arquivo = open(self.arquivoLeitura, "r")
                texto = self.arquivo.readlines()
                for i in range(len(texto)):
                    try:
                        self.energia.append(float(texto[i].split()[1]))
                        self.volume.append(float(texto[i].split()[0]))
                    except:
                        try:
                            self.energia.append(float(texto[i]))
                        except:
                            print("Erro no conteudo do arquivo.")
            except:
                print("Erro no arquivo.")
                return
        except:
            print("Erro ao abrir arquivo")
        self.botao_calculaEnergiaCoesao.setEnabled(True)
        self.botao_calculaEnergiaFormacao.setEnabled(True)

    '''
            Método para realizar o cálculo de energia de coesão
    '''

    def calcularEnergiaCoesao(self):
        if self.metodoCalculo_A.isChecked():
            self.metodoEscolhido = 1
        if self.metodoCalculo_B.isChecked():
            self.metodoEscolhido = 2
        if self.metodoCalculo_C.isChecked():
            self.metodoEscolhido = 3
        if self.metodoCalculo_D.isChecked():
            self.metodoEscolhido = 4
            print("FLA")
        if self.metodoEscolhido == -1:
            self.msg.setText("AVISO")
            self.msg.setInformativeText("Escolha um método para a realização do cálculo!")
            self.msg.show()
        else:
            try:
                self.leEntradas()
            except:
                print("Erro na leitura de dados nas entryBOXes")
                self.listaEntradasDeAtomos[:] = []
                self.listaEntradasNumeroDeAtomos[:] = []
                return
            self.ec = True
            self.ef = False
            '''
                Se o botão estiver ativado ele salva o método que sera utilizado
                para fazer o calculo.

            '''
            self.soma = Handler(self.atomos, self.quantidades, self.metodoEscolhido)
            self.somatorioEnergiaAtomoLivre = self.soma.somatorioEATML()  # Resultado do somatorio de EATML
            self.calc = Calculo(self.energia, self.somatorioEnergiaAtomoLivre, 0)
            self.resultado = self.calc.calculo_energia_coesao()
            self.geraArquivo()


    '''
            Método para realizar o cálculo de energia de formação
    '''

    def calcularEnergiaFormacao(self):  # Método que da inicio ao cálculo
        if self.metodoCalculo_A.isChecked():
            self.metodoEscolhido = 1
        if self.metodoCalculo_B.isChecked():
            self.metodoEscolhido = 2
        if self.metodoCalculo_C.isChecked():
            self.metodoEscolhido = 3
        if self.metodoCalculo_D.isChecked():
            self.metodoEscolhido = 4
        if self.metodoEscolhido == -1:
            self.msg.setText("AVISO")
            self.msg.setInformativeText("Escolha um método para a realização do cálculo!")
            self.msg.show()
        else:
            try:
                self.leEntradas()
            except:
                print("Erro na leitura de dados nas entryBOXes")
                self.listaEntradasDeAtomos[:] = []
                self.listaEntradasNumeroDeAtomos[:] = []
                return
            self.ef = True
            self.ec = False
            self.soma = Handler(self.atomos, self.quantidades, self.metodoEscolhido)
            self.somatorioEnergiaCristalina = self.soma.somatorioECRYS()  # Resultado do somatorio de ECRYS
            self.calc = Calculo(self.energia, 0, self.somatorioEnergiaCristalina)
            self.resultado = self.calc.calculo_energia_formacao()
            self.listaEntradasDeAtomos[:] = []
            self.listaEntradasNumeroDeAtomos[:] = []
            self.geraArquivo()


    '''
            Método para gerar arquivo de resultado e mostrar no textBrowser os mesmos.
    '''

    def geraArquivo(self):
        try:
            formula = Polinomio.geradorPolinomio(self.volume, self.resultado)
            self.arquivoSaida = open(self.arquivoLeitura + "__Resultados" + ".txt", "w")
            if len(self.volume) > 0 and self.ef:
                self.arquivoSaida.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                        "ENERGIA DE FORMACAO\n\n")
                self.textBrowser.append("VOLUME" + "         " + "ENERGIA" + "           " +
                                        "ENERGIA DE FORMACAO\n\n")
                for i in range(len(self.resultado)):
                    self.arquivoSaida.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                            str(self.resultado[i]) + "\n")
                    self.textBrowser.append(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                            str(self.resultado[i]) + "\n")
                self.textBrowser.append("\nFORMULA:  " + formula)
                self.arquivoSaida.write("\nFORMULA:  " + formula)
                self.arquivoSaida.close()
                self.geraGrafico()
            elif self.ec:
                self.arquivoSaida.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                        "ENERGIA DE Coesão\n\n")
                self.textBrowser.append("VOLUME" + "         " + "ENERGIA" + "           " +
                                        "ENERGIA DE Coesão\n\n")
                for i in range(len(self.resultado)):
                    self.arquivoSaida.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                            str(self.resultado[i]) + "\n")
                    self.textBrowser.append(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                            str(self.resultado[i]) + "\n")
                self.textBrowser.append("\nFORMULA:  " + formula)
                self.arquivoSaida.write("\nFORMULA:  " + formula)
                self.arquivoSaida.close()
                self.geraGrafico()
        except:
            print("erro ao criar arquivo")
            return
        self.textBrowser.setVisible(True)
        self.resultadoLabel.setVisible(True)
        self.resetaEntradas()

    '''
            Método para gerar os gráficos com os resultados do cálculo.
    '''

    def geraGrafico(self):
        self.botao_calculaEnergiaCoesao.setEnabled(False)
        self.botao_calculaEnergiaFormacao.setEnabled(False)
        self.botaoBrowseFiles.setEnabled(False)
        if self.ec:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de coesão")
                plt.ylabel("Energia de coesão")
                plt.xlabel("Volume")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                self.resetaEntradas()
                return

        if self.ef:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de formação")
                plt.xlabel("Volume")
                plt.ylabel("Energia de formação")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                return


    '''
            Método para reiniciar as entryboxes e as listas de atomos e numero deles.
    '''

    def resetaEntradas(self):
        self.atomos[:] = []
        self.quantidades[:] = []
        for i in range(len(self.listaEntradasDeAtomos)):
            self.listaEntradasDeAtomos[i].clear()
            self.listaEntradasNumeroDeAtomos[i].clear()
        return


if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainUIClass()
    '''

        Seta a imagem de fundo da janela e o tamanho da mesma.

    '''
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/atom.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    app.setWindowTitle("CeF 1.7")
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/bg.png")))
    app.setPalette(palette)
    app.setFixedSize(870, 970)
    '''

        Mostra a janela na tela

    '''
    app.show()
    a.exec_()
