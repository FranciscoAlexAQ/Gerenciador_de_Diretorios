from tkinter import * 
from Pesquisa import Pesquisa

class Main:
    def __init__(self):
        self.root = Tk()
        self.configurarTela()
        self.criarEntrysLabels()
        self.crarOptionMenu()
        self.root.mainloop()
    
    def configurarTela(self):
        self.root.title('Gerenciador de Arquivos')
        self.root.geometry('350x350+600+50')

    def criarEntrysLabels(self):
        self.nomeArquivo = Label(self.root, text='Nome', font=('Times BOLD', 10))
        self.nomeArquivo.place(relx=0.4, rely=0.05)
        self.entryNomeArquivo = Entry(self.root, justify=CENTER)
        self.entryNomeArquivo.place(relx=0.25, rely=0.14, relwidth=0.5)

        self.selectTipo = Label(self.root, text='O que deseja buscar? ')
        self.selectTipo.place(relx=0.3, rely=0.25)

        self.nome = Label(self.root, text='Nome', font=('Times BOLD', 10))
        self.nome.place(relx=0.2, rely=0.47)
        self.entryNome = Entry(self.root, justify=CENTER)
        self.entryNome.place(relx=0.35, rely=0.47, relwidth=0.5)
        
        self.tamanho = Label(self.root, text='Tamanho (Bytes)', font=('Times BOLD', 10))
        self.tamanho.place(relx=0.2, rely=0.55)
        self.entryTamanho = Entry(self.root, justify=CENTER)
        self.entryTamanho.place(relx=0.52, rely=0.55, relwidth=0.2)


        self.caminho = Label(self.root, text='Caminho', font=('Times BOLD', 10))
        self.caminho.place(relx=0.2, rely=0.63)
        self.entryCaminho = Entry(self.root, justify=CENTER)
        self.entryCaminho.place(relx=0.4, rely=0.63, relwidth=0.5)

        self.btn = Button(self.root, text='PROCURAR', command=self.mostrarResultadoPesquisa)
        self.btn.place(relx=0.3, rely=0.75, relwidth=0.4)

        self.mensagem = Label(self.root, text='ESSA AÇÃO PODE DEMORAR UM POUCO', 
            font=('Times BOLD', 10))
        self.mensagem.place(relx=0.1, rely=0.9)

    def crarOptionMenu(self):
        self.escolha = StringVar()
        self.escolha.set('Pasta')
        self.lista = ['Pasta', 'Arquivo']

        self.escolhaTipo = OptionMenu(self.root, self.escolha, *self.lista)
        self.escolhaTipo.place(relx=0.25, rely=0.32, relwidth=0.5)

    def mostrarResultadoPesquisa(self):
        self.dados = Pesquisa()
        aux = self.dados.pesquisar(self.entryNomeArquivo.get(), self.escolha.get())

        self.entryNome.delete(0, END)
        self.entryTamanho.delete(0, END)
        self.entryCaminho.delete(0, END)

        for i in range(3):
            if i == 0:
                self.entryNome.insert(END, aux[i])
            elif i == 1:
                self.entryTamanho.insert(END, aux[i])
            else:
                self.entryCaminho.insert(END, aux[i])
        
        self.entryNomeArquivo.delete(0, END)

Main()
