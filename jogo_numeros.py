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

        for c in range(0, 4): #pula uma linha quando da 4 listas
            for l in range(0,4): #printa 4 listas
                print(self.mapa[posicao], end='') #printa elas
                posicao += 1 
            print()

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

        for numero in self.mapa: #ver todo o mapa no self.mapa
            if len(numero) != 0: #verifica se tem algo na lista
                listas_das_posicoes.append(posicao_cima)

            posicao_cima += 1

        total = 0
        for posicao in listas_das_posicoes:
            if posicao not in [0, 1, 2, 3]: # se a posição não entiver em 0,1,2,3
                del self.mapa[listas_das_posicoes[total]]
                total += 1

        print(listas_das_posicoes)





tela = PrimeiraJogada()

tela.primeira_jogada()


    
