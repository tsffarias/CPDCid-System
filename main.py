from classes.Car import Car

if __name__ == "__main__":
    carro = Car("FBI3643",
                "20845156218",
                "ASTON MARTIN",
                "DB9 Coupe 6.0 V12 510cv",
                2014,
                "Preto",
                "Particular",
                "SP",
                "Pereira Barreto")

    print(carro.__str__())

