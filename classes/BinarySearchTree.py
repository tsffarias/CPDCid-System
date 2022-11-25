'''
Arvore Binaria de Busca
Referencia 1:  https://youtu.be/f5dU3xoE6ms
Referencia 2:  https://youtu.be/Zaf8EOVa72I
Referencia 3:  https://youtu.be/z0Ho8nMNlAM

Tanto o método de inserção iterativa quanto recursiva funcionam
contudo, para inserção ordenada muito grande, a recursiva estoura
o limite de profundidade de recursão da linguagem
'''

from classes.Car import Car

dados_bst = []

class node:
    def __init__(self, value=None, car=None):
        self.value = value
        self.car = car
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
        self.last_visited_node = None # saves the last entrypoint to get deeper operations


class BinarySearchTree:
    def __init__(self):
        self.root = None

    #inserção iterativa
    def insert(self, value, car):
        if self.root == None:
            self.root = node(value, car)
            self.root.last_visited_node = self.root
            return
        
        root = self.root
        
        while True:
            
            
            if value < root.value:
                if root.left_child != None: 
                    if (value < self.root.last_visited_node.value):
                        root = self.root.last_visited_node
                    else:
                        root = root.left_child        
                else:
                    root.left_child=node(value, car)
                    root.left_child.parent = root
                    self.root.last_visited_node = root.left_child
                    break
            elif value >= root.value:
                if root.right_child != None:
                    if (value >= self.root.last_visited_node.value):
                        root = self.root.last_visited_node
                    else:
                        root = root.right_child
                else:
                    root.right_child=node(value, car)
                    root.right_child.parent = root
                    self.root.last_visited_node = root.right_child
                    break

    # inserção recursiva @thiago
    # def insert(self, value, car):
    #     if self.root == None:
    #         self.root = node(value, car)
    #     else:
    #         self._insert(value, car, self.root)

    # def _insert(self, value, car, cur_node):
    #     if value < cur_node.value:
    #         if cur_node.left_child == None:
    #             cur_node.left_child = node(value, car)
    #             cur_node.left_child.parent = cur_node  # set parent
    #         else:
    #             self._insert(value, car, cur_node.left_child)
    #     elif value > cur_node.value:
    #         if cur_node.right_child == None:
    #             cur_node.right_child = node(value, car)
    #             cur_node.right_child.parent = cur_node  # set parent
    #         else:
    #             self._insert(value, car, cur_node.right_child)
    #     else:
    #         print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            #print(f'key = {str(cur_node.value)} / car = {str(cur_node.car)}  / height = {cur_node.height}')
            dados_bst.append(str(cur_node.car))
            self._print_tree(cur_node.right_child)

    def preparando_salvamento_dados(self):
        self.print_tree()
        return dados_bst

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            #print("Node to be deleted not found in the tree!")
            return -1
        # -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False

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
        if self.root != None:
            for ano in range(int(ano_inicial), int(ano_final)+1):
                self._relatorio_intervalo_tempo(self.root, ano, 'padrão antigo')
                self._relatorio_intervalo_tempo(self.root, ano, 'padrão mercosul')
        else:
            print('Arvore binaria de busca vazia')

    def _relatorio_intervalo_tempo(self, cur_node, ano, padrao_placa):
        if cur_node != None:
            self._relatorio_intervalo_tempo(
                cur_node.left_child, ano, padrao_placa)
            if int(cur_node.car.ano_frabricacao) == int(ano) and cur_node.car._padrao_placa.lower() == padrao_placa:
                self.carro_info(cur_node.car)
            self._relatorio_intervalo_tempo(
                cur_node.right_child, ano, padrao_placa)

    def relatorio_estadual_final_placa(self, uf):
        if (Car().validation_uf(uf)):
            if self.root != None:
                self._relatorio_estadual_final_placa(self.root, uf, 'padrão antigo')
                self._relatorio_estadual_final_placa(self.root, uf, 'padrão mercosul')
            else:
                print('Arvore binaria de busca vazia')
        else:
            print('UF inválido, por favor tente novamente.')
    
    def _relatorio_estadual_final_placa(self, cur_node, uf, padrao_placa):
        if cur_node != None:
            self._relatorio_estadual_final_placa(
                cur_node.left_child, uf, padrao_placa)
            if cur_node.car.estado == uf.upper() and cur_node.car._padrao_placa.lower() == padrao_placa:
                self.carro_info(cur_node.car)
            self._relatorio_estadual_final_placa(
                cur_node.right_child, uf, padrao_placa)

