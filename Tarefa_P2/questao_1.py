from datetime import datetime

def calc_angulo(horas, minutos):
    angulo_horas = (horas % 12) * 30
    angulo_minutos = minutos * 6

    # Calcula a diferença entre os dois ângulos
    angulo = abs(angulo_horas - angulo_minutos)

    # O menor ângulo será o mínimo entre a diferença e 360° - diferença
    menor_angulo = min(angulo, 360 - angulo)

    return menor_angulo


def mostrar_angulo():
    while True:
        input_horario = input()

        if input_horario.lower() == 'f':
            print("Fim...")
            break

        # Decidi defender dessa forma, pois ele "verifica" o 0 a esquerda e também se é um horário válido entre 00hr e 23:59
        if len(input_horario) == 5 and input_horario[2] == ':':
            try:
                horario = datetime.strptime(input_horario, "%H:%M")
                horas = horario.hour
                minutos = horario.minute

                angulo = calc_angulo(horas, minutos)
                print(f"O menor ângulo é de {angulo:.0f}°")
            except ValueError:
                print("Input inválido")
        else:
            print("Input inválido")

mostrar_angulo()