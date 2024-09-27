class Tabuleiro:
    def __init__(self):
        self.colunas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.linhas = [1, 2, 3, 4, 5, 6, 7, 8]

    def posicao_valida(self, posicao):
        return (
            len(posicao) == 2
            and posicao[0] in self.colunas
            and posicao[1].isdigit()
            and int(posicao[1]) in self.linhas
        )

    def movimentos_cavalo_gerador(self, posicao):
        if not self.posicao_valida(posicao):
            raise ValueError("Posição inválida")

        x = self.colunas[posicao[0]]
        y = int(posicao[1])

        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            new_x, new_y = x + dx, y + dy
            if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                coluna_letra = list(self.colunas.keys())[list(self.colunas.values()).index(new_x)]
                yield f"{coluna_letra}{new_y}"

def main():
    tabuleiro = Tabuleiro()

    while True:
        posicao_inicial = input().lower()
        if posicao_inicial == 'f':
            print("Fim...")
            break

        try:
            gen = tabuleiro.movimentos_cavalo_gerador(posicao_inicial)
            movimentos = sorted(list(gen))
            print(" ".join(movimentos))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
