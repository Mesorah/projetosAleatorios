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

    def nome_jogador(self):
        qual_seu_nome = input('Qual o nome de seu jogador? ')
        self.nome = qual_seu_nome
        return self.nome

    def idade_jogador(self):
        while True:
            qual_sua_idade = input('Qual a idade de seu jogador? ')

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
            qual_sua_cidade = input('Qual cidade você nasceu? ')

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

    
    def exibir_perfil(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Cidade: {self.cidade}''')


"""
    Os trabalhos disponíveis para o jogador
"""
class Trabalho(Perfil):
    def __init__(self):
        super().__init__()
        self.trabalho = None
        self.salario_trabalho = 0

    """
        Esta primeira parte serve para criar os empregos, e depois usar um for para que printe bonitinho e certo no terminal
    """
    def trabalhos_disponiveis(self):
        lista_de_trabalhos_disponiveis = [
            {'numero_do_emprego': 1, 'nome': 'Caixista de supermercado', 'salario': 1100, 'nivel_de_experiencia': 0},
            {'numero_do_emprego': 2, 'nome': 'Auxiliar de limpeza', 'salario': 1100, 'nivel_de_experiencia': 0}
        ]
        
        for trabalho in lista_de_trabalhos_disponiveis:
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
                for trabalhos in lista_de_trabalhos_disponiveis:
                    if escolha_trabalho == trabalhos['numero_do_emprego']:
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
        trabalho_escolhido = lista_de_trabalhos_disponiveis[escolha_trabalho -1]
        self.trabalho = trabalho_escolhido['nome']
        self.salario_trabalho = trabalho_escolhido['salario']

        return self.trabalho, self.salario_trabalho
    
    
class ComecaTrabalhar(Trabalho):
    def __init__(self):
        super().__init__()

    # def exemplo_trabalho(self):
    #     print('Fazendo as tarefas')
    #     print('Almoçando')
    #     print('Pegando o salário com o chefe')

    #     salario += 1100
    #     experiencia += 5
    
    def trabalho_caixista(self):
        print(self.salario_trabalho)
        print('Passando os produtos...')
        sleep(3)
        print('Almoçando...')
        sleep(3)
        print('Pegando o salário com o chefe')
        print(f'+ R${self.salario_trabalho}')
        self.dinheiro += self.salario_trabalho


"""
    Deixar como última classe e herde da última classe, a classe Exibit só serve para exibir as informações
"""
class Exibir(ComecaTrabalhar):
    def __init__(self):
        super().__init__()

        #self.trabalho_caixista()
        # self.nome_jogador()
        # self.idade_jogador()
        # self.cidade_jogador()

        # os.system('cls')

        # self.exibir_perfil()

        # print()

        # self.trabalhos_disponiveis()





jogo = Exibir()
trabalho, salario = jogo.trabalhos_disponiveis()  # Obtém o trabalho e o salário
print(f'Trabalho escolhido: {trabalho}, Salário: {salario}')
jogo.trabalho_caixista()