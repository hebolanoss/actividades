# Ejercicio Herencia

# Desarrollado por Esteban Norena Arroyave
# Octubre 10 de 2015

# Importar libreria sys para el manejo de los argumentos de la consola
import sys
# Importar libreria os para acceder a funcionalidades dependientes del Sistema Operativo
import os

# ------------------ Inicio de definicion de constantes y parametros ------------------ #

# Nombre archivo de errores
nombre_archivo_errores = "errores.txt"

# Nombre archivo de registro de operacion del programa
nombre_archivo_registro = "log.txt"


# ------------------ Fin de definicion de constantes y parametros ------------------ #

# ------------------ Inicio de definicion de funciones empleadas ------------------ #

# Funcion que crea un nuevo archivo .txt
def crear_archivo(nombre_archivo):
	try:
		archivo = open(nombre_archivo, 'w')
		archivo.close()
	except:
		guardar_error("Error creando archivo " + nombre_archivo + "!");
		return False
		
	return True

# Funcion que lee las lineas de un archivo de texto y las devuelve en una lista.
def leer_lineas_archivo(nombre_archivo):
	lineas = ()
	try:
		archivo = open(nombre_archivo, 'r')
		lineas = archivo.readlines()
		archivo.close()
	except IOError:
		guardar_error("Error leyendo archivo " + nombre_archivo + "!")
		
	return lineas 

# Funcion que guarda al final del archivo definido la linea especificada. Devuelve True si fue exitoso o False en caso de error.
def escribir_linea_archivo(nombre_archivo, linea_a_escribir):	
	try:
		archivo = open(nombre_archivo, 'a')
		archivo.write(linea_a_escribir)
		archivo.close()
	except IOError:
		guardar_error("Error escribiendo linea " + linea_a_escribir + " en archivo " + nombre_archivo + "!")
		return False
		
	return True


# Funcion que guarda un mensaje de error en el archivo errores.txt
def guardar_error(mensaje_error):
	escribir_linea_archivo(nombre_archivo_errores, "\n" + mensaje_error + "\n")

# Funcion que guarda un registro de operacion en el archivo log.txt
def guardar_log(mensaje_registro):
	escribir_linea_archivo(nombre_archivo_registro, "\n" + mensaje_registro + "\n")

# Funcion que finaliza el programa y guarda el respectivo mensaje de terminacion en el archivo errores.txt
def terminar_programa(mensaje_terminacion):
	guardar_error(mensaje_terminacion)
	guardar_log("Programa terminado por error... Verificar archivo errores.txt para mas detalles.")
	
	# Terminar el programa
	sys.exit()

# Funcion que valida la existencia, nombre y extension de un archivo.
def validar_archivo(nombre_archivo):
	archivo_valido = True
	
	# El archivo.txt debe existir.
	if(os.path.isfile(nombre_archivo) == False):
		print "No existe archivo " + nombre_archivo
		guardar_error("Archivo suministrado no existe.")

	# Validar que el nombre no tenga espacios.
	cantidad_palabras = len(nombre_archivo.split(" "))
	if(cantidad_palabras > 1):
		archivo_valido = False
		guardar_error("Nombre de archivo tiene mas de una palabra.")
	
	# Validar que la extension sea .txt
	if(not nombre_archivo.endswith('.txt')):
		archivo_valido = False
		guardar_error("Archivo no tiene extension .txt")
	
	return archivo_valido

# Funcion que valida cada linea del archivo vehiculoX.
def validar_linea_archivos_vehiculos (linea_por_validar, numero_de_linea):
	array_respuesta = [0 for x in range(3)]

	# Separar la linea por el simbolo (token) =
	arreglo_caracteristicas = linea_por_validar.split("=")
	
	if arreglo_caracteristicas[1][len(arreglo_caracteristicas[1])-1] == "\n":
		arreglo_caracteristicas[1] = arreglo_caracteristicas[1][0:len(arreglo_caracteristicas[1])-1]
	else:
		arreglo_caracteristicas[1] = arreglo_caracteristicas[1]
	
	
	if arreglo_caracteristicas [0] == "tipo" or arreglo_caracteristicas[0] == "modelo":
		
		array_respuesta[0] = True
		array_respuesta[1] = arreglo_caracteristicas[0]
		array_respuesta[2] = arreglo_caracteristicas[1]
		return array_respuesta
	else:
		array_respuesta [0] = False
	if arreglo_caracteristicas[0] != "modelo" or arreglo_caracteristicas[0] != "tipo":
		try:
			caracteristicas = int(arreglo_caracteristicas[0])
			guardar_error("La linea " + str(numero_de_linea) + " no cumple con la estructura requerida")
			array_respuesta[0]= False
		except ValueError:
			array_respuesta[0]= True
			array_respuesta[1]= arreglo_caracteristicas[0]
		valor_caracteristicas= int(arreglo_caracteristicas[1])
		if valor_caracteristicas >0:
			array_respuesta[2] = arreglo_caracteristicas[1]
		else:
			array_respuesta[0] = False
	return array_respuesta

