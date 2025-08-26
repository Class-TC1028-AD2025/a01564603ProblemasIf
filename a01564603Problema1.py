"""
Evento Juvenil: Para personas de 13 a 17 años (inclusive).

Evento para Adultos: Para personas de 18 años o más.

Evento Familiar: Para todas las edades.
"""
try:
    #preguntamos su edad en enteros y la guardamos en la variable edad 
    edad=int(input("Cuántos años tienes: "))
    print("")
    #verificamos si es menor de 13 
    if(edad<13):
        print("Lo siento, no puedes asistir a los eventos con restricción de edad. Solo al Evento Familiar.")
    #Si es mayor de trece revisamos que sea menor a 18 
    elif(edad<18):
        print("Puedes asistir al Evento Juvenil y al Evento Familiar.")
    #Si es mayor de 18 ya no hace falta hacer más verificaciones
    else: print("Puedes asistir al Evento para Adultos y al Evento Familiar.")
except:
    #en caso de que no se introduzca un entero se le notifica al usuario 
    print("El programa se ha cerrado por que usaste terminos no validos prueba usando numeros enteros")