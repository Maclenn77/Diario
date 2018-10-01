#Módulo con funciones de fechas en español
#Función que expresa la fecha en formato de carta
def fcarta():
    from time import strftime
    import locale
    locale.setlocale(locale.LC_TIME, "es-MX") # Establece fecha local
    return strftime('A %A, %d de %B de %Y:')
#Crea un archivo nombrado con la fecha de hoy
def farchivo():
    from time import strftime
    import locale
    archivo = open(strftime('%Y%m%d.txt'), 'w+')
    
