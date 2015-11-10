# Programa Ejercicio de Herencia v.0.0.1
#Programa desarollado por Julian Andres  Duarte Castañeda

# Importar libreria sys para manejo de argumentos de linea de comandos
import sys 



#---------------------------------------------------Definicion de las clases de vehiculos -----------------------------------------------------------------#

class vehiculo(object):
	def __init__(self,modelo,cilindraje,n_ejes):
		self.modelo=modelo
		self.n_ejes=n_ejes
		self.cilindraje=cilindraje
		
		
  
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo son las siguientes: \n\nModelo: '+str(self.modelo)+'\nCilindraje del motor: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes) 
	def arrancar(self):
		return 'El Vehiculo '+str(self.modelo)+'arrancara en contados minutos, verificar que sus puertas se enceuntren cerradas corectamente.'
	def acelerar(self):
		return 'El Vehiculo '+str(self.modelo)+'debe acelerar, por su seguridad abroche su cinturon de seguridad'
	def apagar(self):
		return 'El Vehiculo '+str(self.modelo)+'se a detenido por completo ,  sus puetas puenden ser abiertas sin peligro alguno.'
	
	
	
class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje, n_ejesr, n_alas,n_alerones,):
		vehiculo.__init__(self,modelo,cilindraje,n_ejes)
		self.n_alas=n_alas
		self.n_alerones=n_alerones
		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo aereo son las siguinetes : \n\nModelo: ' +str(self.modelo)+ '\nCilindraje: ' +str(self.cilindraje)+ '\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)
	def despegar(self):
		return 'El vehiculo aereo '+str(self.modelo)+'esta poniendo sus  turbinas en funcionamiento, por favor no ubicarse cerca para evitar accidentes, el que se quedo se quedo.'
	def aterrizar(self):
		return 'El vehiculo aereo '+str(self.modelo)+'esta a punto de aterrizar, por favor apagar aparatos electronicos que puedan interferir con la rutina de aterrizaje .'


