class Caixa:
    def __init__(self):
        # Definindo as notas e moedas disponíveis em centavos
        self.notas = [10000, 5000, 2000, 1000, 500, 200]
        self.moedas = [100, 50, 25, 10, 5, 1]
    def calcular_decomposicao(self, valor):
        valor = int(round(valor * 100))

        print("NOTAS:")
        for nota in self.notas:
            quantidade_notas = valor // nota
            valor %= nota
            print(f"{quantidade_notas} nota(s) de R$ {nota / 100:.2f}")

        print()
        print("MOEDAS:")
        for moeda in self.moedas:
            quantidade_moedas = valor // moeda
            valor %= moeda
            print(f"{quantidade_moedas} moeda(s) de R$ {moeda / 100:.2f}")


def main():
    caixa = Caixa()

    while True:
        try:
            valor = input().strip()
            if valor.lower() == 'f':
                print("Fim...")
                break

            valor_monetario = float(valor)
            if valor_monetario < 0:
                raise ValueError("Valor inválido")

            caixa.calcular_decomposicao(valor_monetario)
            print()
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
