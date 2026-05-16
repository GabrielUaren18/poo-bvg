"""Modelagem da entidade Cliente para o sistema bancário."""


class Cliente:
    """Classe que representa um cliente no sistema bancário."""

    def __init__(self, nome: str, idade: int, saldo_inicial: float):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo_inicial
        self.__ativo = True

    # ===== GETTERS =====
    @property
    def nome(self):
        """Retorna o nome do cliente."""
        return self.__nome

    @property
    def idade(self):
        """Retorna a idade do cliente."""
        return self.__idade

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self.__saldo

    @property
    def ativo(self):
        """Indica se a conta está ativa."""
        return self.__ativo

    # ===== MÉTODOS =====
    def sacar(self, valor: float):
        """Realiza saque na conta do cliente.

        Args:
            valor (float): valor a ser sacado

        Raises:
            ValueError: se saldo for insuficiente ou conta inativa
        """
        if not self.__ativo:
            raise ValueError(f"Conta de {self.__nome} está inativa.")

        if valor > self.__saldo:
            raise ValueError(f"Saldo insuficiente para saque de R${valor:.2f}")

        self.__saldo -= valor
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")

    def depositar(self, valor: float):
        """Realiza depósito na conta do cliente.

        Args:
            valor (float): valor a ser depositado
        """
        if not self.__ativo:
            raise ValueError(f"Conta de {self.__nome} está inativa.")

        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")

    def desativar_conta(self):
        """Desativa a conta do cliente."""
        self.__ativo = False