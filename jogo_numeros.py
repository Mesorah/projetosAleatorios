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

            posicao_cima += 1
 #guarda os numeros que vao mudar de posiçao
        total = 0

        for c in self.mapa: #pega os numero de tudo no mapa
            for posicao in listas_das_posicoes:
                if posicao > 3: #se a posição não entiver em 0,1,2,3

                    for numero_sem_sublista in self.mapa[listas_das_posicoes[total]]: #pega a posiçao
                        listas_dos_numeros.append(numero_sem_sublista)

                    self.mapa[listas_das_posicoes[total]].clear() #limpa a posiçao do numero
                    
                total += 1
            break
        
        tot = 0
        for posicao in listas_das_posicoes:
            if posicao in [0,1,2,3]:
                continue
            elif posicao in [4,5,6,7]:
                if posicao == 4 and listas_das_posicoes not in [0]:
                    print('blz')
                elif posicao == 5 and listas_das_posicoes not in [1]:
                    print('blz')
                elif posicao == 6 and listas_das_posicoes not in [2]:
                    print('blz')
                elif posicao == 7 and listas_das_posicoes not in [3]:
                    print('blz')

            elif posicao in [8,9,10,11]:
                if posicao == 8 and listas_das_posicoes not in [4]:
                    print('blz')
                elif posicao == 9 and listas_das_posicoes not in [5]:
                    print('blz')
                elif posicao == 10 and listas_das_posicoes not in [6]:
                    print('blz')
                elif posicao == 11 and listas_das_posicoes not in [7]:
                    print('blz')

            elif posicao in [12,13,14,15]:
                if posicao == 12 and listas_das_posicoes not in [8]:
                    print('blz')
                elif posicao == 13 and listas_das_posicoes not in [9]:
                    print('blz')
                elif posicao == 14 and listas_das_posicoes not in [10]:
                    print('blz')
                elif posicao == 15 and listas_das_posicoes not in [11]:
                    print('blz')

        print(listas_dos_numeros, 'aaaaaa')
        #self.mostrar_mapa()

        print(listas_das_posicoes)





tela = PrimeiraJogada()

tela.primeira_jogada()


    
