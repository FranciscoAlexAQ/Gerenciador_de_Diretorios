import os

class Pesquisa:
    def pesquisar(self, dados, tipo='Arquivo'):
        self.encontrado = 0 
        if tipo == 'Pasta':
            while self.encontrado == 0:
                for self.diretorios, self.pastas, self.Arquivos in os.walk(r'C:\\'):
                    if dados in self.pastas:
                        self.encontrado += 1
                        for pasta in self.pastas:
                            if pasta == dados:
                                self.nome = pasta 
                                self.tamanho = os.path.getsize(self.diretorios + '\\' + pasta)
                                self.caminho = self.diretorios
                               
                if self.encontrado == 0:
                    self.nome = ''
                    self.tamanho = ''
                    self.caminho = ''
                    break
        else:
            while self.encontrado == 0:
                for self.diretorios, self.pastas, self.Arquivos in os.walk(r'C:\\'):
                    if dados in self.Arquivos:
                        self.encontrado += 1
                        for arquivo in self.Arquivos:
                            if arquivo == dados:
                                self.nome = arquivo
                                self.tamanho = os.path.getsize(self.diretorios + '\\' + arquivo)
                                self.caminho = self.diretorios
                               
                if self.encontrado == 0:
                    self.nome = ''
                    self.tamanho = ''
                    self.caminho = ''
                    break
        return [self.nome, self.tamanho, self.caminho]


if __name__ == '__main__':
    dado = Pesquisa()

    print(dado.pesquisar('arquivos.py'))
