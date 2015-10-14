# Desarrollado por Daniela Mendieta Osorio 
# Octubre 13  de 2015

# Importar libreria sys para manejo de argumentos de linea de comandos
import sys

#Definicion de funciones 

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

	#Clases 

class vehiculo(object):
	def __init__(self,modelo,cilindraje,n_ejes):
		self.modelo=modelo
		self.n_ejes=n_ejes
		self.cilindraje=cilindraje
		
		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo son: \nModelo: '+str(self.modelo)+'\nCilindraje del motor: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes) 


class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje, n_ejesr, n_alas,n_alerones,):
		vehiculo.__init__(self,modelo,cilindraje,n_ejes)
		self.n_alas=n_alas
		self.n_alerones=n_alerones
	
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo aereo son: \nModelo: ' +str(self.modelo)+ '\nCilindraje: ' +str(self.cilindraje)+ '\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)
	
class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes):
		vehiculo_aereo.__init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones)
		self.n_cohetes=n_cohetes		
	def mostrar_detalles(self):
		return 'Las caracteristicas del vehiculo Espacial son: \nModelo: ' +str(self.modelo)+'\nCilindraje: '+str(self.cilindraje)+'\nNumero de ejes: '+str(self.n_ejes)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)+'\nNumero de cohetes: '+str(self.n_cohetes)
	
#Introducir archivo
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
n_ejes = int(caracteristicas_vehiculo[3][1])

if (tipo == "vehiculo"):
	print "\nEl vehiculo es de tipo: Vehiculo" 
	v1 = vehiculo (modelo,cilindraje,n_ejes)
	print v1.mostrar_detalles()
	print v1.arrancar()
	print v1.acelerar()
	print v1.apagar()
	
if (tipo == "vehiculo_aereo"):
	print "\nEl vehiculo es de tipo: Aereo" 
	
	n_alas = int(caracteristicas_vehiculo[4][1])
	n_alerones = int(caracteristicas_vehiculo[5][1])
	v1 = vehiculo(modelo,cilindraje,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cilindraje,v1.n_ejes, n_alas,n_alerones)
	
	print va1.mostrar_detalles()
	print va1.despegar()
	print va1.aterrizar()

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
 