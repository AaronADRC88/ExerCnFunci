__author__ = 'aferreiradominguez'
#1. Inserte el caracter entre cada letra de la cadena. Ej: separar y , deber?a devolver s,e,p,a,r,a,r
#2. Reemplace todos los espacios por el caracter. Ej: mi archivo de texto.txt y \_ deber?a devolver mi\_archivo\_de\_texto.txt
#3. Reemplace todos los d?gitos en la cadena por el caracter. Ej: su clave es: 1540 y X deber?a devolver su clave es: XXXX
#4. Inserte el caracter cada 3 d?gitos en la cadena. Ej. 2552552550 y . deber?a devolver 255.255.255.0

cadea="separar"
char=','
print (char.join(cadea))
cadeaEs=" cadea con espacios no medio"
charEs=' '
print(cadeaEs.split(charEs))
cadeaNum="12345"
charNew='X'
def replace_all(str):
    cad=""
    for i in str:
        cad=cad+i.replace(i,charNew)
    return cad

print(replace_all(cadeaNum))
cadeaNum2="2552552550"
charNum='.'
print((repr(3.0)))