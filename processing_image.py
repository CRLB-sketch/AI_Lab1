######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Processing Image
    Tiene metodos que retornan matrices para la deteccion de patrones
    en los laberintos.

Colores conforme a los numeros en cada matriz:
    - '0': Cuadro libre (Cuadro Blanco)
    - '1': Cuadro ocupado (Cuadro Negro)
    - '2': Punto de inicio (Cuadro Rojo)
    - '3': Punto de victorio (Cuadro Verde)
"""
######################################################################################

# Try with numpy, pillow

from PIL import Image, ImageFilter
import numpy as np

def discretize_image(file_image : str, pixels_square_h = 20, pixels_square_w = 20):
    img = Image.open(file_image)
    pixels = img.load()

    # Tamanio
    width = img.size[0]
    height = img.size[1]
                        
    # Vamos a llevar a cabo la suma de los pixeles
    matrix = []
    for x in range(width):
        matrix_column = []
        aux_pixels = []
        for y in range(height):
            pixel = pixels[x, y]
            # Se llevara a cabo la suma y promedios de los colores para luego guardarlo en la matriz
            if(len(aux_pixels) >= pixels_square_h):
                pixel_mean = get_color_mean(aux_pixels)
                matrix_column.append(pixel_mean)
                aux_pixels = []
            # Se guardara todos los pixeles en un listado auxiliar
            else:                
                aux_pixels.append(pixel)
        matrix.append(matrix_column)
        
    # Revertir valores para obtener el promedio de los colores pendientes
    matrix_zip = zip(*matrix)
    matrix_zip_list = list(matrix_zip)
        
    # Vamos a obtener los promedios pendientes
    pixels = matrix_zip_list
    matrix = []
    for x in range(len(matrix_zip_list)):
        matrix_column = []
        aux_pixels = []
        for y in range(len(matrix_zip_list[0])):
            pixel = pixels[x][y]
            if(len(aux_pixels) >= pixels_square_h):
                pixel_mean = get_color_mean(aux_pixels)
                matrix_column.append(pixel_mean)
                aux_pixels = []
            # Se guardara todos los pixeles en un listado auxiliar
            else:                
                aux_pixels.append(pixel)
        matrix.append(matrix_column)
        
    print(matrix)
    print(len(matrix))
    print(len(matrix[0]))
    return 

def get_color_mean(pixels : list):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    
    for colors in pixels:
        r, g, b = colors
        sum_r += r
        sum_g += g
        sum_b += b
        
    elements = len(pixels)        
    return (int(sum_r / elements), int(sum_g / elements), int(sum_b / elements))

def create_img_solution(matrix : list, w : int, h : int):
    data = np.zeros((h, w, 3), dtype=np.uint8)
    
    # Vamos a procesar toda la data para crear la imagen
    
    # Crear la imagen
    img = Image.fromarray(data, 'RGB')
    img.show()
    return
    