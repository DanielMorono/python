#Ejercicio Ciclos - ejercicio 5.1 FALTA TERMINAR
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
            print("\n ERROR - NO ES UN NUMERO ENTERO\n")

    notas.append(nota)

    suma = suma + notas [contador]

    contador += 1

    respuesta =input("\n Desea ingresar otra nota? [SI/NO]\n")
    respuesta = respuesta.upper()    
    
promedio = suma / contador

print ("\nEl promedio es: ", promedio)
