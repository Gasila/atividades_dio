from abc import ABC, abstractmethod
from datetime import datetime


class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_operacao(self, conta, operacao):
        operacao.processar(conta)

    def vincular_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Usuario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf


class RegistroHistorico:
    def __init__(self):
        self._registros = []

    @property
    def registros(self):
        return self._registros

    def incluir_operacao(self, operacao):
        self._registros.append({
            "tipo": operacao.__class__.__name__,
            "valor": operacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class ContaBancaria:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = RegistroHistorico()

    @classmethod
    def criar_conta(cls, cliente, numero):
        return cls(numero, cliente)

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
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        print("Saque efetuado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self._saldo += valor
        print("Depósito efetuado com sucesso.")
        return True


class ContaCorrente(ContaBancaria):
    def __init__(self, numero, cliente, limite=500, max_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.max_saques = max_saques

    def sacar(self, valor):
        saques_realizados = len([
            op for op in self.historico.registros if op["tipo"] == "Saque"
        ])

        if saques_realizados >= self.max_saques:
            print("Limite de saques excedido.")
            return False

        if valor > self.limite:
            print("Saque excede o limite permitido.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return (
            f"Agência: {self.agencia}\n"
            f"Número: {self.numero}\n"
            f"Titular: {self.cliente.nome}"
        )


class OperacaoFinanceira(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def processar(self, conta):
        pass


class Saque(OperacaoFinanceira):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def processar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.incluir_operacao(self)


class Deposito(OperacaoFinanceira):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def processar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.incluir_operacao(self)
