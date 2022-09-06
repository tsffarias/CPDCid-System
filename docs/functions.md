# Indice de funções


## main.py
carro_coleta_dados(placa)

load_data(estrutura_de_dados, tipo_estrutura)

menu()

menu_estrutura_de_dados()

space()


## class Celula(builtins.object)

Celula(conteudo)

Methods defined here:

\_\_init\_\_(self, conteudo)

Initialize self.  See help(type(self)) for accurate signature.

Data descriptors defined here:

\_\_dict\_\_

dictionary for instance variables (if defined)

\_\_weakref\_\_

list of weak references to the object (if defined)


## class ListaDuplamenteEncadeada(builtins.object)
Methods defined here:

\_\_init\_\_(self)

Initialize self.  See help(type(self)) for accurate signature.

busca(self, valor)

carro_info(self, carro)

imprimir_estrutura_de_dados(self)

inserir(self, posicao, conteudo)

inserir_no_fim(self, conteudo)

inserir_no_inicio(self, conteudo)

item(self, posicao)

remover(self, posicao)

remover_do_fim(self)

remover_do_inicio(self)

Readonly properties defined here:

fim

inicio

quantidade

Data descriptors defined here:

\_\_dict\_\_

dictionary for instance variables (if defined)

\_\_weakref\_\_

list of weak references to the object (if defined)

## class TabelaDispercao(builtins.object)

Hashmap - Tabela de Disperção(Encadeamento Externo)
Hashfunction: Soma(ascii de cada caracter da placa) MOD tamanho da tabela de disperção
Referencia 1: https://youtu.be/ea8BRGxGmlA
Referencia 2: https://youtu.be/54iv1si4YCM

### Methods defined here:
\_\_delitem\_\_(self, key)

\_\_getitem\_\_(self, key)

\_\_init\_\_(self)

Initialize self.  See help(type(self)) for accurate signature.

\_\_setitem\_\_(self, key, val)

carro_info(self, carro)

edit_item(self)

get_hash(self, key)

imprimir_estrutura_de_dados(self)

relatorio_estadual_final_placa(self, uf, placa)

-validar o UF e usar o search # https://stackabuse.com/python-check-if-string-contains-substring/

relatorio_intervalo_tempo(self, ano_inicial, ano_final)

Data descriptors defined here:

\_\_dict\_\_

dictionary for instance variables (if defined)

\_\_weakref\_\_

list of weak references to the object (if defined)

## class Vehicle(builtins.object)
   	Vehicle(placa=None, padrao_placa=None, renavam=None, marca=None, modelo=None, ano_frabricacao=None, cor=None, categoria=None, estado=None, cidade=None)
 

 
Methods defined here:

\_\_init\_\_(self, placa=None, padrao_placa=None, renavam=None, marca=None, 
modelo=None, ano_frabricacao=None, cor=None, categoria=None, estado=None, cidade=None)
Initialize self.  See help(type(self)) for accurate signature.

\_\_str\_\_(self)
    Return str(self).
    Data descriptors defined here:

\_\_dict\_\_
dictionary for instance variables (if defined)

\_\_weakref\_\_

list of weak references to the object (if defined)

ano_frabricacao

categoria

cidade

cor

estado

marca

modelo

padrao_placa

placa

renavam





-- criando com pydoctor