#Ejercicio 5.1. Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso
#si desea ingresar más notas, e imprimiendo el promedio correspondiente

print("|Programa para sacar promedio|")

notas = []

contador = 0
suma = 0
respuesta = "SI"

while (respuesta == "SI"):
    while True:
        try:
            nota = int(input("Ingrese una nota: "))
            break
        except:
            print("\nERROR - NO ES UN NUMERO ENTERO\n")

    notas.append(nota)

    suma = suma + notas [contador]

    contador += 1

    respuesta =input("\nDesea ingresar otra nota? [SI/NO]\n")
    respuesta = respuesta.upper()

    while(respuesta != "SI" and respuesta != "NO"):
        print("ERROR - RESPUESTA INVALIDA")
        respuesta =input("\nDesea ingresar otra nota? [SI/NO]\n")
        respuesta = respuesta.upper()
    
promedio = suma / contador

print ("\nEl promedio es: ", promedio)
