#Inicio
import archivo
def inicio():
    x = int(input('Presiona (1) para escribir en el diario. \n\nPresiona (2) para leer en el diario.\n\nPresiona (3) para salir.'))
    if x == 1:
        archivo.escribir_i()
        inicio()
    elif x == 2:
        archivo.leer_todo()
        inicio()
    elif x == 3:
        quit()
    else:
        print('Opción no válida')
        inicio()
inicio()
