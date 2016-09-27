
class Calculo:
    def __init__(self, etot, eatml, eatmb):
        self.etot = etot
        self.eatml = eatml
        self.eatmb = eatmb
        self.ec = []

    def calculo_energia_coesao(self):
        for i in range(len(self.etot)):
            self.ec.append(self.etot[i] - self.eatml)
        return self.ec

    def calculo_energia_formacao(self):
        for i in range(len(self.etot)):
            self.ec.append(self.etot[i] - self.eatmb)
        return self.ec
