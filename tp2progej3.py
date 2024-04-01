def calcular_vuelto(dinero_recibido, gasto):
    #calculo el vuelto
    vuelto = dinero_recibido - gasto

    #separo parte entera y parte decimal
    parte_entera = int(vuelto)
    parte_decimal = vuelto - parte_entera

    return parte_entera, parte_decimal

#listo

gasto = float(input("Ingrese el gasto realizado: "))
dinero_recibido = float(input("Ingrese la cantidad de dinero recibido: "))

parte_entera, parte_decimal = calcular_vuelto(dinero_recibido, gasto)

print(f"El vuelto es: {parte_entera} pesos y {parte_decimal} centavos.")
