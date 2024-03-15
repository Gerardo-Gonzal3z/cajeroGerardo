saldo = 1000
contraseña = 225125
intentos = 0

while True:
    U = input("Ingrese su Usuario: ")
    if U == "BCC-2215":
        while intentos < 3:  # Limitar a tres intentos
            C = int(input("Escriba su Contraseña: "))
            if C == contraseña:
                print("*****")
                print("MENU")
                print("*****")
                print("1. RETIRAR")
                print("2. DEPOSITAR")
                print("3. REALIZAR TRANSFERENCIA")
                print("4. ESTADO DE CUENTA")
                print("5. SALIR")
                while True:
                    O = int(input("Seleccione una Opcion: "))
                    match O:
                        case 1:
                            print("*****")
                            print("MENU")
                            print("*****")
                            print("1. Q100")
                            print("2. Q300")
                            print("3. Q500")
                            print("4. Q1000")
                            print("5. SALIR")
                            R = int(input("SELECCIONE UNA CANTIDAD: "))
                            match R:
                                case 1:
                                    saldo -= 100
                                    print("Retiro Realizado")
                                case 2:
                                    saldo -= 300
                                    print("Retiro Realizado")
                                case 3:
                                    saldo -= 500
                                    print("Retiro Realizado")
                                case 4:
                                    saldo -= 1000
                                    print("Retiro Realizado")
                                case 5:
                                    break
                                case _:
                                    print("Opcion Incorrecta")
                        case 2:
                            print("*****")
                            print("MENU")
                            print("*****")
                            print("1. Q100")
                            print("2. Q300")
                            print("3. Q500")
                            print("4. Q1000")
                            print("5. SALIR")
                            D = int(input("SELECCIONE UNA CANTIDAD: "))
                            match D:
                                case 1:
                                    saldo += 100
                                    print("Deposito Realizado")
                                case 2:
                                    saldo += 300
                                    print("Deposito Realizado")
                                case 3:
                                    saldo += 500
                                    print("Deposito Realizado")
                                case 4:
                                    saldo += 1000
                                    print("Deposito Realizado")
                                case 5:
                                    break
                                case _:
                                    print("Opcion Incorrecta")
                        case 3:
                            print("REALIZAR TRANSFERENCIA")
                            cuenta_destino = input("Ingrese el número de cuenta del destinatario: ")
                            monto = float(input("Ingrese el monto a transferir: "))
                            if monto <= saldo:
                                saldo -= monto
                                print(f"La Transferencia de Q{monto} se a realizado a la cuenta {cuenta_destino}.")
                            else:
                                print("Saldo insuficiente para realizar la transferencia.")
                        case 4:
                            print("Su Saldo Disponible es de: " + str(saldo))
                            break
                        case 5:
                            exit()
                        case _:
                            print("Opcion Incorrecta")
                break  # Salir del bucle de intentos si la contraseña es correcta
            else:
                intentos += 1
                print("Contraseña Incorrecta. Intento", intentos, "de 3.")
        else:
            print("Ha excedido el límite de intentos. Saliendo del programa.")
            exit()
    else:
        print("Usuario Incorrecto")