try:
    Total=0

    #Creamos un loop que dure 3 iteraciones
    for i in range (1, 4 ,1): 
        #Vamos sumando en la variable total todas las calificaciones
        Total += float(input(F"Inserta examen {i}: "))

    #Sacamos el promedio y lo redondeamos a dos decimales para su facil comprensión 
    promedio=round(Total/3,2)

    print("")
    #Revisamos si tiene nota aprobatoria o reprobatoria y la imprimimos
    if(promedio >= 70):
        print(f"¡Felicidades! Tu promedio fue de {promedio} por lo que aprobaste")
    else: print(f"Lo siento. Tu promedio fue de {promedio} por lo que reprobaste")

except:
    # en caso de que no se introduzca un numero valido se notifica al usuario 
    print("El programa se ha cerrado por que usaste terminos no validos prueba usando numeros positivos mayores a cero")