#tratamento de excesao quando a pessoa taca qualquer coisa no cpf
def validador_nome(nome_usuario):
    for c in nome_usuario:
        if c.isdigit():
            return False
    if len(nome_usuario) >= 12:
        return True
    else:
        return None
    
def idade(data):
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

def criar_conta():
    while True:
        nome_usuario = input('digite seu nome completo: ')
        if validador_nome(nome_usuario):
            ano_nascimento = input('digite seu ano de nascimento: ')
            if idade(ano_nascimento):
                cpf = input('digite seu cpf: ')
                if sncpf(cpf):
                    return nome_usuario, ano_nascimento, cpf
                else:
                    print('Cpf inválido')
                    return False
            else:
                print('Data de nascimento inválido')
                return False
        else:
            print('Nome inválido')
            return False

def conta_usuario():
    informacoes = {}
    nome, idade, cpf = criar_conta()
    if nome is not None:
        informacoes = {
            'nome': nome,
            'idade': idade,
            'cpf': cpf}
        
        return informacoes['nome']
    
    return None
    
def saldo_bancario():
    valor = 100
    dinheiro = 0
    while True:
        saldo = int(input('Digite um valor para depositar: '))
        try:
            saldo = int(saldo)
            if saldo > valor:
                print('saldo insuficiente')
            else:
                print(f'você adicionou R${saldo}')
                valor -= saldo
                dinheiro = saldo
                return dinheiro
        except ValueError:
            print('Erro')
    
def ver_saldo(dinheiro):
    print(f'Saldo disponível: R${dinheiro}')

def transferencia(dinheiro):
    while True:
        nome_transferencia = input('qual o nome da pessoa que você quer enviar?')
        if validador_nome(nome_transferencia):
            quantia = input('qual a quantia que você quer enviar?')
            try:
                quantia = int(quantia)
                if quantia > dinheiro:
                    print('Valor insuficiente')
                else:
                    print(f'Enviado para {nome_transferencia} R${quantia}')
                    return dinheiro - quantia

            except ValueError:
                print('digite apenas valores inteiros')


def menu():
    global dinheiro
    dinheiro = 100

    nome_usuario = conta_usuario()

    if nome_usuario is not None:
        print(f'Bem vindo {nome_usuario}')
        saldo_bancario()
        while True:
            print('''
    oque gostaria de fazer?
    [1] transferencia bancária
    [2] ver seu saldo
    [3] para adicionar dinheiro''')
            escolha = input('digite sua opção: ')
            try:
                escolha = int(escolha)
                if escolha == 1:
                    dinheiro = transferencia(dinheiro)
                elif escolha == 2:
                    ver_saldo(dinheiro)
                elif escolha == 3:
                    dinheiro = saldo_bancario()
                else:
                    break
            except ValueError:
                print('erro')         
menu()