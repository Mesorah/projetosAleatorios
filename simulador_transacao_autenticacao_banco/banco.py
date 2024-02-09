#checar agencia, checar cliente, checar conta, _checa_se_conta_e_do_cliente, authenticar, repr
import contas
import pessoas
class Banco:
    def __init__(self):
        self.agencia = []
        self.clientes = []
        self.contas = []

    ag = False
    def checa_agencia(self, numero_agencia):
        self.ag = numero_agencia in self.agencia

    cl = False
    def checa_clientes(self, cliente):
        self.cl = cliente in self.clientes
    
    cc = False
    def checa_conta(self, conta):
        self.cc = conta in self.contas

    ccc = False
    def checa_conta_cliente(self, pessoa, conta):
        self.ccc = conta is pessoa.conta
    
    def authenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        self.checa_agencia(conta.agencia) #conta.agencia
        self.checa_clientes(cliente)
        self.checa_conta(conta)
        self.checa_conta_cliente(cliente, conta)

        print(self.ag, self.cl, self.cc, self.ccc)

        if self.ag and self.cl and self.cc and self.ccc:
            return True
        return False



    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'



if __name__ == '__main__':
    c1 = pessoas.Pessoa('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Pessoa('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencia.extend([111, 222])


    if banco.authenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)


    #cp1 = contas.ContaPoupanca()