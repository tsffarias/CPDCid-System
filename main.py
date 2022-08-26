from classes.Car import Car
from services.Read_write_file import Read_write_file
from services.Time_execution import Time_execution

'''
Grupo: Thiago, Eduardo, Quirino, Biel
Título: CPDCID: PYTHON - Estrutura de Dados 2022
'''

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
    Read_write_file.read_file() # lendo arquivo
    end_time = Time_execution.end_time()  # capturando tempo final

    # calculando o tempo de execucao
    Time_execution.calculate_time_execution(start_time, end_time, 'Carregamento de Dados')

if __name__ == '__main__':

    load_data()

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
            print(resposta_usuario)
        else:
            print('Tente novamente.')

        space()
        resposta_nova_solicitacao = int(input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
