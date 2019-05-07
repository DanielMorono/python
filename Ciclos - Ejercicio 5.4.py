#Ejercicio 5.4 - Falta terminar
import random

numeroRandom = random.randrange (1,50)

print (numeroRandom)

print ("Numero random generado\n")

while True:
    while True:
        try:
            numeroIngresado = int(input("Ingrese el numero: "))
            break
        except:
            print("ERROR - NO ES UN NUMERO ENTERO\n")

    if (numeroIngresado > numeroRandom):
        print("Incorrecto - El numero ingresado es mayor\n")
    if (numeroIngresado < numeroRandom):
        print("Incorrecto - El numero ingresado es menor\n")
    if (numeroIngresado == numeroRandom):
        print ("Respuesta CORRECTA!! El numero era ",numeroRandom)
        break
    


