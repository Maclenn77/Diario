#Módulo con funciones de fechas en español
#Función que expresa la fecha en formato de carta
from time import strftime
import locale

def fcarta():
    loc = locale.getlocale()[0]
    locale.setlocale(locale.LC_TIME, loc) # Establece fecha local
    return strftime('A %A, %d de %B de %Y:')
#Crea un archivo nombrado con la fecha de hoy
def farchivo():
    archivo = open(strftime('%Y%m%d.txt'), 'w+')
    
