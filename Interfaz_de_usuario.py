from datetime import datetime
from Parqueadero import Parqueadero
from Cliente import Cliente
from Vehiculo import Vehiculo


def verificar_entrada(limite_inferior, limite_superior, texto_input):
    while True:
        try:
            entrada = int(input(texto_input))
            if limite_inferior <= entrada <= limite_superior:
                return entrada
        except:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def verificar_sexo():
    while True:
        sexo = (input("Digite su genero (M/F): ")).upper()
        if sexo not in ["F", "M"]:
            print("porfavor, seleccione si es masculino o femenino (M/F).")
        else:
            return sexo


def verificar_fecha():
    while True:
        fecha_str = input("Digite la fecha (dd/mm/aaaa): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            return fecha
        except:
            print("Fecha ínvalida, ingrese la fecha en formato DD/MM/AAAA.")
    return fecha


def verificar_hora(texto):
    while True:
        tiempo_ingreso = input(texto)
        if len(tiempo_ingreso) == 5:
            hora_ingreso, minuto_ingreso = map(int, tiempo_ingreso.split(':'))

            hora_valida = True
            if hora_ingreso < 0 or hora_ingreso > 23 or minuto_ingreso < 0 or minuto_ingreso > 59:
                hora_valida = False

            if hora_valida:
                return tiempo_ingreso
            else:
                print(
                    "Hora inválida. Por favor, ingrese una hora válida en formato de 24 horas.")
        else:
            print("No olvide que son 5 caracteres como esta indicado (hh:mm)")



def verificar_año_fabricacion():
    año_actual = datetime.now().year
    año_fabricacion = input("Digite el año de fabricación de su vehículo: ")
    try:
        año_fabricacion = int(año_fabricacion)
        if año_fabricacion > año_actual:
            print("Año no válido. Por favor, ingrese un año válido.")
            return False
        elif año_actual - año_fabricacion < 10:
            return True
        else:
            print("El vehículo tiene más de 10 años de antigüedad.")
            return False
    except ValueError:
        print("Año no válido. Por favor, ingrese un año válido.")
        return False


print("Indique las dimensiones de su easy_parking")
print("1. 6x6")
print("2. 8x8")
print("3. 10x10")

tamaño = verificar_entrada(1, 3, "Opción: ")

if tamaño == 1:
    tamaño = 6
elif tamaño == 2:
    tamaño = 8
else:
    tamaño = 10

easy_parking = Parqueadero(tamaño)

while True:
    print("<====================================================================================================>")
    print("-----------------------------------------------------------------------------------------------------")
    print(" ")
    print("BIENVENIDO A EASY PARKING.  (⁠つ⁠≧ ⁠▽ ⁠≦⁠)⁠つ")
    print(" ")
    print("Hola Usuario somos un sistema de easy_parking creado por nuestros presidentes. \nEsperamos que tu instancia en nuestras instalaciones sea sasfactoria.")
    print(" ")
    print("¡RECUERDE! Para poder hacer uso de nuestros servicios debe de ser mayor de edad y su vehiculo no debe de tener más de 10 años de antiguedad.")
    print(" ")
    print("-----------------------------------------------------------------------------------------------------")
    print(" ")

    print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES.")
    print(" ")
    print("1. Registrar un vehiculo ")
    print("2. Retirar o buscar un vahiculo y generar factura")
    print("3. Calcular la tasa de ocupacion ")
    print("4. Total Dinero Ganado")
    print("5. Cantidad de vehiculos que han ingresado")
    print("6. Cantidad de puestos que han sido ocupados")
    print("7. Cantidad de Hombres y mujeres")
    print("8. porcentaje de vehiculos por marca")
    print("9. porcentaje de vehiculos por año de fabricación")
    print("10. Listar TODOS los vehiculos")
    print("11. salir del programa")
    print(" ")

    opcion_seleccionada = verificar_entrada(1, 11, "Por favor, seleccione una de las diez opciones disponibles: ")

    if opcion_seleccionada == 1:
        print(" ")
        print("INGRESANDO UN VEHICULO: ")
        propietario = input("Por favor ingrese su nombre y apellido: ").upper()
        sexo = verificar_sexo()
        print(">>Fecha de nacimiento<<")
        fecha_nacimiento = verificar_fecha()

        cliente_antiguo = True
        cliente_creado = easy_parking.obtener_cliente(propietario, fecha_nacimiento.day, fecha_nacimiento.month, fecha_nacimiento.year)

        if cliente_creado == None:
            cliente_creado = Cliente(propietario, sexo, fecha_nacimiento.day, fecha_nacimiento.month, fecha_nacimiento.year)
            cliente_antiguo = False

        if cliente_creado.verificar_mayor_edad() == True:

            marca = input("Digite la marca de su vehiculo: ").upper()
            placa = input("Digite la placa de su vehiculo: ") 
            print(">>Fecha de ingreso<<")
            fecha_ingreso = verificar_fecha()
            tiempo_ingreso = verificar_hora("Digite la hora y minutos de ingreso al parqueadero (hh:mm): ")
            tiempo_ingreso = datetime.strptime(tiempo_ingreso, "%H:%M").time()
            año_fabricacion = verificar_año_fabricacion()

            if año_fabricacion==True:
                precios = easy_parking.lista_precios
                print("\nPrecios disponibles:")
                for i, precio in enumerate(precios, start=1):
                    print(f"{i}. ${precio}") 
                tarifa = verificar_entrada(1, len(precios), "Opción: ")
                tarifa = precios[tarifa-1]

                # Ubicar el carro en un espacio disponible
                registro_exitoso = False
                for fila in range(easy_parking.tamaño):
                    for columna in range(easy_parking.tamaño):
                        if easy_parking.precios[fila, columna] == tarifa and easy_parking.matriz[fila, columna] == False:
                            print("--------------------------------------------------------------------")
                            
                            vehiculo_creado = Vehiculo(marca, placa, año_fabricacion, tarifa, fecha_ingreso, tiempo_ingreso, [fila, columna])
                            cliente_creado.agregar_vehiculo(vehiculo_creado)
                            easy_parking.contador_vehiculos +=1
                            easy_parking.matriz[fila, columna] = True

                            if cliente_antiguo == False:
                                easy_parking.registrar_cliente(cliente_creado)
                            registro_exitoso = True
                            print(f"Carro registrado con éxito. Precio: {tarifa}")
                            print(f"Carro ubicado en la posición: ({easy_parking.filas[fila]}{columna + 1})")
                            break
                            
                    if registro_exitoso == True:
                        break
                if registro_exitoso == False:
                    print("--------------------------------------------------------------------")
                    print("No se encontró un espacio disponible con el precio seleccionado.")
                    print("--------------------------------------------------------------------")

    elif opcion_seleccionada == 2:
        print("\nRETIRAR UN VEHÍCULO Y GENERAR FACTURA")

        while True:
            if len(easy_parking.clientes) != 0:
                listar_vehiculos= easy_parking.listar_clientes_y_vehiculos()
                nombre_cliente = input("Ingrese su nombre: ").upper()
                print("Digite la fecha de nacimiento")
                fecha_nacimiento = verificar_fecha()
                cliente = easy_parking.obtener_cliente(nombre_cliente, fecha_nacimiento.day, fecha_nacimiento.month, fecha_nacimiento.year)

                if cliente != None:
                    vehiculos = cliente.vehiculos
                    # Buscar el vehículo en el easy_parking
                    for vehiculo in vehiculos:
                        print(f"{vehiculos.index(vehiculo)+1}. Marca: {vehiculo.marca}, Placa: {vehiculo.placa}, Modelo: {vehiculo.año_fabricacion} Ubicación: {easy_parking.filas[vehiculo.ubicacion[0]]}{vehiculo.ubicacion[1]+1}")
                    placa_vehiculo = input("Ingrese la placa del vehiculo: ")
                    # Buscar el vehículo por placa
                    vehiculo = None
                    for v in vehiculos:
                        if v.placa == placa_vehiculo:
                            vehiculo = v
                            break
                    if vehiculo is not None:
                        fecha_salida = datetime.now().date()
                        tiempo_salida = datetime.now().strftime("%H:%M")
                        print(easy_parking.retirar_vehiculo(cliente, vehiculo, fecha_salida, tiempo_salida))
                        break
                    else:
                        print("Vehículo no encontrado, verifique la placa")
                        break
                else:
                    print("Cliente no encontrado, verifique los datos")
                    break
            else:
                print("El parqueadero no registra clientes...")
                break

    elif opcion_seleccionada == 3:
        # Calcular tasa de ocupació
        print(easy_parking.calcular_tasa_ocupacion())


    elif opcion_seleccionada == 4:  # NO SIRVE
        # Calcular total de dinero ganado
        print(f"El total acumulado en ganancias es de ${easy_parking.ganancias}")

    elif opcion_seleccionada == 5:
        # Calcular cantidad de vehículos que han ingresado
        print(f'La cantidad de vehiculos que han ingresado: {easy_parking.contador_vehiculos}')

    elif opcion_seleccionada == 6:
        print(f"La cantidad de puestos ocupados actualmente es de {easy_parking.contar_puestos_ocupados()}")

    elif opcion_seleccionada == 7:
        print(easy_parking.calcular_porcentaje_mujeres_y_hombres())

    elif opcion_seleccionada == 8:
        # Calcular porcentaje de vehículos por marca
        print(easy_parking.calcular_porcentaje_marca())
        # easy_parking.calcular_porcentaje_vehiculos_marca()

    elif opcion_seleccionada == 9:
        # Calcular porcentaje de vehículos por año de fabricación
        print(easy_parking.calcular_porcentaje_año_fabricación())

    
    elif opcion_seleccionada == 10:
        listar = easy_parking.listar_clientes_y_vehiculos()

    elif opcion_seleccionada == 11:
        # Salir del programa
        mostrar_menu = False
        print("HASTA LA PROXIMA!!")
        break



    #REVISAR EL RETIRO POR SU PLACA 