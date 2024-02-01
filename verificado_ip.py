def solution(inputString):
    ponto = inputString.count('.')
    certo = False
    vish = True

    if inputString[0] != '.' or inputString[-1] != '.':

        if ponto == 3:

            numeros = []
            inteiro = []
            sla = inputString.split('.')

            for c in sla:
                numeros.append(c)
            try:
                for c in sla:
                    c = int(c)
                    inteiro.append(c)
            except ValueError:
                return False

            for inteiros in inteiro:
                if inteiros >= 0 and inteiros <= 255:
                    for d in numeros:
                        if d[0] == '0':
                            try:
                                d = d[1]
                                vish = True
                                if vish:
                                    return False
                                return False
                            except IndexError:

                                certo = True
                else:
                    return False

            if certo == True:
                return True
        else:
            return False
    else:
        return False
    
    return True


ip = input()
print(solution(ip))