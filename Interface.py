from tkinter import *
from Handler import Handler
from Calculo import Calculo
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import matplotlib.pyplot as plt

#  Esta interface foi criada utilizando o Módulo tkinter, o programa asseguir serve para realizar os
#  calculos de energia de coesão e formacão.
#  Criado por Rafahel Mello aluno de Ciência da computacão da Universidade Regional Integrada de Santo Ângelo
class Interface:
    def __init__(self):  # Inicializacão da interface do programa
        self.raiz = Tk()
        self.raiz.title("Calculadora CeF 1.1")
        self.raiz.geometry("650x800")  # Tamanho da janela
        self.raiz.resizable(width=False, height=True)  # Se a janela pode ser redimencionada
        self.titulo = Label(self.raiz, text="Calculadora CeF 1.1",
                            font=('Times New Roman', 25, 'bold'))
        self.entry_desc = Label(self.raiz, text="Entre com numero de especies atomicas")
        self.ec = False
        self.ef = False
        self.energia = []
        self.volume = []
        self.atomo = []
        self.n_atomos = []
        self.graf = []
        self.qtd_atomos = Entry()
        self.adc_entrada_atomo = Button(self.raiz, text="+", command=self.adc)
        self.botaoCalcularEC = Button(self.raiz, text="Calcular Energia de Coesão",
                                      command=self.calculaEC, state=DISABLED)
        self.botaoCalcularEF = Button(self.raiz, text="Calcular Energia de formação",
                                      command=self.calculaEF, state=DISABLED)
        self.n_atomos_desc = Label(self.raiz, text="Adicioinar")
        self.escolher_arquivo = Button(self.raiz, text="Abrir arquivo", command=self.escolherArquivo)
        # Grids. Coloca os elementos da GUI na tela e nas posicoes selecionas por row e column
        self.titulo.grid(row=0, column=2)
        self.entry_desc.grid(row=2, column=0)
        self.n_atomos_desc.grid(row=2, column=2)
        self.adc_entrada_atomo.grid(row=1, column=2)
        self.qtd_atomos.grid(row=1, column=0)
        self.raiz.mainloop()

    def geraArquivo(self):  # Método para gerar arquivo com os resultados do cálculo
        try:
            self.arquivo = open(self.arquivo + "__Resultados" + ".txt", "w")
            if len(self.volume) > 0 and self.ef:
                self.arquivo.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                   "ENERGIA DE FORMAÇÃO\n\n")
                for i in range(len(self.resultado)):
                    self.arquivo.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                       str(self.resultado[i]) + "\n")
                self.arquivo.close()
            elif self.ec:
                self.arquivo.write("VOLUME" + "         " + "ENERGIA" + "           " +
                                   "ENERGIA DE COESÃO\n\n")
                for i in range(len(self.resultado)):
                    self.arquivo.write(str(self.volume[i]) + "       " + str(self.energia[i]) + "        " +
                                       str(self.resultado[i]) + "\n")
                self.arquivo.close()
        except:
            messagebox._show("Erro", "Erro ao criar arquivo de respostas.")
        messagebox._show("Calculo concluido!", "O cálculo foi concluido com sucesso.")
        self.geraGrafico()

    def geraGrafico(self):  # Funcão responsavel por gerar grafico onde x = volume y = resultado
        if self.ec:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de coesão")
                plt.ylabel("Energia de coesão")
                plt.xlabel("Volume")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
        if self.ef:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                plt.title("Calculo de energia de formação")
                plt.xlabel("Energia de formação")
                plt.ylabel("Volume")
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
        self.raiz.quit()

    def iniciaEC(self, entrada_atomos, numero_atomos):  # Método que da inicio ao cálculo
        self.ec = True
        self.ef = False
        self.soma = Handler(entrada_atomos, numero_atomos)
        self.somatorioEnergiaAtomoLivre = self.soma.somatorioEATML()  # Resultado do somatorio de EATML
        self.calc = Calculo(self.energia, self.somatorioEnergiaAtomoLivre, 0)
        self.resultado = self.calc.calculo_energia_coesao()
        self.geraArquivo()

    def iniciaEF(self, entrada_atomos, numero_atomos):  # Método que da inicio ao cálculo
        self.ef = True
        self.ec = False
        self.soma = Handler(entrada_atomos, numero_atomos)
        self.somatorioEnergiaCristalina = self.soma.somatorioECRYS()  # Resultado do somatorio de ECRYS
        self.calc = Calculo(self.energia, 0, self.somatorioEnergiaCristalina)
        self.resultado = self.calc.calculo_energia_formacao()
        self.geraArquivo()

    def escolherArquivo(self):  # Método para escolher arquivo apartir de um botão na GUI
        self.arquivo = ""
        self.energia.clear()
        self.volume.clear()
        self.arquivo = str(askopenfile("r"))
        # As próximas 3 linhas retiram a parte que não é necessário da string que contem o caminho do arquivo
        self.arquivo = self.arquivo.replace("<_io.TextIOWrapper name='", "")
        self.arquivo = self.arquivo.replace("' mode='r' encoding='cp1252'>", "")
        self.arquivo = self.arquivo.replace("' mode='r' encoding='UTF-8'>", "")
        arq = open(self.arquivo)
        try:
            texto = arq.readlines()
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
        self.botaoCalcularEC.configure(state=NORMAL)
        self.botaoCalcularEF.configure(state=NORMAL)

    def adc(self):  # Método necessário para adicionar entradas de texto para serem adicionados os atomos.
        try:
            qtdAtomos = int(self.qtd_atomos.get())  # número de especies de atomos digitados
            r = 3  # row para ajustar os widgets na grid
            if qtdAtomos > 100 or qtdAtomos <= 0:
                messagebox._show("Erro", "A quantidade de espécies atomicas deve ser entre 1 e 100.")
                return
            for i in range(qtdAtomos):
                self.atomo.append(Entry(self.raiz))
                self.n_atomos.append(Entry(self.raiz))
            for i in range(qtdAtomos):
                self.atomo[i].grid(row=r, column=0)
                self.n_atomos[i].grid(row=r, column=2)
                r += 1
            self.escolher_arquivo.grid(row=r, column=4)
            r += 1
            self.botaoCalcularEC.grid(row=r, column=4)
            r += 1
            self.botaoCalcularEF.grid(row=r, column=4)
            self.adc_entrada_atomo.grid_remove()
            self.qtd_atomos.grid_remove()
            self.entry_desc.config(text="Espécie atômica")
            self.n_atomos_desc.config(text="Número de átomos")
        except:
            messagebox._show("Erro", "Caracter não permitido na entrada de espécies de atomos."
                                     " Tente novamente")

    def calculaEC(self):
        entrada_atomos = []
        numero_atomos = []

        try:
            for i in range(len(self.atomo)):
                entrada_atomos.append(self.atomo[i].get().capitalize())
                x = self.n_atomos[i].get()
                numero_atomos.append(int(x))
        except:
            messagebox._show("Erro", "Adicione as espécies atomicas e a"
                                     " quantidade para cada um deles")
        self.iniciaEC(entrada_atomos, numero_atomos)

    def calculaEF(self):
        entrada_atomos = []
        numero_atomos = []

        try:
            for i in range(len(self.atomo)):
                entrada_atomos.append(self.atomo[i].get().capitalize())
                x = self.n_atomos[i].get()
                numero_atomos.append(int(x))
        except:
            messagebox._show("Erro", "Adicione as espécies atomicas e a"
                                     " quantidade para cada um deles")
        self.iniciaEF(entrada_atomos, numero_atomos)

if __name__ == '__main__':
    gui = Interface()


