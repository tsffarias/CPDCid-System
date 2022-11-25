<img src="https://img.icons8.com/cute-clipart/64/000000/car-racing.png" alt="CPDCid-System ícone by Icons8" width="100px" align="right"/>

# CPDCid-System

Trabalho de Estrutura de Dados e Programação I, da turma T01-2022-2.
Desenvolvido pelos discentes:

 - Gabriel Felipe Barbosa [@gabrielfbarbosa](https://github.com/gabrielfbarbosa)
 - Luiz Eduardo Satelis dos Santos [@edusatelis](https://github.com/edusatelis/)
 - Luiz Fernando Postingel Quirino [@luizfpq](https://github.com/luizfpq/)
 - Thiago Silva Farias [@tsffarias](https://github.com/tsffarias)


## Descrição sucinta

 Implementar alguns protótipos para a manipulação de dados de veículos utilizando várias estruturas de dados diferentes, de tal forma que possam avaliar e indicar qual a melhor estrutura de dados se aplica ao projeto


### Estruturas implementadas

  - Listas encadeadas
  - Tabelas de dispersão com encadeamento externo
  - Arvore Binaria de Busca
  - Arvore AVL
  - Arvore Digital


# Documentação

## Estrutura dos arquivos
    .
    ├── classes → Objetos (estruturas de dados e veículos)
    │   ├── AVLTree.py
    │   ├── BinarySearchTree.py
    │   ├── Car.py
    │   ├── ListaDuplamenteEncadeada.py
    │   ├── TabelaDispercao.py
    │   ├── Trie.py
    │   └── Vehicle.py
    ├── docs → Documentos para modelagem e desenvolvimento do sistema
    │   ├── enunciado_trabalho_pratico.pdf
    │   ├── functions.md 
    │   └── vars.md
    ├── files
    │   ├── veiculos.ernv → Arquivo de dados com 700 mil entradas
    │   └── veiculos_test.ernv → Arquivo de dados para testes rápidos
    ├── main.py → Arquivo principal do sistema
    ├── README.md → Readme file do git
    ├── README.txt
    └── services
        ├── Read_write_file.py → leitura e escrita de arquivos de dados
        └── Time_execution.py → calcula os tempos de execução das ações

## Instruções de uso

### Execução do sistema

Em seu terminal, execute:

    python3 main.py


### Menu inicial:
  
    Opção 1 - Lista Duplamente Encadeada
    Opção 2 - Tabela de Disperção (Encadeamento Externo)
    Opção 3 - Arvore Binaria de Busca
    Opção 4 - Arvore AVL
    Opção 5 - Arvore Digital (Trie)
    _______________________

    ❐ Informe a sua opção de Estrutura de Dados (1 a 5): 

As opções indicam números a serem pressionados, ao escolher uma das opções, o sistema irá trabalhar com a estrutura de dados definida, daquele momento em diante.

 * Para escolher outra estrutuda de dados, o usuário deverá sair do sistema e iniciá-lo novamente.

### Menu principal

    Tempo de execução da operação Carregamento de Dados: 7.47 segundos

    CPDCID: PYTHON
    Estrutura de Dados: arvore_trie

    Opção 1 - Pesquisar Carro
    Opção 2 - Remover Carro
    Opção 3 - Adicionar Carro
    Opção 4 - Editar Carro
    Opção 5 - Relatório de Veículos
    Opção 6 - Sair do programa
    _______________________

    ❐ Informe a sua opção (1 a 6): 


Ao carregar a estrutura de dados definida, o sistema exibirá as funções princiais definidas por números, no mesmo conceito aplicado no menu inicial. Além da informação no topo da tela que indica qual a estrutura de dados está sendo utilizada e o tempo para execução do carregamento dos dados. 

* O valor referente ao tempo de carregamento dos dados, só será exibido caso seja a primeira vez que o usuário visualiza a tela. 

### Navegação

Para todas as operações seguintes, o usuário irá navegar atraves de um menu de seleção com o mesmo comportamento e padrão de uso.

Em todas as telas que permitem retorno, o usuário receberá a mesma mensagem padrão, contendo o tempo de execução da ultima ação e as opções de retornar ao Menu Principal (com a estrutura de dados já definida) e a opção de sair.


    Tempo de execução da operação Pesquisar carro: 0.0 segundos

    Digite (1), se desejar voltar ao menu e (2) caso deseje finalizar: 


### Finalização

Ao selecionar a opção referente a 'Sair do programa', será exibido o tempo de salvamento do arquivo de dados.

    Programa finalizado!
    Tempo de execução da operação Salvando Arquivo: 0.0 segundos



