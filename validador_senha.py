def validador_senha(senha):
    tam = False
    num = False
    esp = False
    mai = False
    men = False
    if len(senha) >= 8:
        tam = True
        for c in senha:
            if c.isnumeric():
                num = True
            if not c.isalpha() and not c.isnumeric():
                esp = True
            if c.isupper():
                mai = True
            if c.islower():
                men = True
    if tam and num and esp and mai and men:
        return 'Válido'
    else:
        return 'Inválido'
    
senha = input('digite sua senha: ')
print(validador_senha(senha))