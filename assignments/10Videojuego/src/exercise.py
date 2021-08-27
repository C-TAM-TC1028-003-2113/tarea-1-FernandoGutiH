def main():
    # escribe tu código abajo de esta línea
    nuevo = int(input("Dame la cantidad de juegos nuevos: "))
    usado = int(input("Dame la cantidad de juegos usados: "))
    n = nuevo * 1000
    u = usado * 350
    n_u = n + u
    print ("El total de la compra es:", n_u)


if __name__ == '__main__':
    main()
