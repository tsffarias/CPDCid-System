class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim

    @property
    def quantidade(self):
        return self._quantidade


    #@TODO: terminar relatório
    def imprimir_estrutura_de_dados(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def inserir_no_inicio(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.proximo = self.inicio
        self._inicio.anterior = celula
        self._inicio = celula
        self._quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)

        celula = Celula(conteudo)
        celula.anterior = self.fim
        self.fim.proximo = celula
        self._fim = celula
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            return self.inserir_no_inicio(conteudo)

        if posicao == self.quantidade:
            return self.inserir_no_fim(conteudo)

        esquerda = self._celula(posicao-1)
        direita = esquerda.proximo
        celula = Celula(conteudo)
        celula.proximo = direita
        celula.anterior = esquerda
        esquerda.proximo = celula
        direita.anterior = celula
        self._quantidade += 1

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida: {}".format(posicao))

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        metade = self.quantidade // 2
        if posicao < metade:
            atual = self.inicio
            for i in range(0, posicao):
                atual = atual.proximo
            return atual
        atual = self.fim

        for i in range(posicao+1, self.quantidade)[::-1]:
            atual = atual.anterior
        return atual

    def _remover_ultimo(self):
        if self.quantidade == 1:
            removido = self.inicio
            self._inicio = None
            self._fim = None
            self._quantidade -= 1
            return removido.conteudo

    def remover_do_inicio(self):
        if self.quantidade == 1:
            return self._remover_ultimo()

        removido = self.inicio
        self._inicio = removido.proximo
        self._inicio.anterior = None
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover_do_fim(self):
        if self.quantidade == 1:
            return self._remover_ultimo()

        removido = self.fim
        self._fim = removido.anterior
        self._fim.proximo = None
        removido.anterior = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_do_inicio()

        if posicao == self.quantidade - 1:
            return self.remover_do_fim()

        removido = self._celula(posicao)
        esquerda = removido.anterior
        direita = removido.proximo
        removido.proximo = None
        removido.anterior = None
        esquerda.proximo = direita
        direita.anterior = esquerda
        self._quantidade -= 1

        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)        
        return celula.conteudo
    
    def busca(self, valor):
        celula = self.inicio
        while celula and (valor not in str(celula.conteudo)):
            celula = celula.proximo
        return celula

    def buscaPlacaAntiga(self, placa):
        letras = {
            "0" : "A", "1" : "B", "2" : "C", "3" : "D", "4" : "E",
            "5" : "F", "6" : "G", "7" : "H", "8" : "I", "9" : "J",
            }
        try:
            placa = list(placa)
            letra = placa.pop(4)
            placa.insert(4, letras.get(letra))
            placa = ''.join(map(str, placa))
            return placa
        except Exception:
            return


    def buscaPlaca(self, valor):
        resultBusca = self.busca(valor)
        if(resultBusca):
            return resultBusca
        else:
            placa = self.buscaPlacaAntiga(valor)
            resultBusca = self.busca(placa)
            if(resultBusca):
                print("Placa constando como: {}".format(placa))
                return resultBusca
            else:
                return 


    def carro_info(self, carro):
        print("")
        print(f'\033[92m\033[1mPlaca:\033[0m {carro.conteudo.placa}\t\033[92m\033[1mPadrão Placa:\033[0m {carro.conteudo.padrao_placa}\t\033[92m\033[1mRenavam:\033[0m {carro.conteudo.renavam}')
        print(f'\033[92m\033[1mMarca:\033[0m {carro.conteudo.marca}\t\033[92m\033[1mModelo:\033[0m {carro.conteudo.modelo}\t\033[92m\033[1m Ano Fab:\033[0m {carro.conteudo.ano_frabricacao}')
        print(f'\033[92m\033[1mCor:\033[0m {carro.conteudo.cor}\t\033[92m\033[1mCategoria:\033[0m {carro.conteudo.categoria}\t\033[92m\033[1mEstado:\033[0m {carro.conteudo.estado}\t\033[92m\033[1mCidade:\033[0m {carro.conteudo.cidade}')
        print("_______________________")
        print("")
