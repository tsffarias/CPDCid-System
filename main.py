from classes.Car import Car
from classes.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada
from classes.TabelaDispercao import TabelaDispercao
from services.Read_write_file import Read_write_file
from services.Time_execution import Time_execution

'''
Grupo: Thiago, Eduardo, Quirino, Biel
Título: CPDCID: PYTHON - Estrutura de Dados 2022
'''

def space():
    print("")


def menu_estrutura_de_dados():
    print("Opção 1 - Lista Duplamente Encadeada")
    print("Opção 2 - Tabela de Disperção (Encadeamento Externo)")
    print("Opção 3 - Em Desenvolvimento")
    print("Opção 4 - Em Desenvolvimento")
    print("_______________________")
    space()

def menu():
    print("Opção 1 - Pesquisar Carro")
    print("Opção 2 - Remover Carro")
    print("Opção 3 - Imprimir Toda Lista")
    print("Opção 4 - Sair do programa")
    print("_______________________")
    space()


def load_data(estrutura_de_dados, tipo_estrutura):
    start_time = Time_execution.start_time()  # capturando tempo inicial
    Read_write_file.read_file(estrutura_de_dados, tipo_estrutura) # lendo arquivo e armazenando em estrutura de dado
    end_time = Time_execution.end_time()  # capturando tempo final
    
    # calculando o tempo de execucao
    Time_execution.calculate_time_execution(start_time, end_time, 'Carregamento de Dados')
    #return lista_duplamente_encadeada
    return estrutura_de_dados

if __name__ == '__main__':

    # escolhendo estrutura de dados
    menu_estrutura_de_dados()
    resposta_usuario = int(input('❐ Informe a sua opção de Estrutura de Dados (1 a 4): '))
    if resposta_usuario == 1:
        estrutura_de_dados = ListaDuplamenteEncadeada()
        tipo_estrutura = 'lista_duplamente_encadeada'
    elif resposta_usuario == 2:
        estrutura_de_dados = TabelaDispercao()
        tipo_estrutura = 'tabela_dispercao'

    estrutura_de_dados = load_data(estrutura_de_dados, tipo_estrutura)

    while (True):

        space()
        print("CPDCID: PYTHON")
        print(f'Estrutura de Dados: {tipo_estrutura}')
        space()
        
        menu()
        # escolhendo operação
        resposta_usuario = int(input('❐ Informe a sua opção (1 a 4): '))
        
        if resposta_usuario == 4:
            print('Programa finalizado!')
            break
        elif resposta_usuario == 1:
            print(resposta_usuario)
        elif resposta_usuario == 2:
            print(resposta_usuario)
        elif resposta_usuario == 3:
            estrutura_de_dados.imprimir_estrutura_de_dados() # imprimindo carros
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
