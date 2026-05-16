"""Script principal para testar a classe Cliente."""

from models.cliente import Cliente


def exibir_relatorio(clientes):
    """Exibe relatório geral dos clientes."""
    print("\n--- RELATÓRIO GERAL ---")
    for i, cliente in enumerate(clientes):
        print(
            f"ID: {i} | Nome: {cliente.nome} | Idade: {cliente.idade} | "
            f"Saldo: R${cliente.saldo:.2f} | Ativo: {cliente.ativo}"
        )


if __name__ == "__main__":
    clientes = [
        Cliente("João Silva", 30, 1000.0),
        Cliente("Maria Souza", 25, 500.0),
    ]

    # Testes de operações
    clientes[0].sacar(200.0)
    clientes[0].depositar(300.0)

    clientes[1].desativar_conta()

    try:
        clientes[1].sacar(100.0)
    except ValueError as e:
        print("Erro:", e)

    exibir_relatorio(clientes)