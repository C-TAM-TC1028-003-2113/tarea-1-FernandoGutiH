def main():
    # escribe tu código abajo de esta línea
    mesant = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    final = (mesant + ingresos - egresos - (cheques * 13)) * 0.925
    print("El saldo final de la cuentaes:", final)


if __name__ == '__main__':
    main()