# ------------------ Fin de definicion de funciones empleadas ------------------ #

#----------------------------Inicializacion de archivos----------------------------#

# Crear el archivo errores.txt para almacenar los errores.
crear_archivo("errores.txt")

# Crear el archivo log.txt para almacenar el registro de operacion del programa.
crear_archivo("log.txt")

guardar_log("Creados archivos errores.txt y log.txt")


#---------------------------------Validaciones----------------------------------#

# Obtener numero de argumentos de linea de comandos
cantidad_argumentos = len(sys.argv)

# Validar que el numero de argumentos sea igual a 2, garantizando que se haya el nombre del archivo del vehiculo.
if (cantidad_argumentos != 2):
	terminar_programa("Numero de argumentos incorrecto. Debe suministrar un argumento con el nombre del archivo del vehiculo")

guardar_log("Numero de argumentos OK")

sys.argv[1] = sys.argv[1]

# Validar la existencia, extension y nombre del archivo
if validar_archivo(sys.argv[1]) == False:
	terminar_programa("El archivo no cumple con los requerimientos.")

guardar_log("Extension, existencia y nombre del archivo OK")


# Variable que almacena el contenido de las lineas del archivo
lineas_archivo_vehiculo = tuple(leer_lineas_archivo(sys.argv[1]))

# Variable que almacena el numero de lineas del archivo
numero_lineas_archivo_vehiculo = len(lineas_archivo_vehiculo)

# Validacion para las lineas del archivo
for i in range (0, numero_lineas_archivo_vehiculo):
	linea_a_validar = validar_linea_archivos_vehiculos(lineas_archivo_vehiculo[i], i+1)
	if linea_a_validar[0] == False:
		terminar_programa('La linea: '+str(lineas_archivo_vehiculo[i])+'no tiene la estructura requerida')


# Validar que el tipo de vehiculo sea correcto

array_tipo_vehiculo = lineas_archivo_vehiculo[0].split('=')

if array_tipo_vehiculo[1][len(array_tipo_vehiculo[1])-1] == "\n":
	array_tipo_vehiculo[1] = array_tipo_vehiculo[1][0:len(array_tipo_vehiculo[1])-1]
else:
	array_tipo_vehiculo[1] = array_tipo_vehiculo[1]


if array_tipo_vehiculo[1] != "vehiculo" and array_tipo_vehiculo[1] != "vehiculo_aereo" and array_tipo_vehiculo[1] != "vehiculo_espacial":
	terminar_programa("El tipo de vehiculo no es correcto")

guardar_log("Numero caracteristicas OK")

#------------------------Creacion de clases y metodos---------------------#

class vehiculo():
	def __init__(self, modelo, n_ejes, cc_motor):
		self.modelo = modelo
		self.n_ejes = n_ejes
		self.cc_motor = cc_motor
	
	def mostrar_caracteristicas(self):
		print '----Caracteristicas del vehiculo----'
		print ""
		print 'Modelo: '+(self.modelo)
		print 'Numero de ejes: '+str(self.n_ejes)
		print 'Cilindraje: '+str(self.cc_motor)



class vehiculo_aereo(vehiculo):
	def __init__(self, modelo, n_ejes, cc_motor, n_alas, n_alerones, flaps):
		vehiculo.__init__(self, modelo, n_ejes, cc_motor)
		self.n_alas = n_alas
		self.n_alerones = n_alerones
		self.flaps = flaps
		
	def mostrar_caracteristicas_aereo(self):
		print "----Caracteristicas del vehiculo_aereo----"
		print ""
		print 'Modelo: '+(self.modelo)
		print 'Numero de ejes: '+str(self.n_ejes)
		print 'Cilindraje: '+str(self.cc_motor)
		print 'Numero de alas: '+str(self.n_alas)
		print 'Numero de alerones: '+str(self.n_alerones)
		print 'Flaps: '+str(self.flaps)

