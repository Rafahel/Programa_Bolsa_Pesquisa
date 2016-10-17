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
            Dicionarios de elementos do programa MÉTODO 1
        '''
        self.eatl_dic = {"Fe": -2545.132813, "N": -109.135600, "Fl": -199.520212}
        self.energiaCristalina_dic = {"Fl": -199.47009291, "Fe": -2540.606906}
        '''
            Dicionarios de elementos do programa MÉTODO 2
        '''
        self.eatl_dicM2 = {"Fe": -4000.132813, "N": -209.135600, "Fl": -399.520212}
        self.energiaCristalina_dicM2 = {"Fl": -1992.47009291, "Fe": -23540.606906}
        '''
            Dicionarios de elementos do programa MÉTODO 3
        '''
        self.eatl_dicM3 = {"Fe": -3000.132813, "N": -109.135600, "Fl": -19322439.520212}
        self.energiaCristalina_dicM3 = {"Fl": -144499.47009291, "Fe": -25566640.606906}

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
                    self.energiaCristalina += self.energiaCristalina_dic[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
            elif self.metodoUtilizado == 3:
                for i in range(len(self.atomos)):
                    self.energiaCristalina += self.energiaCristalina_dic[self.atomos[i]] * self.qtd[i]
                return self.energiaCristalina
        except:
            self.msg.setText("Erro")
            self.msg.setInformativeText("Elemento " + format(self.atomos) +
                          " não existente na lista de elementos.")
            self.msg.show()




