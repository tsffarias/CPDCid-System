#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name_of_the_creator
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
from services.Read_write_file import Read_write_file
from services.Time_execution import Time_execution


def space():
    print("")

def menu():
    print("Opção 1 - Pesquisar Carro")
    print("Opção 2 - Remover Carro")
    print("Opção 3 - Imprimir Toda Lista")
    print("Opção 4 - Sair do programa")
    print("_______________________")
    space()

def load_data():
    start_time = Time_execution.start_time()  # capturando tempo inicial
    lista_duplamente_encadeada = ListaDuplamenteEncadeada()
    Read_write_file.read_file(lista_duplamente_encadeada)  # lendo arquivo
    end_time = Time_execution.end_time()  # capturando tempo final
    # calculando o tempo de execucao
    Time_execution.calculate_time_execution(start_time, end_time, 'Carregamento de Dados')
    return lista_duplamente_encadeada

if __name__ == '__main__':

    lista_duplamente_encadeada = load_data() # carregando dados dos carros

    while (True):

        space()
        print("CPDCID: PYTHON")
        space()
        
        menu()

        resposta_usuario = int(input('❐ Informe a sua opção (1 a 4): '))
        
        if resposta_usuario == 4:
            print('Programa finalizado!')
            break
        elif resposta_usuario == 1:
            busca_carro = input("Entre com o dado do veículo para busca: ")
            busca_carro = ListaDuplamenteEncadeada.busca(lista_duplamente_encadeada, busca_carro)
            print(busca_carro.conteudo)

        elif resposta_usuario == 2:
            print(resposta_usuario)
        elif resposta_usuario == 3:
            lista_duplamente_encadeada.imprimir() # imprimindo carros
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
