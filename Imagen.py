import rasterio
import numpy as np
import matplotlib.pyplot as plt
import PIL 
from affine import Affine

class Imagen():
  
  def __init__(self, path = '', nombre = ''):
    self.ruta = ruta
    self.nombre = nombre
   
  def modificar_ruta(self, ruta):
    self.ruta = ruta
    
  def modificar_nombre(self, ruta):
    self.nombre = nombre
   
  def normalizar_8_bits(self, i_dtype):
    potencia = int(i_dtype.replace('uint', ''))
    rgb_normalizado = ((rgb/((2**potencia)-1))*255).astype(np.uint8)
    return = rgb_normalizado
  
  def modificar_coordenadas(self):
    imagen = rasterio.open(self.ruta + self.nombre)
    crs = imagen.crs
    bands = imagen.read()
    new_transform=Affine(1,2,1,1,2,1)
