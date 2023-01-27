######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Processing Image
    Tiene metodos que retornan matrices para la deteccion de patrones
    en los laberintos.

Colores conforme a los numeros en cada matriz:
    - ' ': Cuadro libre (Cuadro Blanco)
    - '#': Cuadro ocupado (Cuadro Negro)
    - 'r': Punto de inicio (Cuadro Rojo)
    - 'g': Punto de victorio (Cuadro Verde)
"""
######################################################################################

# Try with numpy, pillow

from PIL import Image, ImageFilter
import numpy as np

class SquarePixel():
    def __init__(self, limit_min_x, limit_min_y, limit_max_x, limit_max_y) -> None:
        self.colors = []        
        self.limit_min_x = limit_min_x
        self.limit_min_y = limit_min_y
        self.limit_max_x = limit_max_x
        self.limit_max_y = limit_max_y        

    def add_color(self, color: tuple, x: int, y: int):
        if(x >= self.limit_min_x and x <= self.limit_max_x and y >= self.limit_min_y and y <= self.limit_max_y):
            self.colors.append(color)

    def see_all_colors(self):
        for j in self.colors:
            print(j)

    def get_color(self) -> tuple:
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for colors in self.colors:
            r, g, b = colors        
            sum_r += r
            sum_g += g
            sum_b += b
        elements = len(self.colors)

        color_mean = (int(sum_r / elements), int(sum_g / elements), int(sum_b / elements))

        # Vamos a determinar el color definitivo
        r = color_mean[0]
        g = color_mean[1]
        b = color_mean[2]

        if(r >= 200 and g >= 200 and b >= 200): # Blanco
            return 0 

        if(r <= 50 and g <= 50 and b <= 50): # Negro
            return 1
        
        if(r >= 200 and g <= 50 and b <= 50): # Rojo (Punto de inicio)
            return 3

        if(r <= 50 and g >= 200 and b <= 50): # Verde (Puntos de meta)
            return 4

        return -1

def discretize_image(file_image : str, pixels_square_h = 20, pixels_square_w = 20):
    img = Image.open(file_image)
    img.thumbnail((100, 100))
    img.show()

    # Tamanio
    width = img.size[0]
    height = img.size[1]
    
    # Cantidad de cuadros a dibujar
    amount_square_x = int(width / pixels_square_w)
    amount_square_y = int(height / pixels_square_h)
    
    squares = [] # Almacenar todos los cuadros con sus limites correspondientes
    # Definir limites para cada cuadro de pixeles
    aux_x1 = 0
    aux_y1 = pixels_square_h - 1
    aux_x2 = 0
    aux_y2 = pixels_square_h - 1
    for x in range(amount_square_x):
        for y in range(amount_square_y):
            square_of_pixel = SquarePixel(aux_x1, aux_y1, aux_x2, aux_y2)            
            squares.append(square_of_pixel)
            aux_x2 += pixels_square_w
            aux_y2 += pixels_square_h        
        aux_x1 += pixels_square_w
        aux_y1 += pixels_square_h
        aux_x2 = 0
        aux_y2 = pixels_square_h - 1
    
    # Definir todos los pixeles en los cuadros
    for row in range(width):
        for col in range(height):
            colors = img.getpixel((row, col))
            for s in squares:
                s.add_color(colors, row, col)

    # Obtener el promedio y la matriz de todos los cuadros creados    
    matrix = []
    count = 1
    matrix_aux = []
    for s in squares:
        if count >= amount_square_x:
            matrix.append(matrix_aux)
            count = 0
            matrix_aux = []
        else:
            matrix_aux.append(s.get_color())
        count += 1

    print(matrix)

    return 
