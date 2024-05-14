from abc import ABC, abstractmethod

class Conta():
    agencia = "0001"
    def __init__(self, saldo, numero, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._cliente = cliente
        self._historico = historico


    def saldo_conta(self): # deu certo
        return self._saldo 
    
    def nova_conta(self, cliente, numero):
        return Conta(0, numero, cliente, historico=None)
        
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        pass

class Cliente():
    def __init__(self, endereco): #contas é LIST
        self.endereco = endereco
        self.contas = []
        
        
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Historico():
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)
        
        
class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        pass
        

class Transacao(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def registrar(self, conta):
        print('deposito ok')
        
    
class Saque(Transacao):
    def registrar(self, conta):
        print('saque ok')

teste_deposito = Deposito()  # funcionou
teste_deposito.registrar(1)  # funcionou
teste_saque = Saque()        # funcionou
teste_saque.registrar(1)     # funcionou
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

teste = Conta(1500, 1, "Maria", "Sem histórico")
print(teste.saldo_conta())