#Importa funciones de tiempo para imprimir en el texto

#Función que imprime la fecha local
from time import strftime
from fecha import fcarta
 
#Escribe al final del archivo diario
def escribir_p(x):
    diario = open(strftime('%Y%m%d.txt'), 'a')
    if x == 'Hasta luego.':
        diario.close
    else:
        diario.write(x+'\n')
        x = input('Nuevo párrafo: \n')
        diario.close()
        escribir_p(x)
        
def escribir_i():
    diario = open(strftime('%Y%m%d.txt'), 'w+')
    diario.write(fcarta()+'\n')
    diario.write(str(input('Escribe en tu diario. Para salir, escribe (Hasta luego.).: \n \n'))+'\n')
    diario.close()
    x = input('Nuevo párrafo: \n')
    escribir_p(x)
    
#Lee todo el archivo
def leer_todo():
    print('¿De qué fecha quieres leer tu diario?')
    year = str(input('Año (AAAA): '))
    mes = str(input('Mes (MM): '))
    dia = str(input('Día (01-31): '))
    diario = open(year+mes+dia+".txt", 'r')
    for line in diario:
        print(line)
    diario.close()
