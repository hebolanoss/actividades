'''
Para correr el codigo por ventana de comandos ingresar la siguiente linea:

	python clases.py vehiculo1.txt vehiculo2.txt vehiculo3.txt vehiculo4.txt
'''




import sys
import os

def leer_lineas_archivo(nombre_archivo):
	lineas = ()
	archivo = open(nombre_archivo, 'r')
	lineas = archivo.readlines()
	archivo.close()
	return lineas 

def validar_linea(linea_por_validar):	
	array_respuesta = [0 for x in range(2)]
	
	# Separar la linea por el simbolo (token) =
	arreglo_campos = linea_por_validar.split("=")
	array_respuesta[0]=arreglo_campos[0]
	array_respuesta[1]=arreglo_campos[1]
	return array_respuesta

def validar_vehiculo(posicion):
	for x in range(0, 3):
		linea_validada = validar_linea(posicion[x+1])
		array_vehiculo[0][x] = linea_validada[0]
		array_vehiculo[1][x] = linea_validada[1]

def validar_vehiculo_2(posicion):
	for x in range(0, 3):
		linea_validada = validar_linea(posicion[x+1])
		array_vehiculo[0][x] = linea_validada[0]
		array_vehiculo[2][x] = linea_validada[1]


def validar_aereo(posicion):
	for x in range(0, 5):
		linea_validada = validar_linea(posicion[x+1])
		array_vehiculo[0][x] = linea_validada[0]
		array_vehiculo[3][x] = linea_validada[1]


def validar_espacial(posicion):
	for x in range(0, 6):
		linea_validada = validar_linea(posicion[x+1])
		array_vehiculo[0][x] = linea_validada[0]
		array_vehiculo[4][x] = linea_validada[1]



class vehiculo(object):
	def __init__(self,modelo,cilindraje,n_ejes):
		self.modelo = modelo
		self.cilindraje = cilindraje
		self.n_ejes = n_ejes
	def det_vehiculo(self):
		return '\n\t\tModelo: '+str(self.modelo)+'\n\t\tCilindraje: '+str(self.cilindraje)+'\n\t\tNumero de ejes: '+str(self.n_ejes)


class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones):
		vehiculo.__init__(self,modelo,cilindraje,n_ejes)
		self.n_alas = n_alas
		self.n_alerones = n_alerones
	def det_aereo(self):
		return '\n\t\tNumero de alas: '+str(self.n_alas)+'\n\t\tNumero de alerones: '+str(self.n_alerones)

class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes):
		vehiculo_aereo.__init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones)
		self.n_cohetes = n_cohetes
	def det_espacial(self):
		return '\n\t\tNumero de cohetes: '+str(self.n_cohetes)


array_lista = [[columnas for columnas in range(1)]for filas in range(4)]

for x in range(0,4):
	array_lista[x] = sys.argv[x+1]


array_array = [[columnas for columnas in range(7)] for filas in range(4)]
for x in range(0,4):
	array_array[x]=tuple(leer_lineas_archivo(array_lista[x]))

print array_array


array_vehiculo = [[columnas for columnas in range(6)] for filas in range(5)]
array_v = [0 for x in range(2)]


array_v[1]=validar_linea(array_array[0][0])
if(int(len(array_v[1][1]))==9):
	validar_vehiculo(array_array[0])

array_v[1]=validar_linea(array_array[1][0])
if(int(len(array_v[1][1]))==9):
	validar_vehiculo_2(array_array[1])

array_v[1]=validar_linea(array_array[2][0])
if(int(len(array_v[1][1]))==15):
	validar_aereo(array_array[2])

array_v[1]=validar_linea(array_array[3][0])
if(int(len(array_v[1][1]))==18):
	validar_espacial(array_array[3])

print array_vehiculo

modelo = array_vehiculo[1][0]
cilindraje = array_vehiculo[1][1]
n_ejes = array_vehiculo[1][2]
v1 = vehiculo(modelo, cilindraje,n_ejes)
print '\n\tVehiculo\n'+v1.det_vehiculo()

modelo = array_vehiculo[2][0]
cilindraje = array_vehiculo[2][1]
n_ejes = array_vehiculo[2][2]
v2 = vehiculo(modelo, cilindraje,n_ejes)
print '\n\tVehiculo\n'+v2.det_vehiculo()

modelo = array_vehiculo[3][0]
cilindraje = array_vehiculo[3][1]
n_ejes = array_vehiculo[3][2]
n_alas = array_vehiculo[3][3]
n_alerones = array_vehiculo[3][4]
v3 = vehiculo_aereo(modelo,cilindraje,n_ejes,n_alas,n_alerones)
print '\n\tVehiculo aereo\n'+v3.det_vehiculo() 
print v3.det_aereo()

modelo = array_vehiculo[4][0]
cilindraje = array_vehiculo[4][1]
n_ejes = array_vehiculo[4][2]
n_alas = array_vehiculo[4][3]
n_alerones = array_vehiculo[4][4]
n_cohetes = array_vehiculo[4][5]
v4 = vehiculo_espacial(modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes)
print '\n\tVehiculo espacial\n'+v4.det_vehiculo() 
print v4.det_aereo()
print v4.det_espacial()





















