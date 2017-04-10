import matplotlib.pyplot as plt
from PyQt4.QtGui import *
class Handler:
    def __init__(self, atomos, qtd, metodo):
        self.atomos = atomos
        self.qtd = qtd
        self.energiatotal = 0
        self.energiaCristalina = 0
        self.metodoUtilizado = metodo
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        '''
            Dicionarios de elementos do programa MÉTODO 1 CCA PBE
        '''
        self.eatl_dic = {"Fe": -2545.55208452, "N": -109.135582, "Fl": -199.520212, "Cl": -922.888709}
        self.energiaCristalina_dic = {"Fl": -109.25426013, "Fe": -2545.132866, "Cl": -922.888709}
        '''
            Dicionarios de elementos do programa MÉTODO 2 CCA WC
        '''
        self.eatl_dicM2 = {"Fe": -2544.81855824, "N": -102.922900, "Fl": -399.520212, "Cl": -922.888709}
        self.energiaCristalina_dicM2 = {"Fl": -1992.47009291, "Fe": -2545.132821, "N": -10905674659, "Cl": -922.888709}
        '''
            Dicionarios de elementos do programa MÉTODO 3 LSDA
        '''
        self.eatl_dicM3 = {"Fe": -2540.606913, "N": -108.53662328, "Fl": -19322439.520212, "Cl": -922.888709}
        self.energiaCristalina_dicM3 = {"Fl": -144499.47009291, "Fe": -2541.14781082, "N": -108.331532, "Cl": -922.888709}
        '''
            Dicionarios de elementos do programa MÉTODO 4 PBE sol CCA
        '''
        self.eatl_dicM4 = {"Fe": -2545.132820, "N": -108.717522, "Fl": -19322439.520212, "Cl": -922.888709}
        self.energiaCristalina_dicM4 = {"Fl": -144499.47009291, "Fe": -2543.27041059, "N": -108.89480193, "Cl": -922.888709}

    def somatorioEATML(self):
        try:
            if self.metodoUtilizado == 1:
                for i in range(len(self.atomos)):
                    self.energiatotal += self.eatl_dic[self.atomos[i]] * self.qtd[i]
                return self.energiatotal

            elif self.metodoUtilizado == 2:
                for i in range(len(self.atomos)):
                    self.energiatotal += self.eatl_dicM2[self.atomos[i]] * self.qtd[i]
                return self.energiatotal

            elif self.metodoUtilizado == 3:
                for i in range(len(self.atomos)):
                    self.energiatotal += self.eatl_dicM3[self.atomos[i]] * self.qtd[i]
                return self.energiatotal
            elif self.metodoUtilizado == 4:
                for i in range(len(self.atomos)):
                    self.energiatotal += self.eatl_dicM4[self.atomos[i]] * self.qtd[i]
                return self.energiatotal
        except:
            self.msg.setText("Erro")
            self.msg.setInformativeText("Elemento " + format(self.atomos) +
                          " não existente na lista de elementos.")
            self.msg.show()

    def somatorioECRYS(self):
        try:
            if self.metodoUtilizado == 1:
                for i in range(len(self.atomos)):
                    self.energiaCristalina += self.energiaCristalina_dic[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
            elif self.metodoUtilizado == 2:
                for i in range(len(self.atomos)):
                    self.energiaCristalina += self.energiaCristalina_dicM2[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
            elif self.metodoUtilizado == 3:
                for i in range(len(self.atomos)):
                    self.energiaCristalina += self.energiaCristalina_dicM3[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
            elif self.metodoUtilizado == 4:
                for i in range(len(self.atomos)):
                    self.energiaCristalina += self.energiaCristalina_dicM4[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
        except:
            self.msg.setText("Erro")
            self.msg.setInformativeText("Elemento " + format(self.atomos) +
                          " não existente na lista de elementos.")
            self.msg.show()




