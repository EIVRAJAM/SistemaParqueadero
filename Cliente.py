from datetime import datetime
from Vehiculo import Vehiculo


class Cliente:

    def __init__(self, nombre, sexo, dia_nacimiento, mes_nacimiento, año_nacimiento):
        self.nombre = nombre
        self.sexo = sexo
        self.dia_nacimiento = dia_nacimiento
        self.mes_nacimiento = mes_nacimiento
        self.año_nacimiento = año_nacimiento
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)

    def Calcular_edad(self):
        edad = None
        restar = 0
        dt = datetime.now()
        diferencia_de_años = dt.year - self.año_nacimiento
        diferencia_de_meses = dt.month - self.mes_nacimiento
        diferencia_de_dias = dt.day - self.dia_nacimiento
        if diferencia_de_meses < 0 or (diferencia_de_meses == 0 and diferencia_de_dias < 0):
            restar = 1
        edad = diferencia_de_años - restar
        return edad

    def verificar_mayor_edad(self):
        edad = self.Calcular_edad()
        if edad >= 18:
            return True
        return False

    def eliminar_vehiculo(self, vehiculo_param):
        for vehiculo in self.vehiculos:
            if [vehiculo.marca, vehiculo.placa, vehiculo.año_fabricacion, vehiculo.ubicacion] == [vehiculo_param.marca, vehiculo.placa, vehiculo_param.año_fabricacion, vehiculo_param.ubicacion]:
                self.vehiculos.pop(self.vehiculos.index(vehiculo))