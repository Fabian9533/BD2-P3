# BD2-P3
# **Integrantes**
* Fabian Martin Alvarado Vargas
* Franco Pacheco Espino
* Johannes Albert Segundo Loayza Huaman
* Nincol Abraham Quiroz Maquin

# Tabla de contenido
- [Cuadro de Actividades](#Cuadro-de-Actividades)
- [Cuadro de Participación](#Cuadro-de-Participación)
- [Introducción](#Introducción)
- [Librerías](#Librerías)
    * [Face Recognition](#Face-Recognition)
    * [Rtree](#Rtree)
    * [KD-Tree](#KD-Tree)
- [Implementación](#Implementación)
    * [Backend](#Backend)
    * [Frontend](#Frontend)
- [Maldición de la dimensionalidad](#Maldición-de-la-dimensionalidad)

# Introducción:
El reconocimiento facial es una analizador facial capaz de identificar o verificar a un sujeto a través de una imagen, vídeo o cualquier elemento audiovisual de su rostro. En este proyecto usaremos las librerías necesarias del procesamiento de imágenes en la cual crearemos un programa que reconozca el rostro de una imagen y devuelve los rostros más similares en comparación a nuestra query o consulta.

# Librerías:
## Face Recognition
La identificación facial es un método que permite confirmar o determinar la identidad de un individuo a través de su rostro. Los sistemas de identificación facial pueden aplicarse para reconocer personas en imágenes, vídeos o en tiempo real. En este proyecto, mediante el uso de bibliotecas específicas para el procesamiento de imágenes, desarrollaremos una aplicación que pueda identificar la cara en una imagen y encontrar las caras más similares dentro de una base de datos.

## RTree
Esta biblioteca emplea un RTree que indexa los vectores distintivos de las imágenes. La estructura que se ha implementado en esta biblioteca está optimizada para abordar eficientemente el problema de localizar los vecinos más próximos.

## KD-Tree
El KD-Tree es una estructura de datos que divide el espacio para organizar puntos en un espacio de múltiples dimensiones (k-dimensiones). Este árbol es valioso para usos como la búsqueda por rango y la identificación del vecino más cercano, que son parte de la meta de nuestro proyecto. Utilizando la biblioteca sklearn, podemos acceder a nuestra estructura de datos KDTree. Mediante la función query(imagen, k), podemos determinar los k vecinos más próximos a la imagen especificada. Todo este proceso se realiza comparando las 128 dimensiones previamente representadas con la ayuda de la biblioteca face_recognition.
