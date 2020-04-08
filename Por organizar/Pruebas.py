"""class Alumno:
    hola =''

    def __init__(self):
        self.nombre = "Pablo"

    def saludar(self):
        #"Imprime un saludo en pantalla"
        print("Hola mundo")
    def ecuacion(self):
        print("A dormir perrito")
        
alumno = Alumno()
alumno.hola='hola'
alumno.saludar()
alumno.ecuacion()
alumno.nombre="Pedro"
class Hola:
    pass
#Javier= Hola()
#print (Javier)
---------------------------------

class Person:
    name =''
    
    school=''

    def Imp_Name(self):
        print ("hola", self.name,
               'como va todo?', self.school)
    
Javier = Person()
Javier.name = "javier"
Javier.school = "U distrital"
Javier.Imp_Name()
Javier.name = "Andres"
Javier.Imp_Name()

-------------------------------------------------
class Persona:
    def __init__(self, n, s):
        self.nombre = n
        self.escuela = s
    def Imprimir_Nombre(self):
        print ("Hola",self.nombre)
    def Imprimir_Universidad(self):
        print ("Bienvenido a la",self.escuela)


Javier = Persona("Andres","U Distrital")
Javier.Imprimir_Nombre()
Javier.Imprimir_Universidad()
Munoz = Persona(2,3)
Munoz.Imprimir_Nombre()
Munoz.Imprimir_Universidad()
Javier.Imprimir_Nombre()
--------------------------------------
class Datos:
    "Define el area de un rectangulo"
    def __init__(self,b,h):
        self.h=h
        self.b=b
             
class Area_Triangulo(Datos):
    def area(self):
        return (self.h*self.b)/2
class Area_Rectangulo(Datos):
    def area(self):
        return self.h*self.b
        
Rectangulo=Area_Rectangulo(1,3)
Triangulo=Area_Triangulo(1,3)
print(Rectangulo.area())
print(Triangulo.area())
--------------------------------------------

while True:
    try:
        edad = int(input("Escribe tu edad: "))
        break
    except ValueError:
        print("¡Debes ingresar un número!")

if edad >= 18:
    print("Eres un adulto.")
else:
    print("Aún no eres un adulto.")
-----------------------------------------
K=["A", "B", "C", "D", "E", "F"]
print(K)
print ("K[1:4]", K[1:4])
print ("K[:4]", K[:4])
print ("K[1:]", K[1:])
print ("K[:]", K[:])
print ("K[1:len(K)]", K[1:len(K)])
print ("K[1:-1]", K[1:-1])
print ("K[1:4:2]", K[1:4:2])
print ("K[:-1]", K[:-1])
print ("K[::-1]", K[::-1])
S="Hola mundo"
print (S)
print("S[::-1]",S[::-1])
print("S[1::2])",S[1::2])
o=list(enumerate(K))
print (o)
print (enumerate(K))
----------------------------------------

k = 123
p="andres"
f=open("/home/pi/Desktop/Prueba/Texto.txt", "a")
f.write(str(p)+" hola " + str(k) + "\n")
#f.write(" Bienvenidos  \n" , ((k)))
f.close()
f=open("/home/pi/Desktop/Prueba/Texto.txt")
print(f.read())
f.close()

----------------------------------------

#IMPORTANDO LIBRERIAS (MODULOS)
from Prueba_Libreria import *
print(sumar(4,7))
print(mult(4,7))

-------------------------------

#import Prueba.suma
#import Prueba import suma
from Prueba import suma
print (suma.suma(2,2,2))
#print (Prueba.Prueba_Libreria.sumar(2,2))
------------------------

import math
from random import *
print (math.sqrt(16))
print (choice(["hola", "mundo", "animal"]))
print (randint (1,20))
print(hex(10))
--------------------------
"""
#Libreria para graficar 
from tkinter import *
apl = Tk()
texto = Label(apl, text ="Hola mundo")
texto.pack()
apl.mainloop()
