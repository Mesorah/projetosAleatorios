import os
from time import sleep

"""
    Cadastro de perfil do jogador
"""
class Perfil:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cidade = None
        self.dinheiro = 0
        self.xp = 0
        self.energia = 100
        self.maximo_energia = 100

    def nome_jogador(self):
        qual_seu_nome = input('Qual o nome de seu jogador? ')
        self.nome = qual_seu_nome
        return self.nome

    def idade_jogador(self):
        while True:
            qual_sua_idade = input(f'Qual a idade de {self.nome}? ')

            try:
                qual_sua_idade = int(qual_sua_idade)
                self.idade = qual_sua_idade
                break
            except ValueError:
                print('Idade inválida')

        return self.idade
    
    def cidade_jogador(self):
        invalido = False
        while True:
            qual_sua_cidade = input(f'Em qual cidade {self.nome} nasceu? ')

            for letra in qual_sua_cidade:
                if letra.isdigit():
                    invalido = True
            
            if not invalido:
                self.cidade = qual_sua_cidade
                print(self.cidade)
                return self.cidade
            else:
                print('Nome de cidade inválida')

    def salario(self, valor):
        self.dinheiro += valor

    """ Verifica o salário para calcular quantos xp ira ganhar """
    def experiencia(self, valor):
        total = valor / 220
        self.xp += total

    def menos_energia(self, valor):
        if valor < 3000:
            self.energia -= 51
            return self.energia
        
    def loja(self):
        while True:
            print('''
UPGRADES
[1] + 10 de energia | R$ 1500
                          
ITENS
[2] Casa | R$ 250000''')
            escolha_loja = input('R: ')
            try:
                escolha_loja = int(escolha_loja)
                break
            except ValueError:
                print('Digite uma opção válida')
                Perfil.clear_screen()
        if escolha_loja == 1 and self.dinheiro >= 1500:
            self.maximo_energia += 10
            print(f'Durma para ter {self.maximo_energia}')
            self.dinheiro -= 1500
        
        elif escolha_loja == 2 and self.dinheiro >= 25000:
            print('Parabéns você comprou uma casa')
            self.dinheiro -= 250000
        else:
            print('Dinheiro insuficiente')

    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    
    def exibir_perfil(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Cidade: {self.cidade}
Profissão: Vagabundo
Dinheiro: {self.dinheiro}
Experiência: R$ 0
Energia: 100%''')

    def exibir_perfil_inteiro(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Cidade: {self.cidade}
Profissão: {self.trabalho}
Dinheiro: R$ {self.dinheiro}
Experiência: {self.xp}
Energia: {self.energia}%''')

"""
    Os trabalhos disponíveis para o jogador
"""
class Trabalho(Perfil):
    def __init__(self):
        super().__init__()
        self.trabalho = None
        self.salario_trabalho = 0
        self.dict_trabalho = None

    """
        Esta primeira parte serve para criar os empregos, e depois usar um for para que printe bonitinho e certo no terminal
    """
    def trabalhos_disponiveis(self):
        lista_de_trabalhos_disponiveis_0 = [
            {'numero_do_emprego': 1, 'nome': 'Caixista de supermercado', 'salario': 1100, 'nivel_de_experiencia': 0},
            {'numero_do_emprego': 2, 'nome': 'Auxiliar de limpeza', 'salario': 1100, 'nivel_de_experiencia': 0}
        ]

        lista_de_trabalhos_disponiveis_60 = [
            {'numero_do_emprego': 3, 'nome': '__', 'salario': 0000, 'nivel_de_experiencia': 60},
            {'numero_do_emprego': 4, 'nome': '__', 'salario': 0000, 'nivel_de_experiencia': 60}
        ]
        
        for trabalho in lista_de_trabalhos_disponiveis_0:
            numero_do_emprego = trabalho['numero_do_emprego']
            nome = trabalho['nome']
            salario = trabalho['salario']
            nivel = trabalho['nivel_de_experiencia']
            print(f'Número do emprego: {numero_do_emprego} | Emprego: {nome} | Salário: R${salario} | Nível de experiência: {nivel}')

        print()

        """
            O resto serve para validar se o número de trabalho existe
        """
        while True:
            escolha_trabalho = input('Qual trabalho você escolhe? ')
            trabalho_encontrado = False
            try:
                escolha_trabalho = int(escolha_trabalho)
                for trabalhos in lista_de_trabalhos_disponiveis_0:
                    if escolha_trabalho == trabalhos['numero_do_emprego']:
                        print()
                        print('trabalho selecionado')
                        trabalho_encontrado = True
                        break
                if not trabalho_encontrado:
                    print('Número de trabalho não encontrado')
            except ValueError:
                print('Por favor, digite o número do trabalho')
            
            if trabalho_encontrado:
                break
        
        # Pega o dicionário do trabalho escolhido e o nome dele
        trabalho_escolhido = lista_de_trabalhos_disponiveis_0[escolha_trabalho -1]
        self.trabalho = trabalho_escolhido['nome']
        self.salario_trabalho = trabalho_escolhido['salario']
        self.dict_trabalho = trabalho_escolhido['numero_do_emprego']

        return self.trabalho, self.salario_trabalho, self.dict_trabalho
    
