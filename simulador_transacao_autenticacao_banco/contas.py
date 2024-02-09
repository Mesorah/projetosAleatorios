#sacar, depositar, detalhes(ver saldo etc)
"""
Conta (ABC)
    ContaCorrente
    ContaPoupanca

    self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito"""


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #depositar, detalhes
        
    def depositar(self, saldo):
        print(f'depositando R${saldo}')
        self.saldo += saldo
    
    def detalhes(self):
        print(f'saldo da conta: R${self.saldo}')
        print(f'numero da conta: {self.conta}')
        print(f'agencia da conta: {self.agencia}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

#sacar   
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'sacando R${valor}')
        else:
            return f'saldo insuficiente, seu saldo atual é {self.saldo}'

#limite
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'sacando R${valor}')
        
        elif self.saldo + self.limite > valor:
            self.saldo -= valor
            print(f'você chegou no negativo, mas te emprestamos um dinheiro')
            print(f'sacando {valor}')

        else:
            print('valor insuficiente')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    conta = ContaPoupanca(3214, 45, 100)
    conta.depositar(45)
    conta.sacar(4)
                
    conta2 = ContaCorrente(3214, 45, 100, 100)
    conta2.depositar(5)
    conta2.sacar(106)
    conta2.detalhes()



