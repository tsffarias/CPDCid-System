from classes.Vehicle import Vehicle
import re
class Car(Vehicle):

    def __init__(self, placa=None, padrao_placa=None, renavam=None, marca=None, modelo=None, ano_frabricacao=None, cor=None, categoria=None, estado=None, cidade=None):
        
        if placa == None:
            super().__init__(placa, padrao_placa, renavam, marca, modelo,
                             ano_frabricacao, cor, categoria, estado, cidade)
            self._tipo_veiculo = 'Carro'
        else:          
            plate_pattern = self.validation_pattern_plate(placa) # verificando padrao de placa
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
                previus_pattern = re.compile(r'[A-Z]{3}[0-9]{4}') #padrão antigo = LLLNNNN
                current_pattern = re.compile(r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}') #padrão atual = LLLNLNN 

                if bool(re.fullmatch(current_pattern, str(placa))):
                    return 'Padrão Mercosul'
                elif bool(re.fullmatch(previus_pattern, str(placa))):
                    return 'Padrão Antigo'
                else:
                    return -1
