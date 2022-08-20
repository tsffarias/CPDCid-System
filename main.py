from classes.Car import Car
from services.Read_write_file import Read_write_file

'''
Grupo: Thiago, Eduardo, Quirino, Biel
Título: CPDCID: PYTHON - Estrutura de Dados 2022
'''

def espaco():
    print("")

def menu():
    print("Opção 1 - Pesquisar Carro")
    print("Opção 2 - Remover Carro")
    print("Opção 3 - Imprimir Toda Lista")
    print("Opção 4 - Sair do programa")
    print("_______________________")
    espaco()

def carregar_dados():
    Read_write_file.read_file()
    

if __name__ == '__main__':
    
    carregar_dados()

    while (True):

        espaco()
        print("CPDCID: PYTHON")
        espaco()
        
        menu()

        resposta_usuario = int(input('❐ Informe a sua opção (1 a 4): '))
        
        if resposta_usuario == 4:
            print('Programa finalizado!')
            break
        elif resposta_usuario == 1:
            print(resposta_usuario)
        else:
            print('Tente novamente.')

        espaco()
        resposta_nova_solicitacao = int(input('Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: '))
        if resposta_nova_solicitacao == 2:
            print('Programa finalizado!')
            break
