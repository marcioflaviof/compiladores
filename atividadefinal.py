import re
import string

operatorslist = {"+":"Adição", "-":"Subtração", "*":"Multiplicação", "/":"Divisão", "**":"Exponencial", "=":"Comparação",
"++":"Adição", "--":"Subtração", "and":"Comparação", "or":"Comparação", "in":"Comparação", ">=":"Comparação", "<=":"Comparação",
"!=":"Comparação", "==":"Comparação"} #reconhecer floats, operatorslist não funciona

commonmistakes = ["=>", "=<", "whilee", "foor", "forr", "iff"]
structures = ["if", "for", "while"]


def spaces(phrase):
    
    newphrase = phrase.replace(" ", "")

    return checkStructures(newphrase)


def checkStructures(phrase):
    
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

    print("OPERADORES: ")
    nextstring = ""
    twostrings = ""
    threestrings = ""

    for a in phrase:
        threestrings = twostrings + a
        twostrings = nextstring+a

        if threestrings in operatorslist:
            print("{} é um operador de {}".format(threestrings, operatorslist[threestrings]))

        elif twostrings in operatorslist:
            print("{} é um operador de {}".format(twostrings, operatorslist[twostrings]))

        elif compareTheLast(a) == True:
            print("{} é um operador de {}".format(a, operatorslist[a]))

        phrase = phrase.replace("and", "=").replace("or", "=").replace("in", "=")
        nextstring = a
    
    print("\n")
    return checkVariables(splitting(phrase))



def compareTheLast(character):

    for a in operatorslist:

        if character == a:
            return True

    return False

def checkOperatorstwo(phrase):


    words_re = re.compile("|".join(comparelist))
    words_retwo = re.compile("|".join(comparelisttwo))
    if words_re.search(phrase) or words_retwo.search(phrase):
        return True

    else:
        return False


        
def splitting(phrase):

    newphrase = re.findall(r"[\w]+", phrase)
    return newphrase




def checkVariables(phrase):

    print("VARIAVEIS E NUMERAIS: ")

    for variable in phrase:
        if variable.isalpha():
            print("{} é uma variavel".format(variable))
        
        elif variable.isdigit():
            print("{} é um numeral".format(variable))




def listToString(list):
    
    str1 = ""

    return str1.join(list)



        


a = input("Coloque aqui a sua frase: ")
print(spaces(a))