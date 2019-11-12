import re
import string

operatorslist = {"+":"Adição", "-":"Subtração", "*":"Multiplicação", "/":"Divisão", "**":"Exponencial", "=":"Comparação",
"++":"Adição", "--":"Subtração", "and":"Comparação", "or":"Comparação", "in":"Comparação", ">=":"Comparação", "<=":"Comparação",
"!=":"Comparação", "==":"Comparação"} 

comparelist = ["and", "or", "in", ">=", "<=", "!=", "==", "=", ">", "<"]
commonmistakes = ["=>", "=<", "whilee", "foor", "forr", "iff", "fpr", "-+", "+-"]
structures = ["if", "for", "while"]
comparer = ["/8", "?8", "?/", "/?", "8/", "*?", "8?", "* /", "/ /", "??", "\\\\", "\\\\/", "/\\", "\\/", "||"]



def checkBlockComments(phrase):

	if ("/*" in phrase) and ("*/" in phrase) == False:
		return("Você digitou o comentário errado")


	elif ("/*" in phrase) == False and ("*/" in phrase):
		return("Você digitou o comentário errado")


	else:
		return checkComments(phrase)

def checkComments(phrase):

    a= ""

    for word in comparer:
        if word in phrase:
            return ("Algum comentário foi digitado incorretamente")

    return(removeComments(phrase))



def removeComments(phrase):
    phrase = re.sub(re.compile("/\*.*?\*/",re.DOTALL ), "", phrase)
    a = ""
    for i in phrase:
        b = a + i
        a = i
        if b == "//":
            phrase = phrase[:phrase.find("//")]
    
    print("Sua frase foi: {}".format(phrase))
    return spaces(phrase)


def spaces(phrase):
    
    newphrase = phrase.replace(" ", "")

    return checkStructures(newphrase)


def checkStructures(phrase):
    
    print("-" * 90)

    a = splitting(phrase)

    if a[0] == "for" or a[0] == "while":
        print("Há uma estrutura de repetição, {}".format(a[0]))
        phrase = phrase.replace("for", "").replace("while", "")
    
    elif a[0] == "if":
        print("Há uma estrutura de seleção, if")
        phrase = phrase.replace("if", "")

    
    checkOperatorsErrors(phrase)



def checkOperatorsErrors(phrase):

    if checkOperatorstwo(phrase) == False:
        return ("[ERROR] Não há operadores válidos")
    
    if commonErrors(phrase) == True:
        return ("[ERROR] Algum operador foi digitado incorretamente")

    else:
        return checkOperators(phrase)


def commonErrors(phrase):

    for operator in commonmistakes:
        if operator in phrase:
            return True

        else:
            return False


def checkOperators(phrase):
    print("-" * 90)
    print("OPERADORES: ")
    nextstring = ""
    twostrings = ""
    threestrings = ""

    for a in phrase:
        threestrings = twostrings + a
        twostrings = nextstring+a

        if threestrings in operatorslist:
            print("{} é um operador de {}".format(threestrings, operatorslist[threestrings]))
            phrase = phrase.replace(threestrings, "=")

        elif twostrings in operatorslist:
            print("{} é um operador de {}".format(twostrings, operatorslist[twostrings]))
            phrase = phrase.replace(twostrings, "=")

        elif compareTheLast(a) == True:
            print("{} é um operador de {}".format(a, operatorslist[a]))
            phrase = phrase.replace(a, "=")

        nextstring = a
    
    print("-" * 90)
    checkFloats(phrase)




def compareTheLast(character):

    for a in operatorslist:

        if character == a:
            return True

    return False

def checkOperatorstwo(phrase):


    words_re = re.compile("|".join(comparelist))
    if words_re.search(phrase):
        return True

    else:
        return False


        
def splitting(phrase):

    newphrase = re.findall(r"[\w]+", phrase)
    return newphrase




def checkVariables(phrase):

    for variable in phrase:
        if variable.isalpha():
            print("{} é uma variavel".format(variable))
        
        elif variable.isdigit():
            print("{} é um numeral".format(variable))
    


def checkFloats(phrase):

    print("VARIAVEIS E NUMERAIS: ")

    matches = re.findall("[+-]?\d+\.\d+", phrase)
    counter = 0

    if matches:
        for element in matches:
            print("{} é um float".format(matches[counter]))
            phrase = phrase.replace(matches[counter],"")
            counter += 1

    return checkVariables(splitting(phrase))

def listToString(list):
    
    str1 = ""
    return str1.join(list)



a = input("Coloque aqui a sua frase: ")
print(checkBlockComments(a))