class vehiculo_espacial(vehiculo_aereo):
	def __init__(self, modelo, n_ejes, cc_motor, n_alas, n_alerones, flaps, n_cohetes, capac_astro, tamano_tanque):
		vehiculo_aereo.__init__(self, modelo, n_ejes, cc_motor, n_alas, n_alerones, flaps)
		self.n_cohetes = n_cohetes
		self.capac_astro = capac_astro
		self.tamano_tanque = tamano_tanque
		
	def mostrar_caracteristicas_espacial(self):
		print "----Caracteristicas del vehiculo espacial----"
		print ""
		print 'Modelo: '+(self.modelo)
		print 'Numero de ejes: '+str(self.n_ejes)
		print 'Cilindraje: '+str(self.cc_motor)
		print 'Numero de alas: '+str(self.n_alas)
		print 'Numero de alerones: '+str(self.n_alerones)
		print 'Flaps: '+str(self.flaps)
		print 'Numero de cohetes: ' +str(self.n_cohetes)
		print 'Capacidad de Astronautas: '+str(self.capac_astro)
		print 'Tamano tanque: '+str(self.tamano_tanque)
		
#------------------------Fin de creacion de clases y metodos---------------------#

#------------------------Inicio de logica del programa---------------------#

# Dependiendo del tipo del vehiculo se procede a verificar que el numero de caracteristicas sea correcto y 
# se almacenan en los objetos correspondientes, luego se llama a la funcion (metodo) que imprime la informacion
# de cada vehiculo.

if array_tipo_vehiculo[1] == "vehiculo":
	# Validar que el numero de caracteristicas sean 4 
	numero_lineas_vehiculo = leer_lineas_archivo(sys.argv[1])
	if numero_lineas_archivo_vehiculo < 4 :
		terminar_programa("El numero de caracteristicas es erroneo")
	array_vehiculo = [1 for t in range(numero_lineas_archivo_vehiculo)]
	for x in range (1, numero_lineas_archivo_vehiculo):
		array = lineas_archivo_vehiculo[x].split('=')
		array_vehiculo[x] = array[1]
	prop_vehiculo = vehiculo(array_vehiculo[1],array_vehiculo[2],array_vehiculo[3])
	prop_vehiculo.mostrar_caracteristicas()



if array_tipo_vehiculo[1] == "vehiculo_aereo":
	# Validar que el numero de caracteristicas sean 6 
	numero_lineas_vehiculo = leer_lineas_archivo(sys.argv[1])
	if numero_lineas_archivo_vehiculo < 6 :
		terminar_programa("El numero de caracteristicas es erroneo")
	array_vehiculo = [1 for t in range(numero_lineas_archivo_vehiculo)]
	for x in range (1, numero_lineas_archivo_vehiculo):
		array = lineas_archivo_vehiculo[x].split('=')
		array_vehiculo[x] = array[1]
	prop_vehiculo_aereo = vehiculo_aereo(array_vehiculo[1], array_vehiculo[2], array_vehiculo[3], array_vehiculo[4], array_vehiculo[5], array_vehiculo[6])
	prop_vehiculo_aereo.mostrar_caracteristicas_aereo()


if array_tipo_vehiculo[1] == "vehiculo_espacial":
	# Validar que el numero de caracteristicas sean 9 
	numero_lineas_vehiculo = leer_lineas_archivo(sys.argv[1])
	if numero_lineas_archivo_vehiculo < 9 :
		terminar_programa("El numero de caracteristicas es erroneo")
	array_vehiculo = [1 for t in range(numero_lineas_archivo_vehiculo)]
	for x in range (1, numero_lineas_archivo_vehiculo):
		array = lineas_archivo_vehiculo[x].split('=')
		array_vehiculo[x] = array[1]
	prop_vehiculo_espacial = vehiculo_espacial(array_vehiculo[1], array_vehiculo[2], array_vehiculo[3], array_vehiculo[4], array_vehiculo[5], array_vehiculo[6], array_vehiculo[7], array_vehiculo[8], array_vehiculo[9])
	prop_vehiculo_espacial.mostrar_caracteristicas_espacial()

guardar_log("Imprimiendo caracteristicas del"+str(array_tipo_vehiculo[1]))

#------------------------Finalizacion del programa---------------------#