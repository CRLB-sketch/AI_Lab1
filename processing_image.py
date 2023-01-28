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

def discretize_image(file_image : str, square_pixels = 20):
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
            if(len(aux_pixels) >= square_pixels):
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
            if(len(aux_pixels) >= square_pixels):
                pixel_mean = get_color_mean(aux_pixels)
                matrix_column.append(pixel_mean)
                aux_pixels = []
            # Se guardara todos los pixeles en un listado auxiliar
            else:                
                aux_pixels.append(pixel)
        matrix.append(matrix_column)
        
    matrix, matrix_nums = matrix_redefine_colors(matrix)
    create_img_solution(matrix, img.size[0], img.size[1])
    return matrix_nums

def get_color_mean(pixels : list):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    
    for colors in pixels:
        # r, g, b = colors
        sum_r += colors[0]
        sum_g += colors[1]
        sum_b += colors[2]
        
    elements = len(pixels)        
    return (int(sum_r / elements), int(sum_g / elements), int(sum_b / elements))

def matrix_redefine_colors(matrix : list):
    matrix_def_colors = []
    matrix_with_numbers = []
    for x in range(len(matrix)):
        matrix_column_c = []
        matrix_column_n = []
        for y in range(len(matrix[0])):
            r, g, b = matrix[x][y]
            
            if(r >= 250 and g <= 210 and b <= 210): # Color Rojo
                color = (255, 0, 0)
                matrix_column_c.append(color)
                matrix_column_n.append(2)
                
            elif(r <= 210 and g >= 250 and b <= 210): # Color Verde
                color = (0, 255, 0)
                matrix_column_c.append(color)
                matrix_column_n.append(3)
            
            elif(r <= 140 and g <= 140 and b <= 140): # Color Negro
                color = (0, 0, 0)
                matrix_column_c.append(color)
                matrix_column_n.append(1)
                
            elif(r >= 140 and g >= 140 and b >= 140): # Color Blanco
                color = (255, 255, 255)
                matrix_column_c.append(color)
                matrix_column_n.append(0)
                                
            else: # Por si el color no es valido vamos a verificar
                print(f"=====> {r}, {g}, {b}")
                color = (0, 0, 255)
                matrix_column_c.append(color)
                matrix_column_n.append(-1)
                
        matrix_def_colors.append(matrix_column_c)        
        matrix_with_numbers.append(matrix_column_n)
        
    return matrix_def_colors, matrix_with_numbers

def create_img_solution(matrix : list, w : int, h : int):
    data = np.zeros((h, w, 3), dtype=np.uint8)
    
    # Vamos a procesar toda la data para crear la imagen
    size_square = len(matrix)
    aux_x1 = 0
    aux_y1 = size_square
    aux_x2 = 0
    aux_y2 = size_square

    # Esto ya sería despues de que se obtenga el promedio de los colores para forma la matriz ya optimizada
    for i in range(size_square):    
        for j in range(size_square):
            r, g, b = matrix[i][j]
            data[aux_x1: aux_y1, aux_x2: aux_y2] = [r, g, b]
            aux_x2 += size_square
            aux_y2 += size_square        
        # Sumar aux 1
        aux_x1 += size_square
        aux_y1 += size_square
        # Resetear aux 2
        aux_x2 = 0
        aux_y2 = size_square

    square_img = Image.fromarray(data)    
    img = Image.fromarray(data, 'RGB')
    img.save('img/testing.png')
    img.show()
    