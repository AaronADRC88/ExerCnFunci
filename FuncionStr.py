__author__ = 'aferreiradominguez'
# 1. Imprima los dos primeros caracteres.
# 2. Imprima los tres ?ltimos caracteres.
# 3. Imprima dicha cadena cada dos caracteres. Ej.: recta deber?a imprimir rca
# 4. Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
# 5. Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.
cadea = "HolalOpOkO"


def corta2Cadea(str):
    str = str[0]+str[1]
    return str


def corta3FinCad(str):
    tam = len(str)
    str = str[tam - 3] + str[tam-2 ]+str[tam-1]
    return str

def siNo(str):
    tam =int(len(str))
    cad=""
    for i in range(0,tam,1):

        if(i%2==0):
            cad=cad+str[i]
    return cad
def alReves(str):
    tam =int(len(str))
    cad=""
    for i in range(0,tam,1):
        cad=cad+str[(tam-1)-i]
    return cad
def alRevesYalDerecho(str):
    print(str)
    tam =int(len(str))
    cad=""
    for i in range(0,tam,1):
        cad=cad+str[(tam-1)-i]
    return cad

print(corta2Cadea(cadea))
print(corta3FinCad(cadea))
print(siNo(cadea))
print(alReves(cadea))
print(alRevesYalDerecho(cadea))
