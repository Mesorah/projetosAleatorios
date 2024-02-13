from random import randint

class PrimeiraJogada: # classe para a primeira jogada
    def __init__(self):
        self.mapa = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] #mapa original
       #self.mapa = [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]

    def primeira_jogada(self): #funçao para adicionar o numero 2, duas vezes em lugares aleatorios
        
        numero_aleatorio1 = randint(0, 15) #gerando o primeiro lugar

        if len(self.mapa[numero_aleatorio1]) == 0: #verificando se tem um espaço para gerar
            self.mapa[numero_aleatorio1].append(2) #adicionando o numero

        funcionou = False
        while not funcionou: # enquanto funcionou for falso
            numero_aleatorio2 = randint(0, 15) #gerando o segundo lugar

            if len(self.mapa[numero_aleatorio2]) == 0 and numero_aleatorio2 != numero_aleatorio1: #verificando se tem um espaço para gerar e se o numero não é igual ao primeiro
                self.mapa[numero_aleatorio2].append(2) #adicionando o numero
                funcionou = True #se for o append o funcionou fica true e quebra o loop

        self.mostrar_mapa()

    def mostrar_mapa(self):
        posicao = 0

        for c in self.mapa:
            print(c, end='')
            posicao += 1
            if posicao == 4: # se chegar em 4 pula a linha
                print()
                posicao = 0

        self.escolher_movimento()

    def escolher_movimento(self):
        while True:
            print()
            escolha_seu_movimento = input('digite para qual direção quer ir (cima, baixo, esquerda, direita) ').lower() #escolher movimento
            if escolha_seu_movimento == 'cima':
                self.movimento_cima() #aciona a outra função
                break

            else:
                print('digite algum movimento existente')


    def movimento_cima(self): #função caso a pessoa escola 'cima'
        posicao_cima = 0
        listas_das_posicoes = []
        listas_dos_numeros = []

        for numero in self.mapa: #ver todo o mapa no self.mapa
            if len(numero) != 0: #verifica se tem algo na lista
                listas_das_posicoes.append(posicao_cima)
                listas_dos_numeros.append(numero.copy()[0])

            posicao_cima += 1
 #guarda os numeros que vao mudar de posiçao

        #for c in self.mapa: #pega os numero de tudo no mapa
        for posicao in listas_das_posicoes:
            if posicao > 3: #se a posição não entiver em 0,1,2,3
                self.mapa[posicao].clear() #limpa a posiçao do numero    
                    
            #break
        
        tot = -1
        for posicao in listas_das_posicoes: #pega as posiçoes
            tot += 1

            if posicao in [0,1,2,3]:
                continue
            else:
                if posicao - 15 >= 0:
                    print(33333333333333333333333333333333333333333)
                    posicao_num = posicao - 15 #recebe a posicao como se tivesse na primeira linha

                    if len(self.mapa[posicao_num]) == 0: #verifica se a lista ta vazia
                        self.mapa[posicao_num].append(listas_dos_numeros[tot])

                    elif self.mapa[posicao_num][0] == listas_dos_numeros[tot]: #icrementa a fundição dos 2 numeros
                        self.mapa[posicao_num].remove(listas_dos_numeros[tot])
                        self.mapa[posicao_num].append(listas_dos_numeros[tot] *2)

                    elif len(self.mapa[posicao_num +8]) == 0 and self.mapa[posicao_num] != posicao: 
                        posicao_num = posicao - 12 #recebe a posicao como se tivesse na segunda linha
                        if len(self.mapa[posicao_num]) == 0:
                            self.mapa[posicao_num].append(listas_dos_numeros[tot])

                        else:
                            posicao_num = posicao - 8 #recebe a posicao como se terceira na segunda linha
                            if len(self.mapa[posicao_num]) == 0:
                                self.mapa[posicao_num].append(listas_dos_numeros[tot])   

                    else:
                        if self.mapa[posicao - 12][0] == listas_dos_numeros[tot]:
                            self.mapa[posicao - 12].append(listas_dos_numeros[tot] *2)
                            self.mapa[posicao - 12].remove(listas_dos_numeros[tot])
                        else:
                            self.mapa[posicao].append(listas_dos_numeros[tot])


                elif posicao - 12 >= 0:
                    posicao_num = posicao - 12 #recebe a posicao como se tivesse na primeira linha

                    if len(self.mapa[posicao_num]) == 0: #verifica se a lista ta vazia
                        self.mapa[posicao_num].append(listas_dos_numeros[tot])

                    elif self.mapa[posicao_num][0] == listas_dos_numeros[tot]: #icrementa a fundição dos 2 numeros
                        self.mapa[posicao_num].remove(listas_dos_numeros[tot])
                        self.mapa[posicao_num].append(listas_dos_numeros[tot] *2)

                    elif len(self.mapa[posicao_num +4]) == 0 and self.mapa[posicao_num] != posicao: 
                        posicao_num = posicao - 8 #recebe a posicao como se tivesse na segunda linha
                        if len(self.mapa[posicao_num]) == 0:
                            self.mapa[posicao_num].append(listas_dos_numeros[tot])

                        else:
                            posicao_num = posicao - 4 #recebe a posicao como se terceira na segunda linha
                            if len(self.mapa[posicao_num]) == 0:
                                self.mapa[posicao_num].append(listas_dos_numeros[tot])   

                    else:
                        if self.mapa[posicao - 8][0] == listas_dos_numeros[tot]:
                            self.mapa[posicao - 8].append(listas_dos_numeros[tot] *2)
                            self.mapa[posicao - 8].remove(listas_dos_numeros[tot])
                        else:
                            self.mapa[posicao].append(listas_dos_numeros[tot])
                        


                elif posicao - 8 >= 0:
                    posicao_num = posicao - 8
                    if len(self.mapa[posicao_num]) == 0:
                        self.mapa[posicao_num].append(listas_dos_numeros[tot])
                    
                    elif self.mapa[posicao_num][0] == listas_dos_numeros[tot]: #icrementa a fundição dos 2 numeros
                        self.mapa[posicao_num].remove(listas_dos_numeros[tot])
                        self.mapa[posicao_num].append(listas_dos_numeros[tot] *2)

                    elif len(self.mapa[posicao_num + 4]) == 0 and self.mapa[posicao_num] != posicao: #pega o posicao_num -4
                        posicao_num = posicao - 4
                        if len(self.mapa[posicao_num]) == 0:
                                self.mapa[posicao_num].append(listas_dos_numeros[tot])

                    else:
                        if self.mapa[posicao - 4][0] == listas_dos_numeros[tot]:
                            self.mapa[posicao - 4].append(listas_dos_numeros[tot] *2)
                            self.mapa[posicao - 4].remove(listas_dos_numeros[tot])
                        else:
                            self.mapa[posicao].append(listas_dos_numeros[tot])
                        

                elif posicao - 4 >= 0:
                    posicao_num = posicao - 4
                    if len(self.mapa[posicao_num]) == 0:
                        self.mapa[posicao_num].append(listas_dos_numeros[tot])

                    elif self.mapa[posicao_num][0] == listas_dos_numeros[tot]: #incrementa a fusão dos 2 numeros
                        self.mapa[posicao_num].remove(listas_dos_numeros[tot])
                        self.mapa[posicao_num].append(listas_dos_numeros[tot] * 2)

                    else:
                        self.mapa[posicao].append(listas_dos_numeros[tot])
                        
        self.spawna_numero()


        #print(listas_das_posicoes)
    def spawna_numero(self):
        funcionou = False
        while not funcionou:
            novo_numero = randint(0, 15)
            if len(self.mapa[novo_numero]) == 0:
                self.mapa[novo_numero].append(2)
                funcionou = True

        self.mostrar_mapa()



tela = PrimeiraJogada()

tela.primeira_jogada()


    
