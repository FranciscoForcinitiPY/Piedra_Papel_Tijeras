import random


def juego_p_p_t():

    print("Bienvenido al juego de Piedra, Papel o Tijeras \n")
    print("elige una de las Opciones y ganale a la maquina \n")

    puntos_maquina = 0 
    puntos_jugador = 0

    """
        Se muestran las opciones a elegir 
        """
    opciones = ["Piedra", "Papel", "Tijeras"]
    reglas = {
            "Piedra":"Tijeras",
            "Tijeras":"Papel",
            "Papel":"Piedra"
        }

    while True:
        print("\n-------------------")
        """
        Contador de puntos
        """
        print(f"Jugador : {puntos_jugador}")
        print(f"Maquina : {puntos_maquina}")

        """
        muestra por pantalla las opciones que estan dentro de la lista y 
        se le pide al usuario que seleccion una opcion
        """
        for i, opcion in enumerate(opciones,start=1):
            print(f"{i} - {opcion}")

        try:
            jugador = int(input("\nElige la opción 1, 2 o 3: "))
        except ValueError:
            print("Ingresá un número válido")
            continue

        """
        Validacion de numeros, 'que sea uno de las opciones dadas'
        """
        if jugador not in [1, 2, 3]:
            print("Opción inválida")
            continue
        jugada_jugador = opciones[jugador - 1]
        jugada_maquina = random.choice(opciones)

        """
        condicionales para dar resultado de EMPATE - GANADOR _ PERDEDOR
        """
        if jugada_jugador == jugada_maquina:
            print(f"Es empate, ambos eligieron {jugada_maquina}")
            """
            suma puntos a ambos por el empate
            """
            puntos_maquina += 1
            puntos_jugador += 1
        elif reglas[jugada_jugador] == jugada_maquina:
            print(f"Ganaste! {jugada_jugador} le gana a {jugada_maquina}")
            """
            Suma punto al jugador por gannar
            """
            puntos_jugador += 1
        else:
            print(f"Perdiste! {jugada_maquina} le gana a {jugada_jugador}")
            """
            Suma punto a la maquina por ganar
            """
            puntos_maquina += 1
        if puntos_jugador == 3 :
            print("\n🎉 Ganaste el juego!")
            # Fin del Juego
            break
        elif puntos_maquina == 3:
            print("\n💀 Perdiste el juego")
            # Fin del Juego
            break

if __name__ == "__main__":
    juego_p_p_t()
