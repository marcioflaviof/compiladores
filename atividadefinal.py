import re
import string
import infixtopostfix

operatorslist = {"+":"Adição", "-":"Subtração", "*":"Multiplicação", "/":"Divisão", "**":"Exponencial", "=":"Atribuição",
"++":"Adição", "--":"Subtração", "and":"Comparação", "or":"Comparação", "in":"Comparação", ">=":"Comparação", "<=":"Comparação",
"!=":"Comparação", "==":"Comparação", ">":"Comparação", "<":"Comparação"} 

comparelist = ["and", "or", "in", ">=", "<=", "!=", "==", "=", ">", "<"]
commonmistakes = ["=>", "=<", "whilee", "foor", "forr", "iff", "fpr", "-+", "+-"]
structures = ["if", "for", "while"]
comparer = ["/8", "?8", "?/", "/?", "8/", "*?", "8?", "* /", "/ /", "??", "\\\\", "\\\\/", "/\\", "\\/", "||"]

#passar da forma infixa para pós-fixa

def checkIfExists(phrase):

    if phrase != "":
        checkBlockComments(phrase)

    else:
        return print("[ERROR] Esqueceu da frase")


def checkBlockComments(phrase):

	if ("/*" in phrase) and "*/" not in phrase:
		return print("[ERROR] Você digitou o comentário errado")


	elif "/*" not in phrase and "*/" in phrase:
		return print("[ERROR] Você digitou o comentário errado")


	else:
		return checkComments(phrase)

def checkComments(phrase):

    a= ""

    for word in comparer:
        if word in phrase:
            return print("[ERROR] Algum comentário foi digitado incorretamente")

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

    return checkBrackets(newphrase)


def checkBrackets(phrase):

    if  ("for" or "if" or "while") == True and ("(" in phrase and ")" in phrase) == False:
        return print("[ERROR] Faltam parênteses")
    
    else:
        return checkStructures(phrase)


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
    
    if commonErrors(phrase) == True:
        return print("[ERROR] Algum operador foi digitado incorretamente")

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


def splitting(phrase):

    newphrase = re.findall(r"[\w]+", phrase)
    return newphrase


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


def checkVariables(phrase):

    number = 1

    for variable in phrase:
        if variable.isalpha():
            print("{} = Identificador {}".format(variable, str(number)))
            number += 1
        
        elif variable.isdigit():
            print("{} é um Inteiro".format(variable))
    


def listToString(list):
    
    str1 = ""
    return str1.join(list)





a = input("Coloque aqui a sua frase: ")
infixtopostfix = infixtopostfix.Conversion(len(a))
infixtopostfix.infixToPostfix(a)
checkIfExists(a)