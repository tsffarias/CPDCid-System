class Vehicle:

    # Construtor
    def __init__(self, placa, renavam, marca, modelo, ano_frabricacao, cor, categoria, estado, cidade):
        self._placa = placa
        self._renavam = renavam
        self._marca = marca
        self._modelo = modelo
        self._ano_frabricacao = ano_frabricacao
        self._cor = cor
        self._categoria = categoria
        self._estado = estado
        self._cidade = cidade

    # Getters e Setters
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def renavam(self):
        return self._renavam

    @renavam.setter
    def renavam(self, renavam):
        self._renavam = renavam

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def ano_frabricacao(self):
        return self._ano_frabricacao

    @ano_frabricacao.setter
    def ano_frabricacao(self, ano_frabricacao):
        self._ano_frabricacao = ano_frabricacao

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    def __str__(self):
        return f'Veiculo: {self._placa} - {self.renavam} - {self._marca} - {self._modelo} - {self._ano_frabricacao} - {self._cor} - {self._categoria} - {self._estado} - {self._cidade}'
