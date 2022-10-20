# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18OaJ1Soi56HViffrbVgl79uf3l0i9xW0
"""

# Importando da biblioteca shapely os comandos para criar pontos, linhas e polígonos
from shapely.geometry import Point, LineString, Polygon

point1 = Point(2,5)
point2 = Point(3,8)
point3 = Point(6,11)
point3D = Point(2,4,1)

x1 = Point(point1).x
x2 = Point(point2).x
x3 = Point(point3).x
x3D = Point(point3D).x

y1 = Point(point1).y
y2 = Point(point2).y
y3 = Point(point3).y
y3D = Point(point3D).y

print(f"As coordenadas de X e Y do ponto 1: {x1}, {y1}")

print(f"As coordenadas de X e Y do ponto 2: {x2}, {y2}")

# Distância entre os pontos 1 e 2
dist = point1.distance(point2)
print(f"A distância entre os pontos 1 e 2: {dist}")

# Coordenadas do ponto 1
list(point1.coords)

# Coordenadas do ponto 2
list(point2.coords)

# Coordenadas do ponto 3
list(point3D.coords)

# Tipos de geometrias
point3D.geom_type

from shapely.geometry.multilinestring import linestring
# Trabalhando com Strings de Linhas
line = LineString([point1,point2,point3])

line

# Comparando duas linhas
line2 = LineString([(2,5),(3,8),(6,11)])
line3 = LineString([(2,2),(3,4),(4,6)])

# Iguais
line == line2

# Diferentes
line == line3

line3

# Coordenadas das linhas

list(line.coords)

# Só as coordenadas de x da lina 1
xcoords1 = list(line.coords.xy[0])
ycoords1 = list(line.coords.xy[1])

xcoords1

# Só as coordenadas de y da lina 1
ycoords1

# Tamanho das linhas
len(line.coords)

# Comprimento das linhas

l_line = line.length
l_line3 = line3.length

l_line

l_line3

l_line < l_line3

# Create polygons

pl1 = Polygon([(1,1),(5,4),(9,1)])
pl2 = Polygon([point1, point2, point3])

pl1

pl2

pl1.area

pl2.area

# Use shell in the polygons
border = [(180, -90), (-180, -90),(-180, 90),(180,90)]

world = Polygon( shell = border)

world

# Create frame in the world

hole = [[(170, -80),(-170,-80),(-170, 80),(170, 80)]]

frame = Polygon(shell=border,holes=hole)

print(frame)

frame

# Print outputs

print(f"Polygon Centroid: {world.centroid}")
print(f"Polygon Area: {world.area}")
print(f"Polygon Boudering Box: {world.bounds}")
print(f"Polygon Boudering Exterior: {world.exterior}")
print(f"Polygon Boudering Length: {world.length}")

# Create a cicly

point4 = Point(1,1)

point4.buffer(2)
