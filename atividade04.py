import re

mystring = input("Digite aqui seu texto: ")



def checkBlockComments(string):

	if ("/*" in string) and ("*/" in string) == False:
		print("Você digitou errado, digite novamente!")
		mynewstring = input("Digite aqui seu código: ")
		return checkBlockComments(mynewstring)

	elif ("/*" in string) == False and ("*/" in string):
		print("Você digitou errado, digite novamente!")
		mynewstring = input("Digite aqui seu código: ")
		return checkBlockComments(mynewstring)

	else:
		return checkComments(string)



def checkComments(string):
	comparer = ["/8", "?8", "?/", "/?", "8/", "*?", "8?", "* /", "/ /", "??", "\\\\", "\\\\/", "/\\", "\\/", "||"]
	a= ""

	for word in comparer:
		for i in string:
			b = a+i
			a = i
			if b == word:
				print("Você digitou errado, digite novamente!")
				mynewstring = input("Digite aqui seu código: ")
				return checkComments(mynewstring)

	return(removeComments(string))



def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ), "", string)
    a = ""
    for i in string:
        b = a + i
        a = i
        if b == "//":
            string = string[:string.find("//")]


    print(string)



checkBlockComments(mystring)
