from datetime import datetime
from Parqueadero import *

class Vehiculo:
    def __init__(self, marca, placa, año_fabricacion, tarifa, fecha_ingreso, hora_ingreso, ubicacion):
        self.marca = marca
        self.placa= placa
        self.año_fabricacion = año_fabricacion
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.ubicacion = ubicacion
        self.tarifa_aplicada = tarifa

    def calcular_tiempo_permanencia(self, fecha_salida, hora_salida):
        if fecha_salida is not None and hora_salida is not None:
            fecha_ingreso_completa = datetime.combine(self.fecha_ingreso, self.hora_ingreso)
            fecha_salida_completa = datetime.combine(fecha_salida, hora_salida)

            tiempo_permanencia = fecha_salida_completa - fecha_ingreso_completa
            return tiempo_permanencia.total_seconds() / 3600
        else:
            return 0