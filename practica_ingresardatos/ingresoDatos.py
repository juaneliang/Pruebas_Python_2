import re

class IngresoDatos():
    pass 

def soloLetras(stringSoloLetras):
    stringSoloLetras = re.sub('[^a-zA-Z]+', '', stringSoloLetras)
    return stringSoloLetras