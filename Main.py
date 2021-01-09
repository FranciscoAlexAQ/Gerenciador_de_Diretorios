from tkinter import * 
from Pesquisa import Pesquisa
from tkinter import messagebox

import time


class Main:
    def __init__(self):
        self.root = Tk()
        self.configurarTela()
        self.criarEntrysLabels()
        self.crarOptionMenu()
        self.root.mainloop()

    def configurarTela(self):
        self.root.title('Gerenciador de Arquivos')
        self.root.geometry('450x500+500+50')
        self.root.config(bg='#2F4F4F')

    def criarEntrysLabels(self):
        self.nomeArquivo = Label(self.root, text='NOME DO ARQUIVO COM A EXTENSÃO',
                                 font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.nomeArquivo.place(relx=0.23, rely=0.05)
        self.entryNomeArquivo = Entry(self.root, justify=CENTER)
        self.entryNomeArquivo.place(relx=0.25, rely=0.14, relwidth=0.5, relheight=0.05)

        self.selectTipo = Label(self.root, text='ESCOLHA O QUE DESEJA PESQUISAR',
                                font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.selectTipo.place(relx=0.23, rely=0.25)

        self.nome = Label(self.root, text='Nome', font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.nome.place(relx=0.1, rely=0.55)
        self.entryNome = Entry(self.root, justify=CENTER)
        self.entryNome.place(relx=0.23, rely=0.55, relwidth=0.5,  relheight=0.05)
        
        self.tamanho = Label(self.root, text='Tamanho (Bytes)', font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.tamanho.place(relx=0.1, rely=0.67)
        self.entryTamanho = Entry(self.root, justify=CENTER)
        self.entryTamanho.place(relx=0.4, rely=0.67, relwidth=0.3, relheight=0.05)

        self.caminho = Label(self.root, text='Caminho', font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.caminho.place(relx=0.1, rely=0.77)
        self.entryCaminho = Entry(self.root, justify=CENTER)
        self.entryCaminho.place(relx=0.25, rely=0.77, relwidth=0.5, relheight=0.05)

        self.btn = Button(self.root, text='PROCURAR', bd=3,
                          highlightbackground='purple',
                          highlightthickness=3, command=self.mostrarResultadoPesquisa)
        self.btn.place(relx=0.3, rely=0.43, relwidth=0.4)

        self.mensagem = Label(self.root, text='ESSA AÇÃO PODE DEMORAR UM POUCO', 
            font=('Times BOLD', 10), bg='#2F4F4F', fg='#fff')
        self.mensagem.place(relx=0.2, rely=0.9)

    def crarOptionMenu(self):
        self.escolha = StringVar()
        self.lista = ['Pasta', 'Arquivo']
        self.escolha.set('Pasta')

        self.escolhaTipo = OptionMenu(self.root, self.escolha, *self.lista)
        self.escolhaTipo.place(relx=0.25, rely=0.32, relwidth=0.5)
        self.escolhaTipo['bd'] = 0

    def mostrarResultadoPesquisa(self):
        self.entryNome.delete(0, END)
        self.entryTamanho.delete(0, END)
        self.entryCaminho.delete(0, END)

        self.dados = Pesquisa.pesquisar(self, self.entryNomeArquivo.get(), self.escolha.get())

        print(self.dados)

        if not self.dados:
            messagebox.showinfo('Nada Encontrado', 'Nenhum dado foi encontrado')
            self.entryNomeArquivo.delete(0, END)
        else:
            for dado in self.dados:
                self.entryNome.insert(END, dado[0])
                self.entryTamanho.insert(END, dado[1])
                self.entryCaminho.insert(END, dado[2])
       
Main()
