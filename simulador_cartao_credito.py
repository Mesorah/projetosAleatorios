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
        if idade >= 18 and idade <= 113:
            return True
    except ValueError:
        return False

def validador_cpf1(n1):
    soma = 0
    n1 = n1.replace('.', '').replace('-', '')
    novos = n1[:9]
    if len(n1) == 11:
        multiplicacao = 0
        cont = 10
        for c in novos:
            multiplicacao = int(c) * cont
            cont -= 1
            soma += multiplicacao
        nova_multiplicacao = soma * 10
        resto_divisao = nova_multiplicacao % 11
        if resto_divisao > 9:
            resto_divisao = 0
        else:
            resto_divisao = resto_divisao
    return resto_divisao, n1, novos

def validador_cpf2(n):
    resto_divisao1, novos1, _ = validador_cpf1(n)
    soma1 = 0
    novos1 = novos1[:10]
    multiplicacao1 = 0
    cont1 = 11
    for c1 in novos1:
        multiplicacao1 = int(c1) * cont1
        cont1 -= 1
        soma1 += multiplicacao1
    nova_multiplicacao1 = soma1 * 10
    resto_divisao1 = nova_multiplicacao1 % 11
    if resto_divisao1 > 9:
        resto_divisao1 = 0
    else:
        resto_divisao1 = resto_divisao1    
    return resto_divisao1

def sncpf(n):
    resto_divisao, c, novos1 = validador_cpf1(n)
    resto_divisao1 = validador_cpf2(n)
    cpf_gerado = f'{novos1}{resto_divisao}{resto_divisao1}'
    total = n.replace('.', '').replace('-', '')
    if cpf_gerado == total:
        return True
    return False

def cadastro():
    cartao = {}
    while True:
        nome_usuario = input('digite seu nome completo: ')
        if validador_nome(nome_usuario) == False:
            cartao['nome'] = nome_usuario

            ano_nascimento = input('digite seu ano de nascimento: ')
            if validador_data(ano_nascimento):
                cartao['data'] = ano_nascimento

                #criar um digito para o cartao tipo 94534563-34
                cpf = input('digite seu cpf: ')
                if sncpf(cpf):
                    cartao['cpf'] = cpf
                    for k,v in cartao.items():
                        print(f'{k}: {v}')
                    print('Cadastrado com sucesso')
                    break

                else:
                    print('cpf inválido')
            else:
                print('Data de nascimento inválida')
        else:
            print('nome inválido')            

cadastro()