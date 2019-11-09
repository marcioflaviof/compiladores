# -*- coding: utf-8 -*-
import string

def Errors(phrase):

    if "((" in phrase or "))" in phrase:
        print("Erro de par�ntese")

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
        print("H� uma estrutura de sele��o, IF")
        Lexical(b)

    elif "for(" in structures:
        a = structures.replace("for(", "")
        b = a.replace("):", "")
        print("H� uma estrutura de repeti��o, FOR")
        Lexical(b)
    
    elif "while(" in structures:
        a = structures.replace("while(", "")
        b = a.replace("):", "")
        print("H� uma estrutura de repeti��o While")
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
          a = "Um operador � necessario entre dois operandos"
          break;

        elif word.isalpha():
            a += "{} � uma variavel \n".format(word)
            quantidade += 1

        elif word.isdigit() or word.lstrip('-').isdigit():
            a += ("{} � um numeral \n".format(word))
            quantidade += 1


        elif word in b:
            quantidade += 1
            a += "{} � um operador de atribui��o \n".format(word)
        
        elif word in c:
            quantidade += 1
            a += "{} � um operador aritim�tico \n".format(word)
         
        if quantidade > 3:
            a = "Quantidade de operadores inv�lida"
            return Printer(a)
    return Printer(a)

def Printer(a):
    print(a)

frase = input("Coloque aqui seu comando: ")
Errors(frase)
