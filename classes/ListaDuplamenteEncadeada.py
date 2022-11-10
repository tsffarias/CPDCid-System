'''
Lista Duplamente Encadeada - Doubly linked list
Referencia: https://github.com/DarlanNoetzold/Estrutura_de_Dados/blob/main/ListaDuplamenteLigada/aula2/ed/ed/lista_duplamente_ligada.py
'''
from classes.Car import Car

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

    def imprimir_estrutura_de_dados(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def preparando_salvamento_dados(self):
        atual = self.inicio
        dados_estrutura = []
        for i in range(0, self.quantidade):
            dados_estrutura.append(str(atual.conteudo))
            atual = atual.proximo

        return dados_estrutura

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

    def __delitem__(self, posicao):
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

    def item(self, posicao):
        celula = self._celula(posicao) 
        return celula.conteudo

    def __edititem__(self, placa, carro):        
        celula = self.inicio
        for i in range(0, self.quantidade):
            if placa == celula.conteudo.placa:
                celula.conteudo = carro
                return True
            celula = celula.proximo
        return None

    def __getitem__(self, placa):
        celula = self.inicio
        posicao = 0
        for i in range(0, self.quantidade):
            if placa == celula.conteudo.placa:
                break
            celula = celula.proximo
            posicao += 1

        return [celula, posicao]

    def carro_info(self, carro):
        print("_______________________")
        print(f'Placa: {carro.conteudo.placa}')
        print(f'Padrão Placa: {carro.conteudo.padrao_placa}')
        print(f'Renavam: {carro.conteudo.renavam}')
        print(f'Marca: {carro.conteudo.marca}')
        print(f'Modelo: {carro.conteudo.modelo}')
        print(f'Ano Fabricação: {carro.conteudo.ano_frabricacao}')
        print(f'Cor: {carro.conteudo.cor}')
        print(f'Categoria: {carro.conteudo.categoria}')
        print(f'Estado: {carro.conteudo.estado}')
        print(f'Cidade: {carro.conteudo.cidade}')
        print("_______________________")
        print("")
        

    def relatorio_intervalo_tempo(self, ano_inicial, ano_final):
        if self.quantidade != 0:
            for ano in range(int(ano_inicial), int(ano_final)+1):
                self._relatorio_intervalo_tempo(ano, 'padrão antigo')
                self._relatorio_intervalo_tempo(ano, 'padrão mercosul')
        else:
            print('Lista Duplamente Encadeada Vazia')

    def _relatorio_intervalo_tempo(self, ano, padrao_placa):
        num_cars = 0
        atual = self.inicio
        for i in range(0, self.quantidade):
            if int(atual.conteudo.ano_frabricacao) == int(ano) and atual.conteudo._padrao_placa.lower() == padrao_placa:
                self.carro_info(atual)
                num_cars += 1
            atual = atual.proximo

    def relatorio_estadual_final_placa(self, uf):
        if (Car().validation_uf(uf)):
            if self.quantidade != 0:
                self._relatorio_estadual_final_placa(uf, 'padrão antigo')
                self._relatorio_estadual_final_placa(uf, 'padrão mercosul')
            else:
                print('Lista Duplamente Encadeada Vazia')
        else:
            print('UF inválido, por favor tente novamente.')

    def _relatorio_estadual_final_placa(self, uf, padrao_placa):
        atual = self.inicio
        for i in range(0, self.quantidade):
            if atual.conteudo.estado == uf.upper() and atual.conteudo._padrao_placa.lower() == padrao_placa:
                self.carro_info(atual)
            atual = atual.proximo



