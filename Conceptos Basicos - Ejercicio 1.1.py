#Conceptos Basicos - Ejercicio 1.1
menu = 1

def pedirNumeroEntero(texto):                              # Validacion numero entero
 
    correcto=False
    num=0
    while(correcto == False):
        try:
            num = int(input(texto))
            correcto=True
        except:
            print("Error - No es un numero")
     
    return num

##def validarSiNo(respuesta):
##    while(respuesta != "SI" and respuesta != "NO"):
##          respuesta = str.upper(input("Desea repetir el proceso? [Si/No]\n"))
##    return respuesta
          

while(menu ==1):                                                      #Menu
    
    print(" _______________________________")
    print("|Elija una funcion: [A / B / C] |")
    print("|-------------------------------|")       
    print("|A)Saludo                       |")
    print("|B)Multiplicar 2 numeros        |")
    print("|C)Terminar                     |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
    opcion = str.upper(input())
    
    while(opcion != "A" and opcion != "B" and opcion != "C"):           #Verificador de opcion valida
        
            opcion = str.upper(input("Ingrese una opcion valida: "))
    
    if (opcion == "A"):                                                 #Opcion A
        
        respuestaA= "SI"
        
        while(respuestaA == "SI"):

            nombre = input("\nIngrese su nombre: ")
            
            print("\nHola %s, bienvenido a el programa!\n" % nombre)
            
            respuestaA = str.upper(input("Desea repetir el proceso? [Si/No]\n"))

            while (respuestaA != "SI" and respuestaA != "NO"):
                
                respuestaA = str.upper(input("Desea repetir el proceso? [Si/No]\n"))
            
    if (opcion == "B"):                                                #Opcion B
        
        respuestaB = "SI"
        
        while(respuestaB == "SI"):
            
            n1 = pedirNumeroEntero("Introduce el primer numero: ")
            
            n2 = pedirNumeroEntero("Introduce el segundo numero: ")
            
            print("\nProducto: ",n1 * n2)
            
            respuestaB = str.upper(input("\nDesea repetir el proceso? [Si/No]\n"))
            
            while (respuestaB != "SI" and respuestaB != "NO"):
                
                respuestaB = str.upper(input("Desea repetir el proceso? [Si/No]\n"))
            
    if (opcion == "C"):                                                #Opcion C
        
        print("\n Hasta pronto!!")
        
        break
        
            
            
