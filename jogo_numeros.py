from random import randint

class Jogo2048: # classe para a primeira jogada

    def __init__(self):
        self.mapa = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] #mapa original
       #self.mapa = [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]


    def jogadas(self): #funçao para adicionar o numero 2, duas vezes em lugares aleatorios
        
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
            escolha_seu_movimento = input('digite para qual direção quer ir (cima, baixo, esquerda, direita) ').lower()[0] #escolher movimento
            
            if escolha_seu_movimento == 'c':
                self.movimento_cima() #aciona a outra função
                break

            elif escolha_seu_movimento == 'b':
                self.movimento_baixo()
                break

            elif escolha_seu_movimento == 'e':
                self.movimento_esquerda()
                break

            elif escolha_seu_movimento == 'd':
                self.movimento_direita()
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

                if posicao - 12 >= 0:
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


            posicoes_passadas = [0,1,2,3, 4,5,6,7, 8,9,10,11]
            for c in range(len(self.mapa)):
                if c in posicoes_passadas:
                    continue

                else:
                    numero_nao_duplicado = []
                    if self.mapa[c] == self.mapa[c- 4] and len(self.mapa[c]) != 0 and len(self.mapa[c-4]) != 0:
                        numero_nao_duplicado.append(self.mapa[c-4].copy())
                        apen = numero_nao_duplicado[0]
                        self.mapa[c - 4].pop()
                        self.mapa[c - 4].append(apen[0] * 2)
                        self.mapa[c].pop()

                    elif len(self.mapa[c]) != 0 and len(self.mapa[c-4]) == 0:
                        transferencia_numeros = []
                        transferencia_numeros.append(self.mapa[c][0])
                        self.mapa[c-4].append(transferencia_numeros[0])
                        
        self.fim_jogo()


    def movimento_baixo(self):
        #[0][1][2][3]
        #[4][5][6][7]
        #[8][9][10][11]
        #[12][13][14][15]

        posicoes_finais = [12, 13, 14, 15]
        posicoes_ja_utilizadas = []

        for movimento in range(len(self.mapa)):
            if movimento in posicoes_finais:
                continue


            else:
                if len(self.mapa[movimento]) > 0:

                    if  movimento + 12 in posicoes_finais: #juncao
                        if len(self.mapa[movimento + 12]) > 0 and self.mapa[movimento][0] == self.mapa[movimento + 12][0] and movimento not in posicoes_ja_utilizadas:
                            self.mapa[movimento + 12].append(self.mapa[movimento][0] * 2)
                            self.mapa[movimento + 12].remove(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                            posicoes_ja_utilizadas.append(movimento + 12)

                        elif len(self.mapa[movimento + 8]) > 0 :
                            if self.mapa[movimento][0] == self.mapa[movimento + 8][0] and movimento not in posicoes_ja_utilizadas:
                                self.mapa[movimento + 8].append(self.mapa[movimento][0] * 2)
                                self.mapa[movimento + 8].remove(self.mapa[movimento][0])
                                self.mapa[movimento].remove(self.mapa[movimento][0])
                                posicoes_ja_utilizadas.append(movimento + 8)

                        elif len(self.mapa[movimento + 4]) > 0:
                            if self.mapa[movimento][0] == self.mapa[movimento + 4][0] and movimento  not in posicoes_ja_utilizadas:
                                self.mapa[movimento + 4].append(self.mapa[movimento][0] * 2)
                                self.mapa[movimento + 4].remove(self.mapa[movimento][0])
                                self.mapa[movimento].remove(self.mapa[movimento][0])
                                posicoes_ja_utilizadas.append(movimento + 4)


                        elif len(self.mapa[movimento +12]) == 0: # ir pro + 12
                            self.mapa[movimento +12].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                                
                        elif len(self.mapa[movimento +8]) == 0: # ir pro + 8
                            self.mapa[movimento +8].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                        
                        elif len(self.mapa[movimento +4]) == 0: # ir pro + 4
                            self.mapa[movimento +4].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])


                    elif movimento + 8 in posicoes_finais: #juncao
                        if len(self.mapa[movimento + 8]) > 0 and self.mapa[movimento][0] == self.mapa[movimento + 8][0] and movimento not in posicoes_ja_utilizadas:
                            self.mapa[movimento + 8].append(self.mapa[movimento][0] * 2)
                            self.mapa[movimento + 8].remove(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                            posicoes_ja_utilizadas.append(movimento + 8)

                        elif len(self.mapa[movimento + 4]) > 0:
                            if self.mapa[movimento][0] == self.mapa[movimento + 4][0] and movimento not in posicoes_ja_utilizadas:
                                self.mapa[movimento + 4].append(self.mapa[movimento][0] * 2)
                                self.mapa[movimento + 4].remove(self.mapa[movimento][0])
                                self.mapa[movimento].remove(self.mapa[movimento][0])
                                posicoes_ja_utilizadas.append(movimento + 4)


                        elif len(self.mapa[movimento +8]) == 0: # ir pro + 8
                            self.mapa[movimento +8].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                        
                        elif len(self.mapa[movimento +4]) == 0: # ir pro + 4
                            self.mapa[movimento +4].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])

                    

                    elif movimento + 4 in posicoes_finais: #juncao
                        if len(self.mapa[movimento + 4]) > 0 and self.mapa[movimento][0] == self.mapa[movimento + 4][0] and movimento not in posicoes_ja_utilizadas:
                            self.mapa[movimento + 4].append(self.mapa[movimento][0] * 2)
                            self.mapa[movimento + 4].remove(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])
                            posicoes_ja_utilizadas.append(movimento + 4)
                        
                        elif len(self.mapa[movimento +4]) == 0: # ir pro + 4
                            self.mapa[movimento +4].append(self.mapa[movimento][0])
                            self.mapa[movimento].remove(self.mapa[movimento][0])

        posicoes_ja_utilizadas.clear()

        self.fim_jogo()
        

    def movimento_esquerda(self):
        #[0][1][2][3]
        #[4][5][6][7]
        #[8][9][10][11]
        #[12][13][14][15]

        for numero in range(len(self.mapa)):
            numeros_iniciais = [0, 4, 8, 12]

            if numero in numeros_iniciais:
                continue
            else:
                if numero - 3 in numeros_iniciais and len(self.mapa[numero]) > 0:
                    if len(self.mapa[numero -3]) > 0 and self.mapa[numero -3][0] == self.mapa[numero][0]: #junçao
                        self.mapa[numero -3].append(self.mapa[numero -3][0] * 2)
                        self.mapa[numero -3].remove(self.mapa[numero -3][0])
                        self.mapa[numero].remove(self.mapa[numero][0])
                    
                    elif len(self.mapa[numero -2]) > 0: # ir pro -2
                        if self.mapa[numero -2][0] == self.mapa[numero][0]: #juncao       
                            self.mapa[numero -2].append(self.mapa[numero -2][0] * 2)
                            self.mapa[numero -2].remove(self.mapa[numero -2][0])
                            self.mapa[numero].remove(self.mapa[numero][0])
                    
                    elif len(self.mapa[numero -1]) > 0: # ir pro -1
                        if self.mapa[numero -1][0] == self.mapa[numero][0]: #juncao       
                            self.mapa[numero -1].append(self.mapa[numero -1][0] * 2)
                            self.mapa[numero -1].remove(self.mapa[numero -1][0])
                            self.mapa[numero].remove(self.mapa[numero][0])


                    elif len(self.mapa[numero -3]) == 0: # ir pro -3
                        self.mapa[numero -3].append(self.mapa[numero][0])
                        self.mapa[numero].remove(self.mapa[numero][0])


                    elif len(self.mapa[numero -2]) == 0: # ir pro -2
                            self.mapa[numero -2].append(self.mapa[numero][0])
                            self.mapa[numero].remove(self.mapa[numero][0])

 
                    elif len(self.mapa[numero -1]) == 0: # ir pro -1 #bug aqui
                            self.mapa[numero -1].append(self.mapa[numero][0])
                            self.mapa[numero].remove(self.mapa[numero][0])


                elif numero - 2 in numeros_iniciais and len(self.mapa[numero]) > 0:
                    if len(self.mapa[numero -2]) > 0 and self.mapa[numero -2][0] == self.mapa[numero][0]: #juncao       
                        self.mapa[numero -2].append(self.mapa[numero -2][0] * 2)
                        self.mapa[numero -2].remove(self.mapa[numero -2][0])
                        self.mapa[numero].remove(self.mapa[numero][0])

                    elif len(self.mapa[numero -1]) > 0: # ir pro -1
                        if self.mapa[numero -1][0] == self.mapa[numero][0]: #juncao       
                            self.mapa[numero -1].append(self.mapa[numero -1][0] * 2)
                            self.mapa[numero -1].remove(self.mapa[numero -1][0])
                            self.mapa[numero].remove(self.mapa[numero][0])

                    elif len(self.mapa[numero -2]) == 0: # ir pro -2
                        self.mapa[numero -2].append(self.mapa[numero][0])
                        self.mapa[numero].remove(self.mapa[numero][0])


                    elif len(self.mapa[numero -1]) == 0: # ir pro -1
                        self.mapa[numero -1].append(self.mapa[numero][0])
                        self.mapa[numero].remove(self.mapa[numero][0])
                

                elif numero - 1 in numeros_iniciais and len(self.mapa[numero]) > 0:
                    if len(self.mapa[numero -1]) > 0 and self.mapa[numero -1][0] == self.mapa[numero][0]: #juncao       
                        self.mapa[numero -1].append(self.mapa[numero -1][0] * 2)
                        self.mapa[numero -1].remove(self.mapa[numero -1][0])
                        self.mapa[numero].remove(self.mapa[numero][0])

                    elif len(self.mapa[numero -1]) == 0: # ir pro -1
                        self.mapa[numero -1].append(self.mapa[numero][0])
                        self.mapa[numero].remove(self.mapa[numero][0])

                if numero in [3, 7, 11, 15] and len(self.mapa[numero]) > 0:
                    if len(self.mapa[numero -1]) > 0:
                        if self.mapa[numero][0] == self.mapa[numero -1][0]:
                            self.mapa[numero -1].append(self.mapa[numero -1][0] * 2)
                            self.mapa[numero -1].remove(self.mapa[numero -1][0])
                            self.mapa[numero].remove(self.mapa[numero][0])
                    else:
                        if len(self.mapa[numero -2]) > 0:
                            self.mapa[numero -1].append(self.mapa[numero][0])
                            self.mapa[numero].remove(self.mapa[numero][0])
                else:
                    continue

        self.fim_jogo()

    
    def movimento_direita(self):
        #[0][1][2][3]
        #[4][5][6][7]
        #[8][9][10][11]
        #[12][13][14][15]

        numeros_do_canto_d = [3,7,11,15]
        posicoes_ja_utilizadas = []

        for posicao in range(len(self.mapa)):
            if posicao in numeros_do_canto_d:
                continue

            else:
                if len(self.mapa[posicao]) > 0:

                    if posicao + 3 in numeros_do_canto_d: #junçao
                        if len(self.mapa[posicao +3]) > 0 and self.mapa[posicao +3][0] == self.mapa[posicao][0] and posicao not in posicoes_ja_utilizadas:
                            self.mapa[posicao +3].append(self.mapa[posicao +3][0] * 2)
                            self.mapa[posicao +3].remove(self.mapa[posicao +3][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            posicoes_ja_utilizadas.append(posicao + 3)

                        
                        elif len(self.mapa[posicao +2]) > 0 and posicao not in posicoes_ja_utilizadas and self.mapa[posicao +2][0] == self.mapa[posicao][0]: #junçao
                            self.mapa[posicao +2].append(self.mapa[posicao +2][0] * 2)
                            self.mapa[posicao +2].remove(self.mapa[posicao +2][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            posicoes_ja_utilizadas.append(posicao + 2)

                        elif len(self.mapa[posicao +1]) > 0 and posicao not in posicoes_ja_utilizadas and self.mapa[posicao +1][0] == self.mapa[posicao][0]: #junçao
                            self.mapa[posicao +1].append(self.mapa[posicao +1][0] * 2)
                            self.mapa[posicao +1].remove(self.mapa[posicao +1][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            posicoes_ja_utilizadas.append(posicao + 1)



                        elif len(self.mapa[posicao +3]) == 0: # ir pro + 3
                            self.mapa[posicao +3].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])

                        elif len(self.mapa[posicao +2]) == 0: # ir pro + 2
                            self.mapa[posicao +2].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                        
                        elif len(self.mapa[posicao +1]) == 0: # ir pro + 1
                            self.mapa[posicao +1].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])


                    elif posicao + 2 in numeros_do_canto_d: #junçao #############
                        if len(self.mapa[posicao +2]) > 0 and self.mapa[posicao +2][0] == self.mapa[posicao][0] and posicao not in posicoes_ja_utilizadas:
                            self.mapa[posicao +2].append(self.mapa[posicao +2][0] * 2)
                            self.mapa[posicao +2].remove(self.mapa[posicao +2][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            posicoes_ja_utilizadas.append(posicao + 2)

                        elif len(self.mapa[posicao +1]) > 0: #junçao
                            if self.mapa[posicao +1][0] == self.mapa[posicao][0] and posicao not in posicoes_ja_utilizadas:
                                self.mapa[posicao +1].append(self.mapa[posicao +1][0] * 2)
                                self.mapa[posicao +1].remove(self.mapa[posicao +1][0])
                                self.mapa[posicao].remove(self.mapa[posicao][0])
                                posicoes_ja_utilizadas.append(posicao + 1)



                        elif len(self.mapa[posicao +2]) == 0: # ir pro + 2
                            self.mapa[posicao +2].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            posicoes_ja_utilizadas.append(posicao + 1)
                        
                        elif len(self.mapa[posicao +1]) == 0: # ir pro + 1
                            self.mapa[posicao +1].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])
                            


                    elif posicao + 1 in numeros_do_canto_d: #junçao #############
                        if len(self.mapa[posicao +1]) > 0 and self.mapa[posicao +1][0] == self.mapa[posicao][0] and posicao not in posicoes_ja_utilizadas:
                            self.mapa[posicao +1].append(self.mapa[posicao +1][0] * 2)
                            self.mapa[posicao +1].remove(self.mapa[posicao +1][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])


                        elif len(self.mapa[posicao +1]) == 0: # ir pro + 1
                            self.mapa[posicao +1].append(self.mapa[posicao][0])
                            self.mapa[posicao].remove(self.mapa[posicao][0])


                    

        posicoes_ja_utilizadas.clear()
        self.fim_jogo()


    def fim_jogo(self):
        cheio = 0
        for c in range(len(self.mapa)):
            if len(self.mapa[c]) > 0:
                cheio += 1

            if cheio == 16:
                print('Fim de jogo')
                break

        if cheio != 16:
            self.spawna_numero()


    def spawna_numero(self):
        funcionou = False
        while not funcionou:
            novo_numero = randint(0, 15)
            if len(self.mapa[novo_numero]) == 0:
                self.mapa[novo_numero].append(2)
                funcionou = True

        self.mostrar_mapa()


tela = Jogo2048()

tela.jogadas()
