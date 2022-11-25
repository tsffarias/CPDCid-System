#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : name_of_the_creator   Line 3
# Created Date: date/month/time ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""

from classes.Car import Car
from pathlib import Path

file_name = 'veiculos_test'

class Read_write_file:

    def save_file(estrutura_de_dados):
        with open(Path("files", f"{file_name}.ernv"), mode="w", encoding='utf8') as file:
            estrutura_de_dados = estrutura_de_dados.preparando_salvamento_dados()
            file.write("\n".join(estrutura_de_dados))

    def read_file(estrutura_de_dados, tipo_estrutura):
        with open(Path("files", f"{file_name}.ernv"), encoding='utf8') as f:
            for line in f:
                # separa o conteudo pelo delimitador ; e coloca em uma lista
                content_list = line.strip().split(";")
                carro = Car()  # criando objeto carro
                # inserindo dados do carro no objeto
                carro.placa = content_list[0]
                carro.padrao_placa = carro.validation_pattern_plate(
                    carro.placa)  # validando padrão de placa
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
                elif tipo_estrutura == 'arvore_binaria_busca':
                    estrutura_de_dados.insert(carro.placa, carro)
                elif tipo_estrutura == 'arvore_avl':
                    estrutura_de_dados.insert(carro.placa, carro)
                elif tipo_estrutura == 'arvore_trie':
                    estrutura_de_dados.insert(carro.placa, carro)

        return estrutura_de_dados
