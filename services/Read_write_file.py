#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name_of_the_creator   Line 3
# Created Date: date/month/time ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
""" 
Realiza as operações básicas de leitura e escrita em arquivo
fornecendo o comportamento de persistencia do sistema
"""

from classes.Car import Car
from pathlib import Path

class Read_write_file:

    def read_file(estrutura_de_dados, tipo_estrutura):
        with open(Path("files", "veiculos_test.ernv"), encoding='utf8') as f:
            for line in f:
                content_list = line.strip().split(";") # separa o conteudo pelo delimitador ; e coloca em uma lista
                carro = Car() # criando objeto carro
                carro.placa = content_list[0] # inserindo dados do carro no objeto
                carro.padrao_placa = carro.validation_pattern_plate(carro.placa) # validando padrão de placa
                carro.renavam = content_list[1]
                carro.marca = content_list[2]
                carro.modelo = content_list[3]
                carro.ano_frabricacao = content_list[4]
                carro.cor = content_list[5]
                carro.categoria = content_list[6]
                carro.estado = content_list[7]
                carro.cidade = content_list[8]

                if tipo_estrutura == 'tabela_dispercao':
                    estrutura_de_dados.__setitem__(carro.placa, carro)
                elif tipo_estrutura == 'lista_duplamente_encadeada':
                    estrutura_de_dados.inserir_no_inicio(carro)

        return estrutura_de_dados
