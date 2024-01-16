def validador_cep(cep):
    numeros = []
    if len(cep) == 9:
        for c in cep:
            numeros.append(c)
        if cep.count('-') == 1:
            numeros.remove('-')
            for c in numeros:
                try:
                    c = int(c)
                    return 'Válido'
                except ValueError:
                    return 'Inválido'
        else:
            return 'Inválido'
cep = input('digite sua senha: ')
print(validador_cep(cep))