class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes):
		vehiculo_aereo.__init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones)
		self.n_cohetes=n_cohetes		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo Espacial son las siguientes : \n\nModelo: ' +str(self.modelo)+'\nCilindraje: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)+'\nNumero de cohetes: '+str(self.n_cohetes)
	def despegar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta en la plataforma de salida se le recomienda a la tripulacion tomar sus puestos correspondiente, y alistarce para su despege'
	def planear(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta planeando gracias a sus sistemas de vuelo programado y seguro, disfrute de su vieje comodo y seguro.'
	def aterrizar(self):
		return 'El vehiculo espacial ' +str(self.modelo)+ 'esta por aterrizar, recuerde no salir del vehiculo antes de que los sistemas de seguridad del vehiculo determinen si el aire es apto para su salud.'
	
#---------------------------------------------------Fin de la definicion de las clases -----------------------------------------------------------------#


#---------------------------------------------------Definicion de funciones-----------------------------------------------------------------#
#Funcion 1 
#funcion para leer las lineas que se encuentran en un archivo determinado

def leer_num_lineas_archivo(nombre_archivo):
	lineas = ()
	try:
		archivo = open(nombre_archivo, 'r')
		lineas = archivo.readlines()
		archivo.close()
	except IOError:
		print("Error leyendo archivo " + nombre_archivo + "!")
		
	return lineas 
#Funcion 2
'''
-Funcion que guarda la informacion leida en las lineas en arreglos para su previo manejo.
-Dicha funcion retorta un arreglo de dos culumas y igual filas como numero de lineas  se encontraron en el archivo leido
-En la primera  columna se gaurda la caracteristica del vehiculo.
-En la segunda columna se guarda el veh_aeroor de la caracteristica definida del vehiculo.
'''
def guardar_info(linea_a_guardar, numero_linea):
	array_respuesta = [0 for x in range(2)]
	
	arreglo_campos = linea_a_guardar.split("=")
	
	caracteristica_guardar = arreglo_campos[0]
	
	arreglo_caracteristicas = caracteristica_guardar
	
	array_respuesta[0] = caracteristica_guardar
	
	parametro_caracteristica = str(arreglo_campos[1])	
	
	array_respuesta[1] = parametro_caracteristica
	
	return array_respuesta


#---------------------------------------------------Fin de definicion de funciones-----------------------------------------------------------------#
#---------------------------------------------------Inicio logica del programa -----------------------------------------------------------------#

#introducir el archivo en la linea de comandos 
archivo_vehiculo = sys.argv[1]

#variable para almacenas las lineas del archivo y el cantenido del mismo
lineas_archivo_vehiculo = tuple(leer_num_lineas_archivo(archivo_vehiculo))

#variable que  almacena el numero de lineas del archivo 
numero_lineas_vehiculo = len(leer_num_lineas_archivo(archivo_vehiculo))

# Array que contendran la informacion de las caracteristicas del vehiculo
caracteristicas_vehiculo = [[columnas for columnas in range(2)] for filas in range(numero_lineas_vehiculo)]



# Array que contendra la informacion de las caracteristicas del vehiculo
for x in range (0,numero_lineas_vehiculo):
	linea_guardada = guardar_info(lineas_archivo_vehiculo[x], x+1)
	
	caracteristicas_vehiculo[x][0] = linea_guardada[0]
	caracteristicas_vehiculo[x][1] = linea_guardada[1]
	
tipo_n = str(caracteristicas_vehiculo[0][1])
tipo = tipo_n.replace("\n","")
	
#Variables que almacenan informacion que sera heredada
modelo_n = str(caracteristicas_vehiculo[1][1])
modelo = modelo_n.replace('\n', ' ' )

cilindraje = int(caracteristicas_vehiculo[2][1])
n_ejes = int(caracteristicas_vehiculo[3][1])
	
#Si el tipo de vehiculo es vehiculo
if (tipo == "vehiculo"):
	print "\n---------El vehiculo es de tipo: Vehiculo---------\n" 
	v1 = vehiculo (modelo,cilindraje,n_ejes)
	print v1.mostrar_detalles() + "\n"
	print v1.arrancar() + "\n"
	print v1.acelerar() + "\n"
	print v1.apagar()
	
#Si el tipo de vehiculo es aereo, heredara caracteristicas de vehiculo.	
if (tipo == "vehiculo_aereo"):
	print "\n-------El vehiculo es de tipo: Aereo---------\n" 
	
	n_alas = int(caracteristicas_vehiculo[4][1])
	n_alerones = int(caracteristicas_vehiculo[5][1])
	v1 = vehiculo(modelo,cilindraje,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.n_ejes, n_alas,n_alerones)
	
	print va1.mostrar_detalles() + '\n'
	print va1.despegar() + '\n'
	print va1.aterrizar() + '\n'


#Si el tipo de vehiuclo es espacial, heredara caracteristicas de vehiculo aereo y de vehiculo.
if (tipo == "vehiculo_espacial"):
	print "\n---------El vehiculo es de tipo: Espacial---------\n"
	
	n_alas = int(caracteristicas_vehiculo[4][1])
	n_alerones = int(caracteristicas_vehiculo[5][1])
	n_cohetes = int(caracteristicas_vehiculo[6][1])

	v1 = vehiculo(modelo,cilindraje,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.n_ejes, n_alas,n_alerones)
	ve1 = vehiculo_espacial(v1.modelo,v1.cilindraje,v1.n_ejes,va1.n_alas,va1.n_alerones,n_cohetes)
	print ve1.mostrar_detalles() + '\n'
	print ve1.despegar() + '\n'
	print ve1.planear()  + '\n'
	print ve1.aterrizar() 
#---------------------------------------------------Fin logica del programa-----------------------------------------------------------------#

		
