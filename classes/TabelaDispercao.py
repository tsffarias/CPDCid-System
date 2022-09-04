'''
Hashmap - Tabela de Disperção (Encadeamento Externo)
Hashfunction: Soma(ascii de cada caracter da placa) MOD tamanho da tabela de disperção
'''

class TabelaDispercao:
 
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    # hash function
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # adicionando elemento ao hashmap
    def __setitem__(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[key_hash].append(key_value)
                return True

    # pesquisando elemento no hashmap
    def __getitem__(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # removendo elemento no hashmap
    def __delitem__(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = TabelaDispercao()
h.__setitem__('Bob', '567-8888')
h.__setitem__('Ming', '293-6753')
h.__setitem__('Ming', '333-8233')
h.__setitem__('Ankit', '293-8625')
h.__setitem__('Aditya', '852-6551')
h.__setitem__('Alicia', '632-4123')
h.__setitem__('Mike', '567-2188')
h.__setitem__('Aditya', '777-8888')
h.print()
h.__delitem__('Bob')
h.print()
print('Ming: ' + h.__getitem__('Ming'))
print(h.keys())


