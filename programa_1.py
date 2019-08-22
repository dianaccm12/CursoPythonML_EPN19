"""
Este script hace ........
Autor: LGFE
Fecha: 06/06/06
"""

#%%
import numpy as np
from geometria import area_figuras, perimetro_figuras


import pandas as pd

#%%


# def hipotenusa(cateto_1, cateto_2):
#     """
#     Esta funcion calcula la hipo de un triag rect
#     :param cateto_1:
#     :param cateto_2:
#     :return:
#     """
#     hip = sqrt(cateto_1**2+cateto_2**2)
#     return hip

def main():

   area_circulo1 = area_figuras.circulo(radio=5.0)
   area_rectangulo1 = area_figuras.rectangulo(lado1=3, lado2=4.)
   area_triangulo1 = area_figuras.triangulo(base=0.58, altura=1.12)
   perimetro_circulo1 = perimetro_figuras.pcirculo(radio=3)
   perimetro_circulo2 = perimetro_figuras.pcirculo(radio=5)

   # print('Area del circulo de radio 5 es: {}'.format(area_circulo1))
   # print('Area del rectangulo de lados 3 y 4 es: {}'.format(area_rectangulo1))


if __name__ == '__main__':
    main()


