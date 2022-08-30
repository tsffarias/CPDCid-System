from classes.Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, placa=None, renavam=None, marca=None, modelo=None, ano_frabricacao=None, cor=None, categoria=None, estado=None, cidade=None):
        super().__init__(placa, renavam, marca, modelo,
                         ano_frabricacao, cor, categoria, estado, cidade)
        self._tipo_veiculo = 'Carro'

    def __str__(self):
        return f'{self._tipo_veiculo}: Placa({self._placa}) - Renavam({self.renavam}) - Marca({self._marca}) - Modelo({self._modelo}) - Ano Fabricação({self._ano_frabricacao}) - Cor({self._cor}) - Categoria({self._categoria}) - Estado({self._estado}) - Cidade({self._cidade})'
