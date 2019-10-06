import string

const1 = "Número"
const2 = "Identificador "
const3 = "Operador Aritmético MULT"
const4 = "Operador Aritmético ADD"
const5 = "Delimitador"
const6 = "Operador de atribuição"
const7 = "Operador Aritmético DIV"
const8 = "Operador Aritimético SUB"



def erroSintaxe(a):
	variavel = ""
	variaveltwo = ""
	operadores = ["/", "+", "-", "*", "%"]
	digitos = string.ascii_letters + "0123456789"

	for i in a:

		if digitos.find(variavel) >= 0 and variaveltwo == " " and digitos.find(i) >= 0:
			return("Foram encontradas duas varáveis seguidas e separadas por espaço em branco {} {}".format(variavel, i))
		
		elif variavel in operadores and variaveltwo == " " and i in operadores:
			return("Foram encontrados dois operadores seguidos e separados por espaço em branco {} {}".format(variavel, i))

		variavel = variaveltwo
		variaveltwo = i
	

	return analisadorAritimetico(a)




def analisadorAritimetico(a):
	mystring = ""
	alphabet = string.ascii_letters
	operadores = 0
	operando = 0
	atribuicao = 0

	for i in a:

		if i.isdigit():
			mystring += ("{} | {} \n".format(i, const1))

		elif i in alphabet:
			mystring += ("{} | {}{} \n".format(i, const2, str(operando)))
			operando += 1

		elif i == chr(42):
			mystring += ("{} | {} \n".format(i, const3))
			operadores += 1

		elif i == chr(43):
			mystring += ("{} | {} \n".format(i, const4))
			operadores += 1

		elif i == chr(59):
			mystring += ("{} | {} \n".format(i, const5))

		elif i == chr(61):
			mystring += ("{} | {} \n".format(i, const6))
			atribuicao +=1

		elif i == chr(47):
			mystring += ("{} | {} \n".format(i, const7))
			operadores += 1

		elif i == chr(45):
			mystring += ("{} | {} \n".format(i, const8))
			operadores += 1

		if operadores > 2:
			return "Quantidade incorreta de operadores"

		if operando > 4:
			return "Quantidade incorreta de operandos"

		if atribuicao == 2:
			return "Tem mais de um operador de atribuição"

	return mystring






a = input("Coloque aqui sua equação: ")
print(erroSintaxe(a))