""" Classe que relaciona com o xp e o dinheiro etc"""
class ComecaTrabalhar(Trabalho):
    def __init__(self):
        super().__init__()

    def exemplo_trabalho(self, msg):
        print(f'{msg}')
        sleep(3)
        print('Almoçando...')
        sleep(3)
        print('Pegando o salário com o chefe...')
        sleep(3)
        print(f'+ R${self.salario_trabalho}')
        self.dinheiro += self.salario_trabalho

        self.experiencia(self.salario_trabalho)
        print(f'+ {self.salario_trabalho / 220} EXP')

        self.menos_energia(self.salario_trabalho)

    """ Função para cada emprego no qual ganha o dinheiro e xp """
    def trabalho_caixista(self):
        self.exemplo_trabalho('Passando os produtos...')

    def trabalho_auxiliar(self):
        self.exemplo_trabalho('Limpando a privada...')


"""
    Deixar como última classe e herde da última classe, a classe Exibit só serve para exibir as informações
"""
class Exibir(ComecaTrabalhar):
    def __init__(self):
        super().__init__()
    
    # Tudo oque irá aparecer no terminal do usuário
    def tela(self):
        # Obrigado a fazer

        self.nome_jogador()
        self.idade_jogador()
        self.cidade_jogador()

        Perfil.clear_screen()

        self.exibir_perfil()
        
        print()

        _, salario, trabalho = self.trabalhos_disponiveis()

         # Não obrigado
        sleep(2)
        Perfil.clear_screen()

        # Loop da tela que o usuário irá ver
        while True:
            certo = False
            print('''
[1] Para trabalhar
[2] Para dormir
[3] Ir para o mercado
[4] Para exibir o perfil''')
            escolha = input('R: ')
            try:
                escolha = int(escolha)
                certo = True
            except ValueError:
                print('Digite uma opção válida')
                Perfil.clear_screen()
        
            if certo:
                if escolha == 1 and self.energia > 51:
                    if trabalho == 1:
                        self.trabalho_caixista()
                        Perfil.clear_screen()

                    elif trabalho == 2:
                        self.trabalho_auxiliar()
                        Perfil.clear_screen()

                elif escolha == 2:
                    print('dormindo...')
                    sleep(3)
                    print('energia recuperada!')
                    self.energia = self.maximo_energia
                    sleep(1)
                    Perfil.clear_screen()

                elif escolha == 3:
                    self.loja()
                    Perfil.clear_screen()
                
                elif escolha == 4:
                    self.exibir_perfil_inteiro()

                elif self.energia < 51:
                    print('energia insuficiente')
                
                else:
                    print('ERROR')
                    sleep(1)
                    Perfil.clear_screen()




jogo = Exibir()
jogo.tela()