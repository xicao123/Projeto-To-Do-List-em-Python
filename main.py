from tarefa import Tarefa
from gestor import GestorTarefas

def menu():
    t= GestorTarefas()
    while True:
        print("\n----Menu----\n")
        print("1- Cria uma tarefa")
        print("2- Listar todas as tarefas")
        print("3- Vê os detalhes de uma tarefa criada")
        print("4- Altera dados de uma tarefa")
        print("5- Marcar uma tarefa como concluida")
        print("6- Remover uma tarefa")
        print("7- Pesquisar tarefas por texto")
        print("8- Filtrar tarefas por estado")
        print("9- Estatisticas sobre as tarefas Registadas")
        print("0- Saír")
        
        try:
            opcao = int(input("Escreve uma opção do menu: "))
        except ValueError:
            print("\nErro: Por favor, digita apenas um número inteiro correspondente ao menu!")
            continue
        match opcao:
            case 1:
                t.adicionarTarefa()
            case 2:
                t.mostrarTarefa()
            case 3:
                t.detalhes_de_uma_tarefa()
            case 4:
                t.alterar_dados()
            case 5:
                t.tarefa_concluida()
            case 6:
                t.revmover_tarefa()
            case 7:
                t.pesquisar_por_texto()
            case 8:
                t.filtrar()
            case 9:
                t.estatistica()
            case 0:
                print("\nA fechar o programa... Obrigado!")
                break
            case _:
                print("\nErro: Opção inválida! Escolhe uma opção de 0 a 9.")

menu()

