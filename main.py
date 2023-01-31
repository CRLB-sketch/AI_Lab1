######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Main: Clase Principal

Este se encargara de unir todas las clases.
"""
######################################################################################

import processing_image

from algorithms_search import *
from frameworks import Labyrinth

def graph_search_lab(image_lab : str, size_square : int):
    # Vamos a discretizar la imagen    
    print("Discretizando imagen...")
    matrix_discreted_image = processing_image.discretize_image(image_lab, size_square)
    
    # Guardar imagen de la matriz creada    
    print("Matriz e imagen guardada como 'img/preview.png'")
    processing_image.save_img_matrix(matrix_discreted_image, "img/preview.png")
    
    # Vamos a crear el framework tipo Laberinto
    print("Analizando Laberinto...")    
    labyrinth = Labyrinth(matrix_discreted_image)
    
    # Vamos a seleccionar un tipo de problema
    print("Utilizando algoritmo establezido...")
    solution = bfs(labyrinth) # ! Desde aqui se puede cambiar el algoritmo deseado
    
    # Al final vamos a mostrar el resultado esperado
    processing_image.save_img_matrix(solution, "img/solution.png")
    print("El proceso se llevo de forma exitosa :D")
    
if __name__ == "__main__":
    print(f'{"":#^100}')
    print(f'{" Inteligencia Artificial - Laboratorio 1 ":#^100}')

    # graph_search_lab("img/test1.png", 20)
    graph_search_lab("img/test2.png", 25)
    
    print(f'{"":#^100}')
