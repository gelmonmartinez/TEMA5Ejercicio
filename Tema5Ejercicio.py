import re #LIBRERIA O REPOSITORIO DE LA EXPRESIONES REGULARES UTILIZADAS
#SE USARA UN EJEMPLO DESCARGADO EN JAVA PARA ESTE EJERCICIO ES EL MAS UTILIZADO.
#LA INTRUCCION DICTA QUE DEBEMOS PASAR DE OTRO LENGUAJE DE PROGRAMACION SE ABRA EN PYTHON
path = "Ejemplo.java"

try:
    archivo = open(path, "r")
except:
    print ("El archivo que intentas abrir no existe")
    quit()

texto = ""

for linea in archivo:
    texto += linea

#ASGINACION DE LAS SENTENCIAS. EJEMPLO: suma = 0, factorial = 1, vidas = cont, etc.
patron = r"[a-zA-Z]{1,}[\s\S][=][\s\S]\w*.\;"
#OPERACIONES BASICAS. Ejemplo: suma = 2.7 + 3, cont = cont + 1, etc. 
patron1 = r"\w.[\=]{1}\w*.\w*.[+|-|*|/]{1}\w*.\w*.\;"
#BOOLEANAS BASICAS UTILIZADAS Ejemplo: edad >= 5, suma != 0, etc.
patron2 = r"[a-zA-Z]+w*.[==|>=|<=|!=]{2}w*.[a-zA-Z0-9]"
#FORMULAS DE TIPO CX = a op ( b op d)
patron3 = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\s|\S][\*|\/|\%|\+|\-][\s|\]\([\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][\S|\s][\w|\d.\d]{1,}[ \)|\S\)]\;"
#ESTRUCTURA DE CONTROL:AL. if, while, for, etc.
patron4 = r"[for|if|while].*[\(]\w.*[\)]{"


respu = re.findall(patron, texto)
respu1 = re.findall(patron1, texto)
respu2 = re.findall(patron2, texto)
respu3 = re.findall(patron3, texto)
respu4 = re.findall(patron4, texto)
print ("\n Respuesta 1 \n\n", respu)
print ("\n Respuesta 2 \n\n", respu1)
print ("\n Respuesta 3 \n\n", respu2)
print ("\n Respuesta 4 \n\n", respu3)
print ("\n Resultado 5 \n\n", respu4)
