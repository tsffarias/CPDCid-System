from classes.Vehicle import Vehicle
import re


class Car(Vehicle):

    def __init__(self, placa=None, padrao_placa=None, renavam=None, marca=None, modelo=None, ano_frabricacao=None, cor=None, categoria=None, estado=None, cidade=None):

        if placa == None:
            super().__init__(placa, padrao_placa, renavam, marca, modelo,
                             ano_frabricacao, cor, categoria, estado, cidade)
            self._tipo_veiculo = 'Carro'
        else:
            plate_pattern = self.validation_pattern_plate(
                placa)  # verificando padrao de placa
            if (plate_pattern == -1):
                raise Exception(f'Placa Inválida: {placa}')

            super().__init__(placa, plate_pattern, renavam, marca, modelo,
                            ano_frabricacao, cor, categoria, estado, cidade)
            self._tipo_veiculo = 'Carro'

    def __str__(self):
        return f'{self._tipo_veiculo}: Placa({self._placa}) - Padrão Placa({self._padrao_placa}) - Renava({self.renavam}) - Marca({self._marca}) - Modelo({self._modelo}) - Ano Fabricação({self._ano_frabricacao}) - Cor({self._cor}) - Categoria({self._categoria}) - Estado({self._estado}) - Cidade({self._cidade})'

    def validation_pattern_plate(self, placa):
        if placa != None:
            if len(placa) == 7:
                previus_pattern = re.compile(
                    r'[A-Z]{3}[0-9]{4}')  # padrão antigo = LLLNNNN
                current_pattern = re.compile(
                    r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}')  # padrão atual = LLLNLNN

                if bool(re.fullmatch(current_pattern, str(placa))):
                    return 'Padrão Mercosul'
                elif bool(re.fullmatch(previus_pattern, str(placa))):
                    return 'Padrão Antigo'
                else:
                    return -1

    def validation_ano_fabricacao(self, ano_frabricacao):
        if len(str(ano_frabricacao)) == 4 and str(ano_frabricacao).isnumeric():
            return True
        else:
            return False

    def validation_renavam(self, renavam):
        if len(str(renavam)) == 11 and str(renavam).isnumeric():
            return True
        else:
            return False

    def validation_marca(self, marca):
        if len(str(marca)) <= 15:  # maximo de 15 caracteres
            return True
        else:
            return False

    def validation_modelo(self, modelo):
        if len(str(modelo)) <= 45:  # maximo de 45 caracteres
            return True
        else:
            return False

    def validation_categoria(self, categoria):
        # sistema antigo
        categoria_sistema_antigo = (
            'particular', 'aluguel', 'aprendizagem', 'experiência/fabricante', 'oficial', 'representação', 'missão diplomática', 'corpo consular', 'corpo diplomático', 'organismo consular/internacional', 'acordo cooperação internacional', 'coleção')
        # sistema atual
        categoria_sistema_atual = (
            'particular', 'comercial', 'especiais', 'oficial e representação', 'diplomático/consular', 'coleção')

        if self._padrao_placa.lower() == 'padrão mercosul':
            if categoria.lower() in categoria_sistema_atual:
                return True
            else:
                return False
        else:
            if categoria.lower() in categoria_sistema_antigo:
                return True
            else:
                return False

    def validation_uf(self, uf):
        list_uf = ('AC', 'AL', 'AP', 'AM', 'BA',
                   'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')

        if uf.upper() in list_uf:
            return True
        else:
            return False
