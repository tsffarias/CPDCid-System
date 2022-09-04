class HashTable:
    def __init__(self):
        self.MAX = 10
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
                print("del", index)
                del self.arr[arr_index][index]


t = HashTable()
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
