# Programa Ejercicio de Herencia v.0.0.1
# Programa que a partir de un archivo introducido en la linea de comandos detecta que tipo de vehiculo se tratara, y
# organiza su informacion en respectivas clases, dependiendo del vehiculo, habran clases que tendran herencia.

# Desarrollado por Cristhian Danilo Viveros Delgado
# Octubre 11  de 2015

# Importar libreria sys para manejo de argumentos de linea de comandos
import sys

#---------------------------------------------------Definicion de funciones-----------------------------------------------------------------#

#Funcion para leer las lineas de un archivo
def leer_lineas_archivo(nombre_archivo):
	lineas = ()
	try:
		archivo = open(nombre_archivo, 'r')
		lineas = archivo.readlines()
		archivo.close()
	except IOError:
		print("Error leyendo archivo " + nombre_archivo + "!")
		
	return lineas 

#Funcion para guardar la informacion de las lineas de un archivo
#Retorna un array de 2 columnas por tantas filas como lineas de archivo
#En la primera columna se almacenara la caracteristica a guardar
#Y En la segunda columna se almacenara el valor de la caracteristica

def guardar_info(linea_a_guardar, numero_linea):
	array_respuesta = [0 for x in range(2)]
	
	arreglo_campos = linea_a_guardar.split("=")
	
	caracteristica_guardar = arreglo_campos[0]
	
	arreglo_caracteristicas = caracteristica_guardar
	
	array_respuesta[0] = caracteristica_guardar
	
	parametro_caracteristica = str(arreglo_campos[1])	
	
	array_respuesta[1] = parametro_caracteristica
	
	return array_respuesta
#-----------------------------------------------------------Fin Definicion De Funciones------------------------------------------------------------------#
#-------------------------------------------------------Definicion de Clases y Clases heredadas----------------------------------------------------------#

class vehiculo(object):
	def __init__(self,modelo,cilindraje,n_ejes):
		self.modelo=modelo
		self.n_ejes=n_ejes
		self.cilindraje=cilindraje
		
		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo son: \nModelo: '+str(self.modelo)+'\nCilindraje del motor: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes) 
	def arrancar(self):
		return 'El Vehiculo '+str(self.modelo)+'arrancara en 15 minutos, por favor abordar el vehiculo.'
	def acelerar(self):
		return 'El Vehiculo '+str(self.modelo)+'debe acelerar con sus '+str(self.cilindraje)+' caballos de fuerza.'
	def apagar(self):
		return 'El Vehiculo '+str(self.modelo)+'ha aterrizado con normalidad, sus ' +str(self.n_ejes)+ ' ejes se han detenido y se encuentra apagado.'
	
		
class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje, n_ejesr, n_alas,n_alerones,):
		vehiculo.__init__(self,modelo,cilindraje,n_ejes)
		self.n_alas=n_alas
		self.n_alerones=n_alerones
	
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo aereo son: \nModelo: ' +str(self.modelo)+ '\nCilindraje: ' +str(self.cilindraje)+ '\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)
	def despegar(self):
		return 'El vehiculo aereo '+str(self.modelo)+'esta poniendo sus ' +str(self.cilindraje)+ ' caballos de fuerza en funcionamiento, por favor no ubicarse en ninguna de sus ' +str(self.n_alas)+ ' alas.'
	def aterrizar(self):
		return 'El vehiculo aereo '+str(self.modelo)+'esta aterrizando, estamos posicionando sus ' +str(self.n_alerones)+ ' alerones para hacer maniobras de aterrizaje.'


