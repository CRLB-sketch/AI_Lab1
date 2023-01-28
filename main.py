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

def graph_search_lab(image_lab : str, size_square : int):
    # 1) Obtener la imagen, leer si contenido y Discretizar la imagen
    matrix_discreted_image = processing_image.discretize_image(image_lab, size_square)
    print(matrix_discreted_image)

    # 3) Usar interfaz generica o clase abstracta para reprsentar el framework el problema formal
    # Para esta clase que se vaya a crear, debe recibir com parametro la construccion de la matriz obtenida
    # Esta clase ayudara a deducir las demas funciones del framework:
    # actions(s), stepCost(s, a, s'), etc.

    # 4) Construir el algoritmo generico (familia = de graphSearch)
    # Recibira como parametrouna instancia del framework de problemas.
    #   -> Breadh First Search (BFS)
    #   -> Depth First search (DFS)
    #   -> A* escojer dos heuristicas distintas y justificar la eleccion realizada
    
    # 5) Construccion de Salida: En este punto se debe de resolver el laberinto
    # Luego se debe de mostrar en pantalla graficamente el camino encontrado
    # La representacion se basara en la matriz discrta

    return

if __name__ == "__main__":
    print(f'{"":#^100}')
    print(f'{" Inteligencia Artificial - Laboratorio 1 ":#^100}')

    # graph_search_lab("img/test1.png", 20)
    graph_search_lab("img/test2.png", 25)
    
    print(f'{"":#^100}')
