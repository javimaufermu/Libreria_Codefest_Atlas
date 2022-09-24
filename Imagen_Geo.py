import rasterio
import numpy as np 
from affine import Affine

# El Proyecto planteado contiene una estructura orientada a objetos para facilitar su uso e importación, 
# principalmente busca la alteración de coordenadas.
class Imagen_Geo():
  
  # Constructor
  def __init__(self, ruta = '', nombre = ''):
    self.ruta = ruta
    self.nombre = nombre
    
  def modificar_ruta(self, ruta):
    self.ruta = ruta
    
  def modificar_nombre(self, ruta):
    self.nombre = nombre
   
  # Función que busca normalizar la resolución de bits a 8 bits 
  #   para comprimir y aumentar la compatibilidad con múltiples librerias (Tiene pérdidas)
  # Retorna las bandas con resolución de bits igual a 8.
  def normalizar_8_bits(self, i_dtype = 'uint16', bandas):
    potencia = int(i_dtype.replace('uint', ''))
    bandas_normalizado = ((bandas/((2**potencia)-1))*255).astype(np.uint8)
    return bandas_normalizado
  
  # En caso de ser necesario, la función 
  # tiene como propósito disminuir la calidad de la imagen y cambiar las coordenadas de la imagen.
  # La función recibe como parámetro de entrada la ruta en la que será guardada la imagen alterada.
  def modificar_coordenadas(self, ruta_guardado = './'):
    imagen = rasterio.open(self.ruta + self.nombre)
    crs = imagen.crs
    bands = imagen.read()
    new_transform=Affine(1,2,1,1,2,1) # Aqui se alteran las coordenadas de la imagen 
                                      #(Por el momento tiene una alteración estática, pero se busca un enfoque de aleatoriedad)
    norm = normalizar_8_bits(imagen.meta['dtype'])
    
    with rasterio.open(ruta_guardado + self.nombre, 'w',
                        driver=imagen.meta['driver'],
                        height=bands.shape[1], width=bands.shape[2], count=bands.shape[0],
                        dtype=bands.dtype, crs=crs, transform=new_transform) as image_transformed:
      
      image_transformed.write(bands) 
   
  
