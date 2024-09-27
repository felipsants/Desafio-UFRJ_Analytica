from collections import defaultdict

def main():
    frequencias = defaultdict(int)

    while True:
        try:
            entrada = input().strip()

            if entrada.lower() == 'f':
                break

            numero = int(entrada)
            frequencias[numero] += 1

        except ValueError:
            continue


    for numero, frequencia in frequencias.items():
        print(f"O número {numero} apareceu {frequencia} vez(es).")
    print("Fim...")

if __name__ == "__main__":
    main()
