#5.1 Defina una función en python que acepte el radio y devuelva el valor 
#del area de un círculo de esas dimensiones.
def calcular(r,pi):
    area= pi* r**2
    return (area)
from math import pi
from re import A
from tkinter import CENTER
from turtle import left, right

r= float(input("Escriba el valor del radio del circulo:"))
area= pi* r**2 
print("El valor del radio es {}".format(area))


#Defina una función en python que acepte 3 
# valores y devuelva solo el maximo de los tres. 

def valores(a,b,c): 
    if(a > b) and (a > b):{
        print("el numero mayor es:", a)
    }
    if (b > a) and (b > c):{
        print("El numero mayor es:", b)
    }
    if (c > a) and (c > b):{
        print("El numero mayor es:",c)
    }

a= float(input("Escriba un valor")) 
b= float(input("Escriba un valor"))
c= float(input("Escriba un valor"))

if(a > b) and (a > b):{
        print("el numero mayor es:", a)
    }
if (b > a) and (b > c):{
        print("El numero mayor es:", b)
    }
if (c > a) and (c > b):{
        print("El numero mayor es:",c)
    }
#Dado una lista de enteros, defina una función en 
#python que devuelva la suma de solo los valores impares de dicha lista.
lista= [1,2,3,4,5,65,78,9,23,56,76,45]

def sumar_impares(lista):
    if len (lista) == 0:
        return 0
    elif lista[0] % 2 !=0:
        return lista[0] + sumar_impares(lista[1 :])
    else:
        return sumar_impares(lista[1 :])
print ("la suma de los impares es:")
print(sumar_impares(lista))


#5.4 Desarrolle una función en python que acepte una variable string 
# como primer parámetro y la cantidad de caracteres de como 
# segundo parámetro. La función debe retornar un nuevo string que 
# consista en el string original y el número correcto de caracteres 
# necesarios para que el string se 
#salga centrado. No agregue caracteres al final del string.
def centrado(a, b):
    espacio = ' '
    cuantos = int((b-len(a))/2)
    return f'{cuantos*espacio}{a}'

a = input('Introduzca una palabra: ')
b = int(input('Introduzca la cantidad de caracteres: '))

print(centrado(a, b))






























