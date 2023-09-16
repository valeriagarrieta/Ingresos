#La aplicacion debe prmitir registrar ingresos y contar el saldo 
#debe permitir egresos y mostrar el saldo
#si el egreso es mayor al saldo npo dbera permitir el rtiro y mostrara un mensaje de saldo insuficiente
#la aplicacion llevara un registro de los movimientos indicando el numero de ingresos y de egresos 

#saldo = 0
saldo = 0
acumIngrsos = 0
acumEgresos = 0

isOn = int(input("Ingrese 1 para inicialixar el servicio: "))

while isOn !=0:

    opc= int(input("1. Ingreso:/n 2. Egreso/n 3. salir"))

    if opc == 1:
        ingreso = int(input("Registre el ingreso: "))

        saldo = saldo + ingreso 

        print(f"su saldo es ${saldo}")
        acumIngrsos+=1
        print(acumIngrsos)
        #acumIngrsos = acumIngrsos +1
    elif opc==2:
        egreso = int(input("Registre el monto a retirar:"))

        saldo = saldo - egreso

        if saldo < 0:
            print("Saldo insuficiente ")
            saldo = saldo + egreso
            print(saldo)

        else:
            print(f"su saldo es:${saldo}")
            acumEgresos+= 1
            print(acumEgresos)

    elif opc==3:
        print("salir")
        isOn=0
    else:
        print("Ingrse una opcion valida")