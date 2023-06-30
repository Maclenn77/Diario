#Inicio
import archivo
def inicio():
    opcion = int(input('Presiona (1) para escribir en el diario. \n\nPresiona (2) para leer en el diario.\n\nPresiona (3) para salir.'))
    if opcion == 1:
        archivo.escribir_i()
        inicio()
    elif opcion == 2:
        archivo.leer_todo()
        inicio()
    elif opcion == 3:
        quit()
    else:
        print('Opción no válida')
        inicio()
inicio()
