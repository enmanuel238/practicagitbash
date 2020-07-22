import random


def generador_contrasena():
	#Este es un generador de contraseñas aleatorias


	mayusculas = [
	"A","B","C","D","E","F","G","H","I","J","K","L",
	"M","N","O","P","Q","R","S","T","U","W","X","Y","Z"
	]
	minusculas = [		
	"a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","w","x","y","z"
	]
	numeros = [
	"1","2","3","4","5","6","7","8","9","0"
	]
	caracteres = mayusculas + minusculas + numeros
	contrasena = []

	for i in range (15):
		caracter_random = random.choice(caracteres)
		contrasena.append(caracter_random)

	contrasena="".join(contrasena)
	return contrasena





def main():

	contrasena = generador_contrasena()
	print("Tu nueva contraseña es: " + str(contrasena))
	
 
if __name__ == '__main__':
	main()