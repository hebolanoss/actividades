# Programa Semana 10 - Utilizacion de clases y herencia
# Harold Esteban Bolaños Serna
# Octubre 13  de 2015

# Importar libreria sys para manejo de argumentos de linea de comandos
import sys

#--------------------funciones------------------------------------------


def leer_lineas_archivo(nombre_archivo):
	lineas = ()
	try:
		archivo = open(nombre_archivo, 'r')
		lineas = archivo.readlines()
		archivo.close()
	except IOError:
		print("Error leyendo archivo " + nombre_archivo + "!")
		
	return lineas 

def guardar_info(linea_a_guardar, numero_linea):
	array_respuesta = [0 for x in range(2)]
	
	arreglo_campos = linea_a_guardar.split("=")
	
	caracteristica_guardar = arreglo_campos[0]
	
	arreglo_caracteristicas = caracteristica_guardar
	
	array_respuesta[0] = caracteristica_guardar
	
	parametro_caracteristica = str(arreglo_campos[1])	
	
	array_respuesta[1] = parametro_caracteristica
	
	return array_respuesta

#------------------------------Clases y herencias.------------------------------------

class vehiculo():
	def __init__(self,modelo,cilindraje,numero_de_ejes):
		self.modelo=modelo
		self.numero_de_ejes=numero_de_ejes
		self.cilindraje=cilindraje
		
		
	def mostrar_detalles(self):
		return 'Las caracteristicas que tiene el vehiculo son: \n\nModelo: '+str(self.modelo)+'\nCilindraje del motor: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.numero_de_ejes) 
	def arrancar(self):
		return 'El Vehiculo '+str(self.modelo)+' esta arrancando.'
	def acelerar(self):
		return 'El Vehiculo '+str(self.modelo)+' esta puesto en marcha.'
	def apagar(self):
		return 'El Vehiculo '+str(self.modelo)+' se ha apagado.'
	
		
class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje, numero_de_ejes, numero_de_alas,numero_de_alerones,):
		vehiculo.__init__(self,modelo,cilindraje,numero_de_ejes)
		self.numero_de_alas=numero_de_alas
		self.numero_de_alerones=numero_de_alerones
	
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo aereo son: \n\nModelo: ' +str(self.modelo)+ '\nCilindraje: ' +str(self.cilindraje)+ '\nNumero de ejes: '+str(self.numero_de_ejes)+'\nNumero de alas: '+str(self.numero_de_alas)+'\nNumero de alerones: '+str(self.numero_de_alerones)
	def despegar(self):
		return 'El vehiculo aereo '+str(self.modelo)+' esta preparandose para el despegue.'
	def aterrizar(self):
		return 'El vehiculo aereo '+str(self.modelo)+' aterrizo exitosamente.'


class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,cilindraje,numero_de_ejes,numero_de_alas,numero_de_alerones,numero_de_cohetes):
		vehiculo_aereo.__init__(self,modelo,cilindraje,numero_de_ejes,numero_de_alas,numero_de_alerones)
		self.numero_de_cohetes=numero_de_cohetes		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo Espacial son: \n\nModelo: ' +str(self.modelo)+'\nCilindraje: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.numero_de_ejes)+'\nNumero de alas: '+str(self.numero_de_alas)+'\nNumero de alerones: '+str(self.numero_de_alerones)+'\nNumero de cohetes: '+str(self.numero_de_cohetes)
	def despegar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ ' acaba de despegar hacia el espacio.'
	def planear(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ ' esta en modo: Piloto Automatico.'
	def aterrizar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ ' aterrizo en la superficie.'
	

#----------------------------------Fin Definicion De Clases y herencia---------------



#-----------------------------Inicio Logica Del Programa-------------------------------


archivo_vehiculo = sys.argv[1]

lineas_archivo_vehiculo = tuple(leer_lineas_archivo(archivo_vehiculo))

numero_lineas_vehiculo = len(leer_lineas_archivo(archivo_vehiculo))

caracteristicas_vehiculo = [[columnas for columnas in range(2)] for filas in range(numero_lineas_vehiculo)]

for x in range (0,numero_lineas_vehiculo):
	linea_guardada = guardar_info(lineas_archivo_vehiculo[x], x+1)
	
	caracteristicas_vehiculo[x][0] = linea_guardada[0]
	caracteristicas_vehiculo[x][1] = linea_guardada[1]

tipo_n = str(caracteristicas_vehiculo[0][1])
tipo = tipo_n.replace("\n","")

modelo_n = str(caracteristicas_vehiculo[1][1])
modelo = modelo_n.replace('\n', ' ' )

cilindraje = int(caracteristicas_vehiculo[2][1])
numero_de_ejes = int(caracteristicas_vehiculo[3][1])


if (tipo == "vehiculo"):
	print "\n---------El vehiculo escogido es de tipo: Vehiculo(terrestre)---------\n" 
	v1 = vehiculo (modelo,cilindraje,numero_de_ejes)
	print v1.mostrar_detalles() + "\n"
	print v1.arrancar() + "\n"
	print v1.acelerar() + "\n"
	print v1.apagar()

if (tipo == "vehiculo_aereo"):
	print "\n-------El vehiculo escogido es de tipo: Vehiculo Aereo---------\n" 
	
	numero_de_alas = int(caracteristicas_vehiculo[4][1])
	numero_de_alerones = int(caracteristicas_vehiculo[5][1])
	v1 = vehiculo(modelo,cilindraje,numero_de_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.numero_de_ejes, numero_de_alas,numero_de_alerones)
	
	print va1.mostrar_detalles() + '\n'
	print va1.despegar() + '\n'
	print va1.aterrizar() + '\n'


if (tipo == "vehiculo_espacial"):
	print "\n---------El vehiculo escogido es de tipo: Vehiculo Espacial---------\n"
	
	numero_de_alas = int(caracteristicas_vehiculo[4][1])
	numero_de_alerones = int(caracteristicas_vehiculo[5][1])
	numero_de_cohetes = int(caracteristicas_vehiculo[6][1])

	v1 = vehiculo(modelo,cilindraje,numero_de_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.numero_de_ejes, numero_de_alas,numero_de_alerones)
	ve1 = vehiculo_espacial(v1.modelo,v1.cilindraje,v1.numero_de_ejes,va1.numero_de_alas,va1.numero_de_alerones,numero_de_cohetes)
	print ve1.mostrar_detalles() + '\n'
	print ve1.despegar() + '\n'
	print ve1.planear() + '\n'
	print ve1.aterrizar() 

#---------------------Fin De Programa-----------------------------