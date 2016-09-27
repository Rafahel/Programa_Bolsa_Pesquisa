from tkinter import *
from Handler import Handler
from Calculo import Calculo
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from tkinter import PhotoImage
from matplotlib import *
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as p
import numpy
import numpy
import os
#  Esta interface foi criada utilizando o Módulo tkinter, o programa asseguir serve para realizar os
#  calculos de energia de coesão e formacão.

# v 0.6

# Gerar graficos OK

#  Criado por Rafahel Mello aluno de Ciência da computacão da Universidade Regional Integrada de Santo Ângelo
class Interface:

    def __init__(self): # Inicializacão da interface do programa

        self.raiz = Tk()
        print("formação".upper())
        self.raiz.title("Calculadora CeF 1.1")
        self.raiz.geometry("650x800")  # Tamanho da janela
        self.raiz.resizable(width=False, height=False)  # Se a janela pode ser redimencionada
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
        self.botaoCalcularEC = Button(self.raiz, text="Calcular Energia de Coesão", command=self.calculaEC, state=DISABLED)
        self.botaoCalcularEF = Button(self.raiz, text="Calcular Energia de formação", command=self.calculaEF, state=DISABLED)
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
            #print(self.arquivo)
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

    def geraGrafico(self): # Funcão responsavel por gerar grafico onde x = volume y = resultado
        if self.ec:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                # self.resultado = sorted(self.resultado)
                # self.volume = sorted(self.volume)
                plt.title("Calculo de energia de coesão")
                plt.ylabel("Energia de coesão")
                plt.xlabel("Volume")
                # plt.plot(self.volume, self.resultado)
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                # plt.ylabel("Energia de coesão")
                # plt.xlabel("Volume")
                # plt.plot(self.volume, self.resultado)
                # plt.show()

        if self.ef:
            if len(self.resultado) > 0 and len(self.volume) == len(self.resultado):
                # self.resultado = sorted(self.resultado)
                # self.volume = sorted(self.volume)
                plt.title("Calculo de energia de formação")
                plt.xlabel("Energia de formação")
                plt.ylabel("Volume")
                # plt.plot(self.volume, self.resultado)
                plt.scatter(self.volume, self.resultado, color='r')
                plt.show()
                # plt.xlabel("Energia de formacão")
                # plt.ylabel("Volume")
                # plt.plot(self.volume, self.resultado)
                # plt.show()

        self.raiz.quit()


    def iniciaEC(self, entrada_atomos, numero_atomos):  # Método que da inicio ao cálculo
        self.ec = True
        self.ef = False
        self.soma = Handler(entrada_atomos, numero_atomos)
        self.somatorioEnergiaAtomoLivre = self.soma.somatorioEATML()  # Resultado do somatorio de EATML
        self.calc = Calculo(self.energia, self.somatorioEnergiaAtomoLivre, 0)
        self.resultado = self.calc.calculo_energia_coesao()
        #print(self.resultado)
        self.geraArquivo()

    def iniciaEF(self, entrada_atomos, numero_atomos):  # Método que da inicio ao cálculo
        self.ef = True
        self.ec = False
        self.soma = Handler(entrada_atomos, numero_atomos)
        self.somatorioEnergiaCristalina = self.soma.somatorioECRYS()  # Resultado do somatorio de ECRYS
        self.calc = Calculo(self.energia, 0, self.somatorioEnergiaCristalina)
        self.resultado = self.calc.calculo_energia_formacao()
        # print(self.x)
        self.geraArquivo()

    def escolherArquivo(self):  # Método para escolher arquivo apartir de um botão na GUI
        self.arquivo = ""
        self.energia.clear()
        self.volume.clear()
        self.arquivo = str(askopenfile("r"))
        # print(arquivo)
        # As próximas 3 linhas retiram a parte que não é necessário da string que contem o caminho do arquivo
        self.arquivo = self.arquivo.replace("<_io.TextIOWrapper name='", "")
        self.arquivo = self.arquivo.replace("' mode='r' encoding='cp1252'>", "")
        self.arquivo = self.arquivo.replace("' mode='r' encoding='UTF-8'>", "")
        # arquivo = arquivo + ".txt"
        #print(self.arquivo)
        arq = open(self.arquivo)
        try:
            texto = arq.readlines()
            # print(texto)
            # print(type(texto))
            # print("Tamanho texto = " + format(len(texto)))
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
        x = int(self.qtd_atomos.get())
        r = 3
        if x > 100 or x < 0:
            return
        for i in range(x):
            # print(i)
            self.atomo.append(Entry(self.raiz))
            self.n_atomos.append(Entry(self.raiz))
        # print(len(atomo))
        for i in range(x):
            self.atomo[i].grid(row=r, column=0)
            self.n_atomos[i].grid(row=r, column=2)
            r += 1
        self.escolher_arquivo.grid(row=r, column=4)
        r += 1
        self.botaoCalcularEC.grid(row=r, column=4)
        r += 1
        self.botaoCalcularEF.grid(row=r, column=4)
        # self.qtd_atomos.configure(state=DISABLED)
        # self.adc_entrada_atomo.configure(state=DISABLED)
        self.adc_entrada_atomo.grid_remove()
        self.qtd_atomos.grid_remove()
        self.entry_desc.config(text="Espécie atômica")
        self.n_atomos_desc.config(text="Número de átomos")


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
        # print(entrada_atomos)
        # print(numero_atomos)
        # print(type(numero_atomos[0]))
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
            # print(entrada_atomos)
            # print(numero_atomos)
            # print(type(numero_atomos[0]))
        self.iniciaEF(entrada_atomos, numero_atomos)