class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes):
		vehiculo_aereo.__init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones)
		self.n_cohetes=n_cohetes		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo Espacial son: \nModelo: ' +str(self.modelo)+'\nCilindraje: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)+'\nNumero de cohetes: '+str(self.n_cohetes)
	def despegar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta encendiendo sus motores y poniendo en marcha sus '+str(self.cilindraje)+' caballos de fuerza, por favor no ubicarse en ninguna de sus ' +str(self.n_alas)+ ' alas para evitar inconvenientes, mantengase alejado de los cohetes, los '+str(self.n_cohetes)+ ' estan a punto de encenderse.'
	def planear(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta planeando con sus '+str(self.n_alerones)+' alerones para un viaje seguro.'
	def aterrizar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta por aterrizar en Marte, sus ' +str(self.n_cohetes)+ ' cohetes estan apagandose, por favor cuiden sus pertenencias aun no conocemos las intenciones de los marcianos.'
	

#-------------------------------------------------------------------Fin Definicion De Funciones-------------------------------------------------------------------#



#--------------------------------------------------------------------Inicio Logica Del Programa-------------------------------------------------------------------#

#Introducir archivo en la linea de comandos
archivo_vehiculo = sys.argv[1]

#Variable que almacena las lineas del archivo y su contenido como tal
lineas_archivo_vehiculo = tuple(leer_lineas_archivo(archivo_vehiculo))

#Variable que almacena el numero de lineas de archivo
numero_lineas_vehiculo = len(leer_lineas_archivo(archivo_vehiculo))

# Array que contendran la informacion de las caracteristicas del vehiculo
# Se crea array caracteristicas con dimensiones 2 columnas y tantas filas como caracteristicas o numero de lineas en el archivo de vehiculoX.txt
# caracteristica[indice][0] -> Caracteristica del vehiculo
# caracteristica[indice][1] -> Valor Caracteristica
caracteristicas_vehiculo = [[columnas for columnas in range(2)] for filas in range(numero_lineas_vehiculo)]

# Almacenar informacion de las caracteristicas del vehiculo en array caracteristicas
for x in range (0,numero_lineas_vehiculo):
	linea_guardada = guardar_info(lineas_archivo_vehiculo[x], x+1)
	
	caracteristicas_vehiculo[x][0] = linea_guardada[0]
	caracteristicas_vehiculo[x][1] = linea_guardada[1]


	
#Variable que almacena el tipo de vehiculo

tipo_n = str(caracteristicas_vehiculo[0][1])
tipo = tipo_n.replace("\n","")

#Variables que almacenan informacion que sera heredada
modelo_n = str(caracteristicas_vehiculo[1][1])
modelo = modelo_n.replace('\n', ' ' )

cilindraje = int(caracteristicas_vehiculo[2][1])
n_ejes = int(caracteristicas_vehiculo[3][1])

#Si el tipo de vehiculo es vehiculo
if (tipo == "vehiculo"):
	print "\nEl vehiculo es de tipo: Vehiculo" 
	v1 = vehiculo (modelo,cilindraje,n_ejes)
	print v1.mostrar_detalles()
	print v1.arrancar()
	print v1.acelerar()
	print v1.apagar()

#Si el tipo de vehiculo es aereo, heredara caracteristicas de vehiculo.	
if (tipo == "vehiculo_aereo"):
	print "\nEl vehiculo es de tipo: Aereo" 
	
	n_alas = int(caracteristicas_vehiculo[4][1])
	n_alerones = int(caracteristicas_vehiculo[5][1])
	v1 = vehiculo(modelo,cilindraje,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.n_ejes, n_alas,n_alerones)
	
	print va1.mostrar_detalles()
	print va1.despegar()
	print va1.aterrizar()

#Si el tipo de vehiuclo es espacial, heredara caracteristicas de vehiculo aereo y de vehiculo.
if (tipo == "vehiculo_espacial"):
	print "\nEl vehiculo es de tipo: Espacial"
	
	n_alas = int(caracteristicas_vehiculo[4][1])
	n_alerones = int(caracteristicas_vehiculo[5][1])
	n_cohetes = int(caracteristicas_vehiculo[6][1])

	v1 = vehiculo(modelo,cilindraje,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.n_ejes, n_alas,n_alerones)
	ve1 = vehiculo_espacial(v1.modelo,v1.cilindraje,v1.n_ejes,va1.n_alas,va1.n_alerones,n_cohetes)
	print ve1.mostrar_detalles()
	print ve1.despegar()
	print ve1.planear()
	print ve1.aterrizar()
#-----------------------------------------------------------Fin Logica De Programa---------------------------------------------------------------------#