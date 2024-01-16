def validador_nome(nome_usuario):
    for c in nome_usuario:
        if c.isdigit():
            return True
    if len(nome_usuario) >= 12:
        return False

def validador_data(data):
    from datetime import datetime
    hoje = datetime.today().year
    try:
        valida = datetime.strptime(data, '%d/%m/%Y')
        idade = hoje - valida.year
        if idade >= 18:
            return True
    except ValueError:
        return False

def calcula_digito_verificador(novos):
    soma = 0
    cont = 10
    for c in novos:
        soma += int(c) * cont
        cont -= 1

    resto_divisao = soma % 11
    if resto_divisao < 2:
        return 0
    else:
        return 11 - resto_divisao

def validador_cpf1(n1):
    n1 = n1.replace('.', '').replace('-', '')
    novos = n1[:9]
    resto_divisao = calcula_digito_verificador(novos)
    return resto_divisao, novos

def validador_cpf2(n):
    resto_divisao, novos1 = validador_cpf1(n)
    digito_verificador = calcula_digito_verificador(novos1)
    
    cpf_gerado = f'{novos1}{digito_verificador}{resto_divisao}'
    print(cpf_gerado)
    if cpf_gerado == n:
        return True
    return False

def cadastro():
    while True:
        nome_usuario = input('digite seu nome completo: ')
        if validador_nome(nome_usuario) == False:
            ano_nascimento = input('digite seu ano de nascimento: ')

            if validador_data(ano_nascimento):       
                cpf = input('digite seu cpf: ')
                if validador_cpf2(cpf):
                    print('ggs')
                    break

            else:
                print('Data de nascimento inválida')
        else:
            print('nome inválido')            

cadastro()