gui = Interface()

# def compute():
#     date = dataent.get()
#     weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#     dia = ('{} foi {}'.format(date, weekday))
#     dataent.delete(0, END)
#     dataent.insert(0, dia)
# def clear():
#     dataent.delete(0,END)
# raiz = Tk()
# texto = Label(raiz,text="Entre com uma data:")
# botao = Button(master=raiz, text="Entrar", command=compute)
# botaoDel = Button(master=raiz, text="Delete", command=clear)
# dataent = Entry(raiz)
# texto.grid(row=0,column=0)
# dataent.grid(row=0,column=1)
# botao.grid(row=1,column=0,columnspan=2)
# botaoDel.grid(row=1,column=0,columnspan=1)
# raiz.mainloop()




# def compute():
#     date = dataent.get()
#     weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#     showinfo(message='{} foi {}'.format(date, weekday))
#     dataent.delete(0, END)
#
# raiz = Tk()
# texto = Label(raiz,text="Entre com uma data:")
# botao = Button(master=raiz, text="Entrar", command=compute)
# dataent = Entry(raiz)
# texto.grid(row=0,column=0)
# dataent.grid(row=0,column=1)
# botao.grid(row=1,column=0,columnspan=2)




# def cliked():
#     hora = strftime("Dia: %d %b %Y\nHora: %H:%M:%S %p\n", localtime())
#     showinfo(message=hora)
# def green():
#     hora = strftime("Dia: %d %b %Y\nHora: %H:%M:%S %p\n", gmtime())
#     showinfo(message=hora)
# raiz = Tk()
#
# botao = Button(master=raiz, text="Clique aqui", command=cliked)
# botao2 = Button(master=raiz, text="Clique aqui2", command=cliked)
# botao.pack()
# botao2.pack()



# labels = [['1', '2', '3'],  # textos de label do teclado
#           ['4', '5', '6'],  # organizados em uma grade
#           ['7', '8', '9'],
#           ['*', '0', '#']]
# print(type(labels))
# for r in range(4):  # para cada linha r = 0, 1, 2, 3
#     for c in range(3):  # para cada coluna c = 0, 1, 2
#         # cria label para linha r e coluna c
#         label = Label(raiz,
#         relief = RAISED,  # borda elevada
#         padx = 10,  # torna label largo
#         text = labels[r][c])  # texto do label
#         # coloca label na linha r e coluna c
#         label.grid(row=r, column=c)












# imagem = PhotoImage(file="imagem.png")
# place = Label(master=raiz, image=imagem, width=300, height=180)
# place.pack(side=RIGHT)
# texto = Label(raiz,
#             font = ('Helvetica', 16, 'bold italic'),
#             foreground='white',   # cor da letra
#             background='red',   # cor do fundo
#             padx=25,  # expande label 25 pixels para esquerda e direita
#             pady=78,  # amplia label 10 pixels acima e abaixo
#             text='A paz começa com um sorriso.')
# texto.pack(expand=False,fill="none",side=LEFT)
