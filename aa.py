def main():
    print('''
[1]- cadastrar tarefa
[2]- visualizar tarefa
[3]- marcar como concluído''')
    print()
    opcao = input('digite sua opção: ')
    return opcao


def opcao1(todas_tarefa):
    #dicionario para cada tarefa
    cadastra_tarefa = {}

    #perguntas
    tarefa = input('Qual nome de tarefa gostaria de cadastrar? ')
    descricao = input('Descreva a tarefa: ')

    #transferencia de dicionario
    cadastra_tarefa = {
        'nome': tarefa,
        'descricao': descricao
    }

    todas_tarefa.append(cadastra_tarefa)

    print("Tarefa cadastrada:")
    print(cadastra_tarefa)
    print()


def opcao2(todas_tarefa):
    print("Todas as tarefas:")
    for tarefa in todas_tarefa:
        print(tarefa)
    print()


def opcao3():
    # Implemente a lógica para marcar tarefa como concluída
    ...


def gerenciamento_tarefa():
    todas_tarefa = []  # Inicialize a lista de tarefas aqui
    while True:
        opcao = main()

        try:
            opcao = int(opcao)
        except ValueError:
            print('Erro: Opção inválida.')

        if opcao == 1:
            print()
            print('Opção 1 selecionada - cadastrar tarefa')
            opcao1(todas_tarefa)
        elif opcao == 2:
            print()
            print('Opção 2 selecionada - visualizar tarefa')
            opcao2(todas_tarefa)
        elif opcao == 3:
            print()
            print('Opção 3 selecionada - marcar como concluído')
            opcao3()
        else:
            print('Opção inválida.')


gerenciamento_tarefa()
