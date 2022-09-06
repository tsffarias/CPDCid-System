#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : name_of_the_creator   Line 3
# Created Date: date/month/time ..etc
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""

from classes.Car import Car
from pathlib import Path

class Read_write_file:

    def read_file(lista_duplamente_encadeada):
        with open(Path("files", "veiculos.ernv"), encoding='utf8') as f:
            for line in f:
                content_list = line.strip().split(";") # separa o conteudo pelo delimitador ; e coloca em uma lista
                carro = Car() # criando objeto carro
                carro.placa = content_list[0] # inserindo dados do carro no objeto
                carro.renavam = content_list[1]
                carro.marca = content_list[2]
                carro.modelo = content_list[3]
                carro.ano_frabricacao = content_list[4]
                carro.cor = content_list[5]
                carro.categoria = content_list[6]
                carro.estado = content_list[7]
                carro.cidade = content_list[8]

                lista_duplamente_encadeada.inserir_no_inicio(carro)

        return lista_duplamente_encadeada