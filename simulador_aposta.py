from random import randint

def validacao(valor_banca):
    while True:
        try:
            aposta = int(input('Digite um valor para apostar: '))
            if aposta <= valor_banca:
                break
            else:
                print('Valor insuficiente')
        except ValueError:
            print('Digite apenas valores inteiros')

    while True:
        try:
            dado_jogador = int(input('Qual número você acha que o dado vai cair? '))
            if dado_jogador >= 1 and dado_jogador <= 6:
                break
            else:
                print('digite apenas valores de 1 a 6')
        except ValueError:
            print('Digite apenas valores inteiros')

    return aposta, dado_jogador

def dado(valor_banca):
    while True:
        numero_aleatorio = randint(1, 6)
        print(numero_aleatorio)

        aposta, dado_jogador = validacao(valor_banca)

        if numero_aleatorio == dado_jogador:
            ganho_aposta = aposta * 3 - aposta
            valor_banca += ganho_aposta
            print(f'Você ganhou R${ganho_aposta}')
            print(f'Sua banca R${valor_banca}')
        else:
            print(f'Você perdeu R${aposta}')
            valor_banca -= aposta
            print(f'Sua banca R${valor_banca}')

            if valor_banca <= 0:
                print('Você perdeu todo seu dinheiro')
                return valor_banca

        continuar = input('Você quer continuar? [s/n] ')
        if continuar == 'n':
            break

    return valor_banca
    
def foguetinho(valor_banca):
    while True:
        numero_aleatorio = randint(1, 6)
        print(numero_aleatorio)

        
        aposta, dado_jogador = validacao(valor_banca)

        if numero_aleatorio != dado_jogador:
            ganho_aposta = aposta * 1.05 - aposta
            valor_banca += ganho_aposta
            print(f'Você ganhou R${ganho_aposta}')
            print(f'Sua banca R${valor_banca}')
        else:
            print(f'Você perdeu R${aposta}')
            valor_banca -= aposta
            print(f'Sua banca R${valor_banca}')
            if valor_banca <= 0:
                print('Você perdeu todo seu dinheiro')
                return valor_banca

        continuar = input('Você quer continuar? [s/n] ')
        if continuar == 'n':
            break

    return valor_banca

def sorteio(valor_banca):
    while True:
        numero_aleatorio = randint(1,90)
        print(numero_aleatorio)

        aposta, dado_jogador = validacao(valor_banca)

        if numero_aleatorio == dado_jogador:
            ganho_aposta = aposta * 120 - aposta
            valor_banca += ganho_aposta
            print(f'Você ganhou R${ganho_aposta}')
            print(f'Sua banca R${valor_banca}')
        else:
            print(f'Você perdeu R${aposta}')
            valor_banca -= aposta
            print(f'Sua banca R${valor_banca}')

        if valor_banca <= 0:
            print('Você perdeu todo seu dinheiro')
            return valor_banca

        continuar = input('Você quer continuar? [s/n] ')
        if continuar == 'n':
            break

    return valor_banca


valor_banca = 100

while True:
    if valor_banca <= 0:
        break

    modo = input('Qual modo você quer jogar? ').lower()
    
    if modo == 'dado':
        valor_banca = dado(valor_banca)
    
    elif modo == 'foguetinho':
        valor_banca = foguetinho(valor_banca)
    
    elif modo == 'sorteio':
        valor_banca = sorteio(valor_banca)
    
    else:
        print('digite um modo válido')