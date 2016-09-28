import matplotlib.pyplot as plt
from tkinter import messagebox as message
class Handler:
    def __init__(self, atomos, qtd):
        self.atomos = atomos
        self.qtd = qtd
        self.energiatotal = 0
        self.energiaCristalina = 0
        # Dicionarios de elementos do programa
        self.eatl_dic = {"Fe": -2545.132813, "N": -109.135600, "Fl": -199.520212}
        self.energiaCristalina_dic = {"Fl": -199.47009291, "Fe": -2540.606906}

    def somatorioEATML(self):
        try:
            for i in range(len(self.atomos)):
                self.energiatotal += self.eatl_dic[self.atomos[i]] * self.qtd[i]
            return self.energiatotal
        except:
            message._show("Erro", "Elemento " + format(self.atomos) +
                          " não existente na lista de elementos.")

    def somatorioECRYS(self):
        try:
            for i in range(len(self.atomos)):
                self.energiaCristalina += self.energiaCristalina_dic[self.atomos[i]] * self.qtd[i]
            return self.energiaCristalina
        except:
            message._show("Erro", "Elemento " + format(self.atomos) +
                          " não existente na lista de elementos.")




