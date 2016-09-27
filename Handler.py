import matplotlib.pyplot as plt
class Handler:
    def __init__(self, atomos, qtd):
        self.atomos = atomos
        self.qtd = qtd
        self.energiatotal = 0
        self.energiaCristalina = 0
        # Dicionarios de elementos do programa
        self.eatl_dic = {"Fe": -2545.132813, "N": -109.135600, "F": -8000}
        self.energiaCristalina_dic = {"Fl": -199.47009291, "Fe": 0}

    def somatorioEATML(self):
        # print("Somatorio")
        print(len(self.atomos))
        for i in range(len(self.atomos)):
            self.energiatotal += self.eatl_dic[self.atomos[i]] * self.qtd[i]
        # print("Energia total: " + format(self.energiatotal))
        return self.energiatotal

    def somatorioECRYS(self):
        print("SomatorioECRYS" + format(len(self.atomos)))
        for i in range(len(self.atomos)):
            print(self.atomos)
            self.energiaCristalina += self.energiaCristalina_dic[self.atomos[i]] * self.qtd[i]
        # print("Energia total: " + format(self.energiatotal))
        return self.energiaCristalina



