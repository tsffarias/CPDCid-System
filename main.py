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
    print("Opção 3 - Editar Carro")
    print("Opção 4 - Imprimir Toda Lista")
    print("Opção 5 - Sair do programa")
    print("_______________________")
    space()


def carro_info(carro):
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
    space()

def carro_coleta_dados(placa):
    carro = Car()
    carro.placa = placa
    carro.padrao_placa = carro.validation_pattern_plate(carro.placa)
    carro.renavam = input('Digite o renavam: ')
    carro.marca = input('Digite a marca: ')
    carro.modelo = input('Digite a modelo: ')
    carro.ano_frabricacao = input('Digite o ano de fabricação: ')
    carro.cor = input('Digite a cor: ')
    carro.categoria = input('Digite a categoria: ')
    carro.estado = input('Digite o estado: ')
    carro.cidade = input('Digite a cidade: ')
    
    carro_info(carro)

def load_data(estrutura_de_dados, tipo_estrutura):
    start_time = Time_execution.start_time()  # capturando tempo inicial
    # lendo arquivo e armazenando em estrutura de dado
    Read_write_file.read_file(estrutura_de_dados, tipo_estrutura)
    end_time = Time_execution.end_time()  # capturando tempo final

    # calculando o tempo de execucao
    Time_execution.calculate_time_execution(
        start_time, end_time, 'Carregamento de Dados')
    # return lista_duplamente_encadeada
    return estrutura_de_dados


if __name__ == '__main__':

    # escolhendo estrutura de dados
    menu_estrutura_de_dados()
    resposta_usuario = int(
        input('❐ Informe a sua opção de Estrutura de Dados (1 a 4): '))
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
        resposta_usuario = int(input('❐ Informe a sua opção (1 a 5): '))

        if resposta_usuario == 5:
            print('Programa finalizado!')
            break
        elif resposta_usuario == 1:  # Pesquisar carro
            placa = input('Digite a placa do carro: ')
            carro = estrutura_de_dados.__getitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                carro_info(carro)
        elif resposta_usuario == 2:  # remover carro
            placa = input('Digite a placa do carro a ser removido: ')
            carro = estrutura_de_dados.__delitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                print(f'Carro com placa {placa} removido com sucesso.')
        elif resposta_usuario == 3:  # editar carro
            placa = input('Digite a placa do carro: ')
            carro = estrutura_de_dados.__getitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                dados = carro_coleta_dados(placa)
        elif resposta_usuario == 4:  # imprimir todos os carros
            estrutura_de_dados.imprimir_estrutura_de_dados()  # imprimindo carros
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(
            input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
