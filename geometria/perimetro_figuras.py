"""
Esta la libreria de areas de figuras geometricas
autor: DC
observaciones:
"""
from math import pi, pow

def pcirculo(radio):
    perimetro = 2*radio*pi
    print('El area del circulo de radio {:.3f} es {:.3f}'.format(radio, perimetro))
    return perimetro
