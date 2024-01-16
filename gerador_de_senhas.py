import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caracteres_especiais = ['!', '@', '%', '$']
senha = []

tamanho_senha = ''

while tamanho_senha != int:
    try:
        tamanho_senha = input('quantos caracteres?')
        tamanho_senha = int(tamanho_senha)
        break
    except ValueError:
        print('digite apenas números inteiros')

senha_legivel = input('senha legivel?').lower()

if senha_legivel[0] == 'n':
   
   while tamanho_senha >= 1:
    numero_aleatorio = random.randint(1,5)
    tamanho_senha -= 1
    
    if numero_aleatorio == 1:
        c = random.choice(caracteres_especiais)
        senha.append(c)
    elif numero_aleatorio == 2 or numero_aleatorio == 3:
        c = random.choice(caracteres)
        senha.append(c)
    elif numero_aleatorio == 4 or numero_aleatorio == 5:
        c = random.choice(numeros)
        senha.append(c)
else:
    while tamanho_senha >= 1:
        numero_aleatorio = random.randint(1,2)
        tamanho_senha -= 1

        if numero_aleatorio == 1:
            c = random.choice(caracteres)
            senha.append(c)
        elif numero_aleatorio == 2:
            c = random.choice(numeros)
            senha.append(c)

random.shuffle(senha)

print(f'sua senha é: ', end='')

for c in senha:
    print(c, end='')
