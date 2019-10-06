a = input("Diga sua frase: ")
c = 0

for i in range	(len(a)):
	if(a[i] == " "):
		c += 1

print("Sua frase possui " + str(len(a) - c +1) + " caracteres")
print("Total de espaços em branco encontrados: " + str(c))
print("Número de caracters com espaço " + str(len(a)+1))
b = a.split(" ")
print("".join(b))