from abc import ABC, abstractmethod, abstractproperty

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realiza_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adiciona_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento,cpf,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class conta:
    def __init__(self,numero ,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self.saldo
        saldo_exedido = valor > saldo
        if saldo_exedido:
            print('Saldo insuficiente!')
        elif (valor > 0) :
            self._saldo -= valor 
            print("\nSaque completo!!!")
            return True
        else:
            print("Operação falhou!")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo +=valor
            print("Deposito realizado")
        else:
            print("Erro no deposito. O valor é invalido!")
            return False
        
        return True

class Contacorrente(conta):
    def __init__(self,numero ,cliente ,limite=500,limite_saques=3):
        super().__init_(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self,valor):
        numeros_saques = len([transacao for transacao in self.historico.trancacoes if transacao["tipo"]== Saque.__name__])

        excedeu_limite = valor >self.limite
        excedeu_saques = numeros_saques >= self.limite_saques
        if excedeu_limite:
            print("Erro na operação!")
        elif excedeu_saques:
            print("Operação Falhou!")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return(f"""
            Agência: {self.agencia}
            Contato: {self.numero}
            Titulaar: {self.cliente.nome}
""")

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
        })

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
