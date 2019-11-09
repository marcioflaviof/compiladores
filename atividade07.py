# -*- coding: utf-8 -*-
import string

def Errors(phrase):

    if "((" in phrase or "))" in phrase:
        print("Erro de parêntese")

    elif "(" in phrase and ")" in phrase:
        Cases(phrase)

    else:
        print("Sintaxe erro")


def Cases(structures):
    a = ""
    b = ""
    if "if(" in structures:
        a = structures.replace("if(", "")
        b = a.replace("):", "")
        print("Há uma estrutura de seleção, IF")
        Lexical(b)

    elif "for(" in structures:
        a = structures.replace("for(", "")
        b = a.replace("):", "")
        print("Há uma estrutura de repetição, FOR")
        Lexical(b)
    
    elif "while(" in structures:
        a = structures.replace("while(", "")
        b = a.replace("):", "")
        print("Há uma estrutura de repetição While")
        Lexical(b)
    
    else:
        print("Sem nenhuma estrutura aqui")


def Lexical(phrase):
    a = ""
    b = ["=", "!=", ">", "<", ">=", "<=", "in"]
    c = ["+", "-", "/", "*"]

    quantidade = 0    
    for i, word in enumerate(phrase.split()):

        if word.isalnum and phrase[i+1].isalnum():
          a = "Um operador é necessario entre dois operandos"
          break;

        elif word.isalpha():
            a += "{} é uma variavel \n".format(word)
            quantidade += 1

        elif word.isdigit() or word.lstrip('-').isdigit():
            a += ("{} é um numeral \n".format(word))
            quantidade += 1


        elif word in b:
            quantidade += 1
            a += "{} é um operador de atribuição \n".format(word)
        
        elif word in c:
            quantidade += 1
            a += "{} é um operador aritimético \n".format(word)
         
        if quantidade > 3:
            a = "Quantidade de operadores inválida"
            return Printer(a)
    return Printer(a)

def Printer(a):
    print(a)

frase = input("Coloque aqui seu comando: ")
Errors(frase)
