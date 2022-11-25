
#from classes.Car import Car

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char, car=None):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # inserting car
        self.car = car 

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word, car):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char, car)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True
        node.car = car

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.car, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[0], reverse=True)

    def dfs_relatorio_uf(self, node, prefix, uf):
        if node.is_end:
            if node.car.estado == uf.upper():
                self.output.append((prefix + node.char, node.car, node.counter))

        for child in node.children.values():
            self.dfs_relatorio_uf(child, prefix + node.char, uf)

    def relatorio_estadual_final_placa(self, x, uf):
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs_relatorio_uf(node, x[:-1], uf)

        for car in self.output:
            self.carro_info(car[1])

    def dfs_relatorio_intervalo_tempo(self, node, prefix, ano_inicial, ano_final):
        if node.is_end:
            print('test1')
            if node.car.ano_frabricacao >= int(ano_inicial) and node.car.ano_frabricacao <= int(ano_final):
                self.output.append(
                    (prefix + node.char, node.car, node.counter))

        for child in node.children.values():
            self.dfs_relatorio_intervalo_tempo(
                child, prefix + node.char, ano_inicial, ano_final)

    def relatorio_intervalo_tempo(self, x, ano_inicial, ano_final):
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
    
        # Traverse the trie to get all candidates
        self.dfs_relatorio_intervalo_tempo(
            node, x[:-1], ano_inicial, ano_final)

        for car in self.output:
            self.carro_info(car[1])

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


#t = Trie()
#print(t.insert("FBI3643"))
#print(t.insert("word"))
#print(t.insert("HHJ7690"))
#print(t.insert("what"))
#print(t.insert("LDG3297"))
#print(t.query(""))

test = [('HGM8629', 'testizinho', 1)]
print(test[0][1])
