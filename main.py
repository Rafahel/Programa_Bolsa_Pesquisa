from Handler import Handler
from Calculo import Calculo
import matplotlib.pyplot as plt
import Interface
from Interface import _fromUtf8
from PyQt4 import QtCore, QtGui
import sys



class MainUIClass(QtGui.QMainWindow, Interface.Ui_MainWindow):

    def __init__(self, parent = None):
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
        self.arquivoLeitura = ""
        self.metodoEscolhido = -1
        self.listaEntradasDeAtomos.append(self.lineEdit)
        self.listaEntradasNumeroDeAtomos.append(self.lineEdit_2)
        self.botaoBrowseFiles.clicked.connect(self.selecionaArquivo)
        self.botao_calculaEnergiaCoesao.clicked.connect(self.calcularEnergiaCoesao)
        self.botao_calculaEnergiaFormacao.clicked.connect(self.calcularEnergiaFormacao)
        self.botao_calculaEnergiaCoesao.setEnabled(False)
        self.botao_calculaEnergiaFormacao.setEnabled(False)
        self.adicionarEntradas()

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

    def leEntradas(self):
        for i in range(self.quantidadeEntradas):
            atomo = str(self.listaEntradasDeAtomos[i].text())
            if len(atomo):
                quantidade = str(self.listaEntradasNumeroDeAtomos[i].text())
                if len(quantidade):
                    self.atomos.append(str(self.listaEntradasDeAtomos[i].text()).capitalize())
                    self.quantidades.append(int(self.listaEntradasNumeroDeAtomos[i].text()))

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
                            print("Erro no conteudo do arquivo")
            except:
                print("Erro no arquivo")
                return
        except:
            print("Erro ao abrir arquivo")
        self.botao_calculaEnergiaCoesao.setEnabled(True)
        self.botao_calculaEnergiaFormacao.setEnabled(True)


    def calcularEnergiaCoesao(self):
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
        if self.metodoCalculo_A.isChecked():
            self.metodoEscolhido = 1
        if self.metodoCalculo_B.isChecked():
            self.metodoEscolhido = 2
        if self.metodoCalculo_C.isChecked():
            self.metodoEscolhido = 3
        self.soma = Handler(self.atomos, self.quantidades, self.metodoEscolhido)
        self.somatorioEnergiaAtomoLivre = self.soma.somatorioEATML()  # Resultado do somatorio de EATML
        self.calc = Calculo(self.energia, self.somatorioEnergiaAtomoLivre, 0)
        self.resultado = self.calc.calculo_energia_coesao()
        self.geraArquivo()
        self.geraGrafico()
        return

    def calcularEnergiaFormacao(self):  # Método que da inicio ao cálculo
        try:
            self.leEntradas()
        except:
            print("Erro na leitura de dados nas entryBOXes")
            self.listaEntradasDeAtomos[:] = []
            self.listaEntradasNumeroDeAtomos[:] = []
            return
        self.ef = True
        self.ec = False
        self.soma = Handler(self.atomos, self.quantidades)
        self.somatorioEnergiaCristalina = self.soma.somatorioECRYS()  # Resultado do somatorio de ECRYS
        self.calc = Calculo(self.energia, 0, self.somatorioEnergiaCristalina)
        self.resultado = self.calc.calculo_energia_formacao()
        print(self.resultado)
        self.listaEntradasDeAtomos[:] = []
        self.listaEntradasNumeroDeAtomos[:] = []
        self.geraArquivo()
        self.geraGrafico()
        return


    def geraArquivo(self):  # Método para gerar arquivo com os resultados do cálculo
        try:
            self.arquivoSaida = open(self.arquivoLeitura + "__Resultados" + ".txt", "w")
            if len(self.volume) > 0 and self.ef:
                self.arquivoSaida.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                   "ENERGIA DE FORMACAO\n\n")
                for i in range(len(self.resultado)):
                    self.arquivoSaida.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                       str(self.resultado[i]) + "\n")
                self.arquivoSaida.close()
            elif self.ec:
                self.arquivoSaida.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                   "ENERGIA DE Coesão\n\n")
                for i in range(len(self.resultado)):
                    self.arquivoSaida.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                       str(self.resultado[i]) + "\n")
                self.arquivoSaida.close()
        except:
            print("erro ao criar arquivo")
            return


    def geraGrafico(self):
        if self.ec:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de coesão")
                plt.ylabel("Energia de coesão")
                plt.xlabel("Volume")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                return

        if self.ef:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de formação")
                plt.xlabel("Volume")
                plt.ylabel("Energia de formação")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                return

    def resetaEntradas(self):
        self.listaEntradasDeAtomos[:] = []
        self.listaEntradasNumeroDeAtomos[:] = []




if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainUIClass()
    app.setFixedSize(958, 926)
    app.show()
    a.exec_()
