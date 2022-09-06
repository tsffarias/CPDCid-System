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
    print("Opção 4 - Relatório de Veículos")
    print("Opção 5 - Sair do programa")
    print("_______________________")
    space()

def carro_coleta_dados(placa):
    carro = Car()
    carro.placa = placa
    carro.padrao_placa = carro.validation_pattern_plate(carro.placa)
    
    renavam = input('Digite o renavam: ')
    if (carro.validation_renavam(renavam)):
        carro.renavam = renavam
    else:
        raise Exception(f'Renavam inválido (padrão de 11 números não respeitados): {renavam}')

    marca = input('Digite a marca: ')
    if (carro.validation_marca(marca)):
        carro.marca = marca
    else:
        raise Exception(f'Marca inválida (maximo de 15 caracteres não respeitados): {marca}')

    modelo = input('Digite a modelo: ')
    if (carro.validation_modelo(modelo)):
        carro.modelo = modelo
    else:
        raise Exception(
            f'Modelo inválido (maximo de 45 caracteres não respeitados): {modelo}')

    ano_frabricacao = input('Digite o ano de fabricação: ')
    if (carro.validation_ano_fabricacao(ano_frabricacao)):
        carro.ano_frabricacao = ano_frabricacao
    else:
        raise Exception(f'Ano de fabricação inválido: {ano_frabricacao}')

    carro.cor = input('Digite a cor: ')
    categoria = input('Digite a categoria: ')
    if (carro.validation_categoria(categoria)):
        carro.categoria = categoria
    else:
        raise Exception(f'Categoria inválida: {ano_frabricacao}')

    estado = input('Digite o estado: ')
    if (carro.validation_uf(estado)):
        carro.estado = estado
    else:
        raise Exception(f'Estado inválido: {estado}')
    carro.cidade = input('Digite a cidade: ')
    
    #estrutura_de_dados.carro_info(carro)

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
            
            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                print('Em Desenvolvimento')
                carro = None
            elif tipo_estrutura == 'tabela_dispercao':
                carro = estrutura_de_dados.__getitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                estrutura_de_dados.carro_info(carro)
        elif resposta_usuario == 2:  # remover carro
            placa = input('Digite a placa do carro a ser removido: ')
            
            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                print('Em Desenvolvimento')
                carro = None
            elif tipo_estrutura == 'tabela_dispercao':
                carro = estrutura_de_dados.__delitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                print(f'Carro com placa {placa} removido com sucesso.')
        elif resposta_usuario == 3:  # editar carro
            placa = input('Digite a placa do carro: ')

            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                print('Em Desenvolvimento')
                carro = None
            elif tipo_estrutura == 'tabela_dispercao':
                carro = estrutura_de_dados.__getitem__(placa)

            if carro is None:
                print('Placa não existe.')
            else:
                dados = carro_coleta_dados(placa)
        elif resposta_usuario == 4:  # Relatorio de veiculos
            # tipo de operação de acordo com o tipo estrutura

            print("Opção 1 - Relatório de Intervalo de Anos")
            print("Opção 2 - Relatório Estadual por Final de Placa")

            resposta_usuario = int(input('❐ Informe a sua opção (1 ou 2): '))

            # Relatório de Intervalo de Anos
            if (resposta_usuario == 1):  
                ano_inicial = input('Digite o ano inicial: ')
                ano_final = input('Digite o ano final: ')
                
                if tipo_estrutura == 'lista_duplamente_encadeada':
                    print('Em Desenvolvimento')
                    #estrutura_de_dados.imprimir_estrutura_de_dados()
                elif tipo_estrutura == 'tabela_dispercao':
                    if (Car().validation_ano_fabricacao(ano_inicial) and Car().validation_ano_fabricacao(ano_final) and (ano_inicial <= ano_final)):
                        estrutura_de_dados.relatorio_intervalo_tempo(
                            ano_inicial, ano_final)
                    else:
                        print('Intervalo de Anos inválido.')
                
            
            
            elif (resposta_usuario == 2): # Relatório Estadual por Final de Placa
                
                if tipo_estrutura == 'lista_duplamente_encadeada':
                    print('Em Desenvolvimento')
                    estrutura_de_dados.imprimir_estrutura_de_dados()
                elif tipo_estrutura == 'tabela_dispercao':
                    # Relatorio estadual por final de placa: o programa deve listar todos os 
                    # veıculos de um dado estado, agrupados pelo digito final da placa.
                    # https://stackabuse.com/python-check-if-string-contains-substring/ **************
                    estrutura_de_dados.imprimir_estrutura_de_dados() 
            else:
                print('Opção inválida.')
            
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(
            input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
