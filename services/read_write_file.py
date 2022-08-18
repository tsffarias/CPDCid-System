from classes.Car import Car
class Read_write_file:

    def read_file():
        with open('.\\files\\veiculos.ernv', encoding='utf8') as f:
            for line in f:
                content_list = line.strip().split(";") # separa o conteudo pelo delimitador ; e coloca em uma lista
                carro = Car(content_list[0],
                            content_list[1],
                            content_list[2],
                            content_list[3],
                            content_list[4],
                            content_list[5],
                            content_list[6],
                            content_list[7],
                            content_list[8])
                
                print(carro.__str__())
