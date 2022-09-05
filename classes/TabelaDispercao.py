'''
Hashmap - Tabela de Disperção(Encadeamento Externo)
Hashfunction: Soma(ascii de cada caracter da placa) MOD tamanho da tabela de disperção
Referencia 1: https://youtu.be/ea8BRGxGmlA
Referencia 2: https://youtu.be/54iv1si4YCM
'''

class TabelaDispercao:
    def __init__(self):
        self.MAX = 64
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: # quando a mesma chave é encontrada, a chave e o valor da tupla são editados
                self.arr[h][index] = (key, val)
                found = True
        if not found: # quando a chama não é encontrada, a tupla com a chave e valor são adicionados no hashmap
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                carro = self.arr[arr_index][index]
                del self.arr[arr_index][index]
                return carro

    def edit_item(self):
        pass

    def imprimir_estrutura_de_dados(self):
        for element in self.arr:
            if len(element):
                for i in element:
                    print(i[1].__str__())

    def carro_info(self, carro):
        print("_______________________")
        print(f'Placa: {carro.placa}')
        print(f'Padrão Placa: {carro.padrao_placa}')
        print(f'Renavam: {carro.renavam}')
        print(f'Marca: {carro.marca}')
        print(f'Modelo: {carro.modelo}')
        print(f'Ano Fabricação: {carro.ano_frabricacao}')
        print(f'Cor: {carro.cor}')
        print(f'Categoria: {carro.categoria}')
        print(f'Estado: {carro.estado}')
        print(f'Cidade: {carro.cidade}')
        print("_______________________")
        print("")

    def relatorio_intervalo_tempo(self, ano_inicial, ano_final):
        num_cars = 0
        for element in self.arr:
            if len(element):
                for carro in element:
                    if carro[1].ano_frabricacao >= ano_inicial and carro[1].ano_frabricacao <= ano_final:
                        self.carro_info(carro[1])
                        num_cars += 1
        print(f'Número total de carros entre os anos {ano_inicial} e {ano_final}: {num_cars}\n')

'''
t = TabelaDispercao()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457

print(t["march 6"])
print(t["march 17"])
print(t.arr)
t["march 6"] = 11 # editando
print(t.arr)
print(t["march 6"])
del t["march 6"]
print(t.arr)

#print(estrutura_de_dados.imprimir_estrutura_de_dados())
#print(estrutura_de_dados.__delitem__('IDE6N11'))
#print(estrutura_de_dados.arr)

# cz commit
'''

