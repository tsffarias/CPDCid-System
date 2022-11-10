#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Thiago, Eduardo, Quirino, Biel
# Created Date: date/month/time ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
"""
Grupo: Thiago, Eduardo, Quirino, Biel
Título: CPDCID: PYTHON - Estrutura de Dados 2022
"""

# ---------------------------------------------------------------------------
from classes.Car import Car
from classes.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada
from classes.TabelaDispercao import TabelaDispercao
from classes.BinarySearchTree import BinarySearchTree
from classes.AVLTree import AVLTree
from services.Read_write_file import Read_write_file
from services.Time_execution import Time_execution
import os

'''
Limpa o terminal independente do sistema operacional
'''
def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")    

def space():
    print("")


def menu_estrutura_de_dados():
    print("Opção 1 - Lista Duplamente Encadeada")
    print("Opção 2 - Tabela de Disperção (Encadeamento Externo)")
    print("Opção 3 - Arvore Binaria de Busca")
    print("Opção 4 - Arvore AVL")
    print("Opção 5 - Em Desenvolvimento")
    print("_______________________")
    space()


def menu():
    print("Opção 1 - Pesquisar Carro")
    print("Opção 2 - Remover Carro")
    print("Opção 3 - Adicionar Carro")
    print("Opção 4 - Editar Carro")
    print("Opção 5 - Relatório de Veículos")
    print("Opção 6 - Sair do programa")
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
        raise Exception(f'Categoria inválida: {categoria}')

    estado = input('Digite o estado: ')
    if (carro.validation_uf(estado)):
        carro.estado = estado
    else:
        raise Exception(f'Estado inválido: {estado}')
    carro.cidade = input('Digite a cidade: ')
    
    return carro

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
    elif resposta_usuario == 3:
        estrutura_de_dados = BinarySearchTree()
        tipo_estrutura = 'arvore_binaria_busca'
    elif resposta_usuario == 4:
        estrutura_de_dados = AVLTree()
        tipo_estrutura = 'arvore_avl'

    clear_screen() # limpa terminal
    estrutura_de_dados = load_data(estrutura_de_dados, tipo_estrutura)

    while (True):

        space()
        print("CPDCID: PYTHON")
        print(f'Estrutura de Dados: {tipo_estrutura}')
        space()

        menu()
        # escolhendo operação
        resposta_usuario = int(input('❐ Informe a sua opção (1 a 6): '))

        if resposta_usuario == 6:
            # capturando tempo inicial da operacao
            start_time = Time_execution.start_time()
            Read_write_file.save_file(estrutura_de_dados)
            print('Programa finalizado!')
            end_time = Time_execution.end_time()  # capturando tempo final da operacao
            # calculando o tempo de execucao
            Time_execution.calculate_time_execution(
                start_time, end_time, 'Salvando Arquivo')
            break
        elif resposta_usuario == 1:  # Pesquisar carro
            placa = input('Digite a placa do carro: ')
            
            # capturando tempo inicial da operacao
            start_time = Time_execution.start_time()
            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                carro = estrutura_de_dados.__getitem__(placa)
                if carro[0] is None:
                    print('Placa não existe.')
                else:
                    estrutura_de_dados.carro_info(carro[0])

            elif tipo_estrutura == 'tabela_dispercao':
                carro = estrutura_de_dados.__getitem__(placa)
                if carro is None:
                    print('Placa não existe.')
                else:
                    estrutura_de_dados.carro_info(carro)

            elif tipo_estrutura == 'arvore_binaria_busca':
                carro = estrutura_de_dados.find(placa)
                if carro is None:
                    print('Placa não existe.')
                else:
                    estrutura_de_dados.carro_info(carro.car)

            elif tipo_estrutura == 'arvore_avl':
                carro = estrutura_de_dados.find(placa)
                if carro is None:
                    print('Placa não existe.')
                else:
                    estrutura_de_dados.carro_info(carro.car)
            
            end_time = Time_execution.end_time()  # capturando tempo final da operacao
            # calculando o tempo de execucao
            Time_execution.calculate_time_execution(
                start_time, end_time, 'Pesquisar carro')
        elif resposta_usuario == 2:  # remover carro
            placa = input('Digite a placa do carro a ser removido: ')
            
            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                # capturando tempo inicial da operacao
                carro = estrutura_de_dados.__getitem__(placa)
                if carro[0] is None:
                    print('Placa não existe.')
                else:
                    start_time = Time_execution.start_time()
                    estrutura_de_dados.__delitem__(carro[1])
                    print(f'Carro com placa {placa} removido com sucesso.')

            elif tipo_estrutura == 'tabela_dispercao':
                # capturando tempo inicial da operacao
                start_time = Time_execution.start_time()
                carro = estrutura_de_dados.__delitem__(placa)
                if carro is None:
                    print('Placa não existe.')
                else:
                    print(f'Carro com placa {placa} removido com sucesso.')
            
            elif tipo_estrutura == 'arvore_binaria_busca':
                # capturando tempo inicial da operacao
                start_time = Time_execution.start_time()
                carro = estrutura_de_dados.delete_value(placa)
                if carro is not None:
                    print('Placa não existe.')
                else:
                    print(f'Carro com placa {placa} removido com sucesso.')
            
            elif tipo_estrutura == 'arvore_avl':
                # capturando tempo inicial da operacao
                start_time = Time_execution.start_time()
                carro = estrutura_de_dados.delete_value(placa)
                if carro is not None:
                    print('Placa não existe.')
                else:
                    print(f'Carro com placa {placa} removido com sucesso.')

            
            end_time = Time_execution.end_time()  # capturando tempo final da operacao
            # calculando o tempo de execucao
            Time_execution.calculate_time_execution(
                    start_time, end_time, 'Remoção de carro')
        
        elif resposta_usuario == 3:  # adicionar carro
            placa = input('Digite a placa do carro: ')
            carro = estrutura_de_dados.__getitem__(placa)

            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                if carro[0] != None:
                    print('Placa já existe. Tente novamente.')
                else:
                    carro = carro_coleta_dados(placa)
                    # capturando tempo inicial da operacao
                    start_time = Time_execution.start_time()
                    estrutura_de_dados.inserir_no_inicio(carro)
                    
                    print(f'Veiculo com placa {carro.placa} adicionado com sucesso.')
                    end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                    Time_execution.calculate_time_execution(
                            start_time, end_time, 'Inserção de novo carro')
                
            elif tipo_estrutura == 'tabela_dispercao':
                if carro != None:
                    print('Placa já existe. Tente novamente.')
                else:
                    carro = carro_coleta_dados(placa)
                    # capturando tempo inicial da operacao
                    start_time = Time_execution.start_time()
                    resultado = estrutura_de_dados.__setitem__(carro.placa, carro)
                    if resultado:
                        print(f'Veiculo com placa {carro.placa} adicionado com sucesso.')
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Inserção de novo carro')
                    else:
                        print('Erro: Veiculo não encontrado.')
        
        elif resposta_usuario == 4:  # editar carro
            placa = input('Digite a placa do carro: ')
            carro = estrutura_de_dados.__getitem__(placa)
            
            # tipo de operação de acordo com o tipo estrutura
            if tipo_estrutura == 'lista_duplamente_encadeada':
                if carro[0] is None:
                    print('Placa não existe.')
                else:
                    carro = carro_coleta_dados(placa)
                    # capturando tempo inicial da operacao
                    start_time = Time_execution.start_time()
                    resultado = estrutura_de_dados.__edititem__(placa, carro)
                    if resultado:
                        print(
                            f'Veiculo com placa {carro.placa} editado com sucesso.')
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Edição de carro')
                    else:
                        print('Erro: Veiculo não encontrado.')
                
            elif tipo_estrutura == 'tabela_dispercao':
                
                if carro is None:
                    print('Placa não existe.')
                else:                
                    carro = carro_coleta_dados(placa)
                    # capturando tempo inicial da operacao
                    start_time = Time_execution.start_time()
                    resultado = estrutura_de_dados.__edititem__(carro.placa, carro)
                    if resultado:
                        print(f'Veiculo com placa {carro.placa} editado com sucesso.')
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Edição de carro')
                    else:
                        print('Erro: Veiculo não encontrado.')
        elif resposta_usuario == 5:  # Relatorio de veiculos
            # tipo de operação de acordo com o tipo estrutura

            print("Opção 1 - Relatório de Intervalo de Anos")
            print("Opção 2 - Relatório Estadual por Final de Placa")

            resposta_usuario = int(input('❐ Informe a sua opção (1 ou 2): '))

            # Relatório de Intervalo de Anos
            if (resposta_usuario == 1):  
                ano_inicial = input('Digite o ano inicial: ')
                ano_final = input('Digite o ano final: ')
                
                if tipo_estrutura == 'lista_duplamente_encadeada':
                    if (Car().validation_ano_fabricacao(ano_inicial) and Car().validation_ano_fabricacao(ano_final) and (ano_inicial <= ano_final)):
                        # capturando tempo inicial da operacao
                        start_time = Time_execution.start_time()
                        estrutura_de_dados.relatorio_intervalo_tempo(
                            ano_inicial, ano_final)
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Relatório de Intervalo de Anos')
                    else:
                        print('Intervalo de Anos inválido.')
                elif tipo_estrutura == 'tabela_dispercao':
                    if (Car().validation_ano_fabricacao(ano_inicial) and Car().validation_ano_fabricacao(ano_final) and (ano_inicial <= ano_final)):
                        # capturando tempo inicial da operacao
                        start_time = Time_execution.start_time()
                        estrutura_de_dados.relatorio_intervalo_tempo(
                            ano_inicial, ano_final)
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Relatório de Intervalo de Anos')
                    else:
                        print('Intervalo de Anos inválido.')
                elif tipo_estrutura == 'arvore_binaria_busca':
                    if (Car().validation_ano_fabricacao(ano_inicial) and Car().validation_ano_fabricacao(ano_final) and (ano_inicial <= ano_final)):
                        # capturando tempo inicial da operacao
                        start_time = Time_execution.start_time()
                        estrutura_de_dados.relatorio_intervalo_tempo(
                            ano_inicial, ano_final)
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Relatório de Intervalo de Anos')
                    else:
                        print('Intervalo de Anos inválido.')
                elif tipo_estrutura == 'arvore_avl':
                    if (Car().validation_ano_fabricacao(ano_inicial) and Car().validation_ano_fabricacao(ano_final) and (ano_inicial <= ano_final)):
                        # capturando tempo inicial da operacao
                        start_time = Time_execution.start_time()
                        estrutura_de_dados.relatorio_intervalo_tempo(
                            ano_inicial, ano_final)
                        end_time = Time_execution.end_time()  # capturando tempo final da operacao
                        # calculando o tempo de execucao
                        Time_execution.calculate_time_execution(
                            start_time, end_time, 'Relatório de Intervalo de Anos')
                    else:
                        print('Intervalo de Anos inválido.')
                
            
            
            elif (resposta_usuario == 2): # Relatório Estadual por Final de Placa
                uf = input('Digite o estado: ')
                # capturando tempo inicial da operacao
                start_time = Time_execution.start_time()

                if tipo_estrutura == 'lista_duplamente_encadeada':
                    estrutura_de_dados.relatorio_estadual_final_placa(uf)
                    end_time = Time_execution.end_time()  # capturando tempo final da operacao
                    # calculando o tempo de execucao
                    Time_execution.calculate_time_execution(
                        start_time, end_time, 'Relatório Estadual por Final de Placa')
                elif tipo_estrutura == 'tabela_dispercao':
                    estrutura_de_dados.relatorio_estadual_final_placa(uf)
                    end_time = Time_execution.end_time()  # capturando tempo final da operacao
                    # calculando o tempo de execucao
                    Time_execution.calculate_time_execution(
                        start_time, end_time, 'Relatório Estadual por Final de Placa')
                elif tipo_estrutura == 'arvore_binaria_busca':
                    estrutura_de_dados.relatorio_estadual_final_placa(uf)
                    end_time = Time_execution.end_time()  # capturando tempo final da operacao
                    # calculando o tempo de execucao
                    Time_execution.calculate_time_execution(
                        start_time, end_time, 'Relatório Estadual por Final de Placa')
                elif tipo_estrutura == 'arvore_avl':
                    estrutura_de_dados.relatorio_estadual_final_placa(uf)
                    end_time = Time_execution.end_time()  # capturando tempo final da operacao
                    # calculando o tempo de execucao
                    Time_execution.calculate_time_execution(
                        start_time, end_time, 'Relatório Estadual por Final de Placa')
            else:
                print('Opção inválida.')
            
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(
            input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        clear_screen() # limpa Terminal
        if resposta_nova_solicitacao == 2:
            # capturando tempo inicial da operacao
            start_time = Time_execution.start_time()
            Read_write_file.save_file(estrutura_de_dados)
            print('Programa finalizado!')
            end_time = Time_execution.end_time()  # capturando tempo final da operacao
            # calculando o tempo de execucao
            Time_execution.calculate_time_execution(
                start_time, end_time, 'Salvando Arquivo')
            break

