def main():
    # escribe tu código abajo de esta línea
    mensaje = int(input("Dame el número de mensaje: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    m = mensaje * 0.80 + megas * 0.80 + minutos * 0.80
    print("El costo mensual es:", m)


if __name__ == '__main__':
    main()
