import copy

produtos = {'nome': 'lapis', 'preco': 2, 'quantidade': 20}

produtos['preco'] *= 1.15

print(produtos)


print()
itens1 = {'nome': 'lapis', 'preco': 2, 'quantidade': 20}

itens2 = copy.deepcopy(itens1)

itens2['nome'] = 'Corinthinas'

print(itens1)
print(itens2)


print()



