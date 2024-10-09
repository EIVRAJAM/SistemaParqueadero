from Parqueadero import Parqueadero
from Cliente import Cliente
from Vehiculo import Vehiculo
from datetime import datetime

parqueadero_prueba_1 = Parqueadero(10)

cliente_1 = Cliente('Abraham Ceballos', 'M', 14, 1, 2005)
vehiculo_cliente_1 = Vehiculo('Tesla', 'ASD123', 2023, 30000, datetime.strptime('30/05/2023', "%d/%m/%Y").date(), datetime.strptime('10:00', "%H:%M").time(), [2,2])
cliente_1.agregar_vehiculo(vehiculo_cliente_1)
parqueadero_prueba_1.registrar_cliente(cliente_1)
parqueadero_prueba_1.contador_vehiculos +=1
parqueadero_prueba_1.matriz[2][2] = True
print(f"Carro registrado con éxito. Precio: {3000}")
print(f"Carro ubicado en la posición: ({parqueadero_prueba_1.filas[2]}{2 + 1})")
print()
print("--------------------------------------------------------")
print()
cliente_2 = Cliente('Juan Hurtado', 'M', 10, 12, 2003)
vehiculo_cliente_2 = Vehiculo('Camaro','KHL153', 2023, 50000, datetime.strptime('30/05/2023', "%d/%m/%Y").date(), datetime.strptime('8:00', "%H:%M").time(), [0,0])
cliente_2.agregar_vehiculo(vehiculo_cliente_2)
parqueadero_prueba_1.registrar_cliente(cliente_2)
parqueadero_prueba_1.contador_vehiculos +=1
parqueadero_prueba_1.matriz[0][0] = True
print(f"Carro registrado con éxito. Precio: {5000}")
print(f"Carro ubicado en la posición: ({parqueadero_prueba_1.filas[0]}{0 + 1})")
print()
print("--------------------------------------------------------")
print()
cliente_3 = Cliente('Sofía Marquez', 'F', 5, 8, 2002)
vehiculo_cliente_3 = Vehiculo('Chevrolet', 'WAD759',2019, 50000, datetime.strptime('30/05/2023', "%d/%m/%Y").date(), datetime.strptime('11:00', "%H:%M").time(), [0,1])
cliente_3.agregar_vehiculo(vehiculo_cliente_3)
parqueadero_prueba_1.registrar_cliente(cliente_3)
parqueadero_prueba_1.contador_vehiculos +=1
parqueadero_prueba_1.matriz[0][1] = True
print(f"Carro registrado con éxito. Precio: {5000}")
print(f"Carro ubicado en la posición: ({parqueadero_prueba_1.filas[0]}{1 + 1})")
print()

print("---------------------------------------------------------")
print("-----------------------INFORMACIÓN-----------------------")
print(parqueadero_prueba_1.calcular_tasa_ocupacion())
print(f"El total acumulado en ganancias es de ${parqueadero_prueba_1.ganancias}")
print(f'La cantidad de vehiculos que han ingresado: {parqueadero_prueba_1.contador_vehiculos}')
print(f"La cantidad de puestos ocupados actualmente es de {parqueadero_prueba_1.contar_puestos_ocupados()}")
print("Calcular porcentaje de mujeres y hombres")
print(parqueadero_prueba_1.calcular_porcentaje_mujeres_y_hombres())
print("Calcular porcentaje de vehículos por marca")
print(parqueadero_prueba_1.calcular_porcentaje_marca())
print("Calcular porcentaje de vehículos por año de fabricación")
print(parqueadero_prueba_1.calcular_porcentaje_año_fabricación())
print()

print("--------------------------RETIRO-------------------------")
print(parqueadero_prueba_1.retirar_vehiculo(cliente_1, vehiculo_cliente_1, datetime.strptime('30/05/2023', "%d/%m/%Y").date(), '11:00'))
print()

print("--------------------------RETIRO-------------------------")
print(parqueadero_prueba_1.retirar_vehiculo(cliente_2, vehiculo_cliente_2, datetime.strptime('30/05/2023', "%d/%m/%Y").date(), '10:00'))
print()

print("---------------------------------------------------------")
print("-----------------------INFORMACIÓN-----------------------")

print(parqueadero_prueba_1.calcular_tasa_ocupacion())
print(f"El total acumulado en ganancias es de ${parqueadero_prueba_1.ganancias}")
print(f'La cantidad de vehiculos que han ingresado: {parqueadero_prueba_1.contador_vehiculos}')
print(f"La cantidad de puestos ocupados actualmente es de {parqueadero_prueba_1.contar_puestos_ocupados()}")
print("Calcular porcentaje de mujeres y hombres")
print(parqueadero_prueba_1.calcular_porcentaje_mujeres_y_hombres())
print("Calcular porcentaje de vehículos por marca")
print(parqueadero_prueba_1.calcular_porcentaje_marca())
print("Calcular porcentaje de vehículos por año de fabricación")
print(parqueadero_prueba_1.calcular_porcentaje_año_fabricación())