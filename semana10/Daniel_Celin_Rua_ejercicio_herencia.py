#Clases de vehiculos V0.0.1
#programa capaz de organizar las clases de vehiculos, las clases de vehiculos estan 
#definidas en 4 archivos de texto.

# Desarrollado por Daniel Celin Rua
# octubre 12 de 2015

# ------------------ Inicio de definicion de constantes y parametros ------------------ #
print '	'
c1=vehiculo(leer_archivo1)
print c1.mostrar_detalle()
print '	'
c2=vehiculo(leer_archivo2)
print c2.mostrar_detalle()
print c2.mostrar_detalle()
print '	'
c3=vehiculo_Aereo(leer_archivo3)
print c3.mostrar_detalle()
print '	'
c4=vehiculo_Espacial(leer_archivo4)
print c4.mostrar_detalle()
print '	' 
# ------------------ fin de definicion de constantes y parametros ------------------ #


# ------------------ Inicio de clases empleadas ------------------ #
class vehiculo ():
	def __init__(self,modelo,cilindraje,n_ejes):
		self.modelo=modelo
		self.cilindraje=cilindraje
		self.n_ejes=n_ejes

	def mostrar_detalle(self):
		return'los detalles del vehiculo son:'+str(self.modelo)+'	'+str(self.cilindraje)+'	'+str(self.n_ejes)


class vehiculo_Aereo(vehiculo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones):
		self.modelo=modelo
		self.cilindraje=cilindraje
		self.n_ejes=n_ejes
		self.n_alas=n_alas
		self.n_alerones=n_alerones
	def mostrar_detalle(self):
		return'los detalles del vehiculo_Aereo son:'+str(self.modelo)+'	'+str(self.cilindraje)+'	'+str(self.n_ejes)+'	'+str(self.n_alas)+'	'+str(self.n_alerones)



class vehiculo_Espacial(vehiculo_Aereo):
	def __init__(self,modelo,cilindraje,n_ejes,n_alas,n_alerones,n_cohetes):
		self.modelo=modelo
		self.cilindraje=cilindraje
		self.n_ejes=n_ejes
		self.n_alas=n_alas
		self.n_alerones=n_alerones
		self.n_cohetes=n_cohetes
	def mostrar_detalle(self):
		return'los detalles del vehiculo_Espacial son:'+str(self.modelo)+'	'+str(self.cilindraje)+'	'+str(self.n_ejes)+'	'+str(self.n_alas)+'	'+str(self.n_alerones)+'	'+str(self.n_cohetes)
# ------------------ Fin de clases empleadas ------------------ #



# ------------------ Inicio de definicion de funciones empleadas ------------------ #
# Funciones que leen las lineas de los archivos de texto y las devuelve en una lista.
def leer_archivo1(): 
	archivo = open("vehiculo1.txt", "r")
	linea=()
	for linea in archivo.readlines():
		
		x=linea.find('=')+1
		print linea[x:]

def leer_archivo2(): 
	archivo = open("vehiculo2.txt", "r")
	linea=()
	for linea in archivo.readlines():
		
		x=linea.find('=')+1
		print linea[x:]

def leer_archivo3(): 
	archivo = open("vehiculo3.txt", "r")
	linea=()
	for linea in archivo.readlines():
		
		x=linea.find('=')+1
		print linea[x:]

def leer_archivo4(): 

	archivo = open("vehiculo4.txt", "r")
	linea=()
	for linea in archivo.readlines():
		
		x=linea.find('=')+1
		print linea[x:]

# ------------------ Fin de definicion de funciones empleadas ------------------ #