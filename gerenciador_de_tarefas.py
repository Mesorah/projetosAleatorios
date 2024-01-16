#cadastrar, visulazar e marcar como concluido ✅❌
def main():
    print('''
[1]- cadastrar tarefa
[2]- visualizar tarefa
[3]- marcar como concluído''')
    print()
    opcao = input('digite sua opção: ')
    return opcao


def opcao1(todas_tarefa):
    from datetime import datetime
    hoje = datetime.now().strftime('%d/%m/%Y')

    cadastra_tarefa = {}

    #perguntas
    tarefa = input('qual nome tarefa gostaria de cadastrar? ')
    descricao = input('Descreva a tarefa: ')
    dia = input('para qual dia queira fazer? ')


    if len(tarefa) <= 100 and len(descricao) <= 500:
        cadastra_tarefa = {
            'nome': tarefa,
            'descrição': descricao,
            'data': hoje
        }

        todas_tarefa.append(cadastra_tarefa)
        print(todas_tarefa)


            




def opcao2(todas_tarefa):
    if len(todas_tarefa) > 0:
        print('suas tarefas:')
        print()
    else:
        print('Listas de tarefas vazias')

    for n, c in enumerate(todas_tarefa):
        print(f'[{n+1}]: {c}')

def opcao3():
    ...


def gerenciamento_tarefa():
    todas_tarefa = []
    while True:
        opcao = main()

        try:
            opcao = int(opcao)
        except ValueError:
            print('erro')

        if opcao == 1:
            print()
            print('Opção 1 selecionada - cadastrar tarefa')
            print()
            opcao1(todas_tarefa)
        elif opcao == 2:
            opcao2(todas_tarefa)
        elif opcao == 3:
            opcao3()
        else:
            print('opção inválida')
    


gerenciamento_tarefa()