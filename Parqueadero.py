import numpy as np
from datetime import datetime

class Parqueadero:

    def __init__(self, tamaño):

        self.tamaño = tamaño
        self.filas = self.obtener_nombres_filas() #letras de las filas
        self.matriz = self.modificar_matriz() #matriz de valores buleanos
        self.precios = self.asignar_precios() #capas de precios
        self.lista_precios = self.definir_precios()
        self.contadores = np.zeros((self.tamaño, self.tamaño), dtype=int)
        self.clientes = []
        self.contador_vehiculos = 0
        self.ganancias = 0
        
        

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def retirar_cliente(self, cliente):
        self.clientes.pop(self.clientes.index(cliente)) #index es el inidce

    def obtener_nombres_filas(self):
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return letras[:self.tamaño] #los : sirven para especificar el rango de elementos que desamos obtener

    def modificar_matriz(self):
        matriz = np.full((self.tamaño, self.tamaño), False, dtype=bool)
        capas = (self.tamaño + 1) // 2

        for capa in range(capas):
            matriz[capa:self.tamaño - capa, capa:self.tamaño - capa] = False #Por ejemplo, si self.tamaño es 6 y capa es 2, entonces el slicing capa:self.tamaño - capa se convertirá en 2:6-2, que es equivalente a 2:4. Esto seleccionará los elementos desde el índice 2 (inclusive) hasta el índice 4 (exclusivo) en esa dimensión.

        return matriz

    def asignar_precios(self): #capas de precios
        precios = np.zeros((self.tamaño, self.tamaño), dtype=int)
        capas = (self.tamaño + 1) // 2
        for capa in range(capas):
            precio_capa = (self.tamaño * 1000) * (capas - capa)
            precios[capa:self.tamaño - capa, capa:self.tamaño - capa] = precio_capa
        return precios
    
    def definir_precios(self):
        if self.tamaño == 10:
            return [10000, 20000, 30000, 40000, 50000]
        elif self.tamaño == 8:
            return [8000, 16000, 24000, 32000]
        else:
            return [6000, 12000, 18000]
    
    def calcular_porcentaje_mujeres_y_hombres(self):
        mujeres = 0
        hombres = 0
        total = 0
        for cliente in self.clientes:
            if cliente.sexo == 'F':
                mujeres +=1
            else:
                hombres +=1
        
            total +=1
        return f"Hombres: {(hombres/total)*100}%, Mujeres: {(mujeres/total)*100}%"
    
    def obtener_indice_fila(self, fila):
        if isinstance(fila, str): #Se recibe un parámetro fila, que puede ser de tipo str o int.
            fila = fila.upper()
            if fila in self.filas:
                return self.filas.index(fila) #Esto proporciona el índice correspondiente a la posición de la fila en la lista self.filas.
            else:
                return None
        elif isinstance(fila, int):
            if fila >= 0 and fila < self.tamaño:
                return fila
            else:
                return None
        else:
            return None

    def contar_puestos_ocupados(self):
        matriz = self.matriz
        filas = len(matriz) #numero de filas, también se pudo utilizar self.tamaño
        columnas = len(matriz[0]) #0 es el indice de la primera fila en la matriz
        puestos_ocupados = 0

        for fila in range(filas):
            for columna in range(columnas):
                if matriz[fila][columna] == True:
                    puestos_ocupados += 1

        return puestos_ocupados


    def obtener_contador(self, fila, columna):
        indice_fila = self.obtener_indice_fila(fila) #fila se le pasa como algumento a obtener_contador y es un parametro del metodo en que estamos

        if indice_fila is None or columna < 0 or columna >= self.tamaño:
            return ("Posición inválida.")
        else:
            contador = self.contadores[indice_fila, columna]
            return (f"El espacio ({fila}, {columna}) ha sido utilizado {contador} veces.")

    def calcular_tasa_ocupacion(self):
        espacios_ocupados = np.count_nonzero(self.matriz)
        espacios_totales = self.tamaño * self.tamaño
        tasa_ocupacion = (espacios_ocupados * 100) / espacios_totales
        return (f"Tasa de ocupación: {tasa_ocupacion}%")


    def buscar_vehiculo(self, propietario):
        for cliente in self.clientes:
            for vehiculo in cliente.vehiculos:
                if vehiculo.propietario == propietario:
                    return vehiculo
        return None
    
    def listar_clientes_y_vehiculos(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("--------------------------------------------------------------------")
            print("LISTADO DE VEHICULOS\n")
            for cliente in self.clientes:
                print(f"Cliente: {cliente.nombre}, Sexo: {cliente.sexo}, Edad: {cliente.Calcular_edad()} años")
                if not cliente.vehiculos:
                    print("  No tiene vehículos registrados.")
                else:
                    for index, vehiculo in enumerate(cliente.vehiculos):
                        print(f"  Vehículo {index + 1}:")
                        print(f"    Marca: {vehiculo.marca}")
                        print(f"    Año de Fabricación: {vehiculo.año_fabricacion}")
                        print(f"    Ubicación: {vehiculo.ubicacion}")
                        print(f"  Placa: {vehiculo.placa}\n")
            print("--------------------------------------------------------------------")

    def retirar_vehiculo(self, cliente, vehiculo, fecha_salida, hora_salida):
        # Convertir la fecha y hora de salida proporcionadas a objetos de fecha y hora
        hora_salida = datetime.strptime(hora_salida, "%H:%M").time()
        # Registrar la fecha y hora de salida en el vehículo
        # Calcular el tiempo de permanencia del vehículo
        tiempo_permanencia = vehiculo.calcular_tiempo_permanencia(fecha_salida, hora_salida)
        if tiempo_permanencia > 0:
            # Calcular el monto a cobrar
            monto_cobro = tiempo_permanencia * vehiculo.tarifa_aplicada
            self.ganancias += monto_cobro  # Agregar el monto calculado al total
            # Eliminar el vehículo del cliente
            cliente.eliminar_vehiculo(vehiculo)
            self.matriz[vehiculo.ubicacion[0]][vehiculo.ubicacion[1]] = False
            if len(cliente.vehiculos) == 0:
                self.retirar_cliente(cliente)
            # Imprimir factura
            return ('\n'f'vehiculo: {vehiculo.marca} placa:{vehiculo.placa} {vehiculo.año_fabricacion}, fecha_salida: {fecha_salida}, '
                    f'hora_salida: {hora_salida}, monto_cobro: {monto_cobro}')
        else:
            return ("No se pudo calcular el tiempo de permanencia. Verifica la información de salida.")


    
    def calcular_porcentaje_año_fabricación(self):
        modelos = []
        cantidades = []
        total = 0
        
        for cliente in self.clientes:
            for vehiculo in cliente.vehiculos:
                modelo = str(vehiculo.año_fabricacion)
                
                if modelo in modelos:
                    index = modelos.index(modelo)
                    cantidades[index] += 1
                else:
                    modelos.append(modelo)
                    cantidades.append(1)
                
                total += 1
        
        porcentajes = []
        
        for cantidad in cantidades:
            porcentaje = (cantidad / total) * 100
            porcentajes.append(porcentaje)
        
        return dict(zip(modelos, porcentajes))

    def calcular_porcentaje_marca(self):
        marca = []
        cantidades = []
        total = 0
        
        for cliente in self.clientes:
            for vehiculo in cliente.vehiculos:
                modelo = str(vehiculo.marca)
                
                if modelo in marca:
                    index = marca.index(modelo)
                    
                    cantidades[index] += 1
                else:
                    marca.append(modelo)
                    cantidades.append(1)
                
                total += 1
        
        porcentajes = []
        
        for cantidad in cantidades:
            porcentaje = (cantidad / total) * 100
            porcentajes.append(porcentaje)
        
        return dict(zip(marca, porcentajes))
    
    def obtener_cliente(self, nombre, dia_nacimiento, mes_nacimiento, año_nacimiento):
        for cliente in self.clientes:
            if [cliente.nombre, cliente.dia_nacimiento, cliente.mes_nacimiento, cliente.año_nacimiento] == [nombre, dia_nacimiento, mes_nacimiento, año_nacimiento]:
                return cliente
        return None