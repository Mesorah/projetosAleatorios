segredo = []
asterisco = []
palavra_secreta = 'perfume'
for c in palavra_secreta:
    segredo.append(c)
    asterisco.append('*')

tot = 0

while True:
    nome_palavra = input('\ndigite uma letra: ')
    tot += 1

    if len(nome_palavra) > 1:
        print('digite apenas uma letra')
    else:
        acerto = False
        for k,v in enumerate(segredo):
            if nome_palavra == v:
                asterisco[k] = nome_palavra
                acerto = True

    for c in asterisco:
        print(f'{c}', end='')

    if '*' not in asterisco:
        print('\nvocê ganhou')
        break

    if not acerto:
        print('\nletra errada')

print(f'Você levou {tot} chances')
