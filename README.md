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

# Implementación
## Backend

## Procesamiento
  Se utiliza bloques para procesar las imagenes. Cada 1000 imagenes procesadas se sube al archivo en memoria secundaria y se limpia el diccionaria para mejorar el rendimiento y la velocidad de procesamiento. Aproximadamente toma 10 a 15 min.

## Sequential
   Para el **`range_search()`**, se utilizó comparaciones con las distancias euclidianas obtenidas por **`numpy.linalg.norm()`**, con una busqueda secquencial en todas las imagenes procesadas de la colección.
   Para el **`knn_search()`**, se utilizó una cola de prioridad. En la que insertamos todos los elementos de la colección (ordenandolos por su distancia) y seleccionamos los K elementos con las distancias más pequeñas a la imagen de entrada. (query)

## R-tree
Para aprovechar al máximo el R-tree en Python, utilizamos *`idx.intersect`* y   *`idx.nearest`* * para la búsqueda por rango y para encontrar los vecinos más cercanos (knn), respectivamente. Aquí, idx representa el índice que se usa de manera adecuada.

En el caso de los vecinos más cercanos, devolvemos la ruta de la imagen y un 'dist' que representa el vector característico de la imagen.

En cuanto a la búsqueda por rango con el R-tree, su implementación no es directa, ya que es necesario crear un MBR (Minimum Bounding Rectangle) para restar y sumar las 128 dimensiones.
 
## KDtree
   Para mejorar la facilidad en la carga de los datos los vectores representativos de 128 dimensiones se guardaron en un csv. Este archivo solo se creará y procesa la primera vez y posteriores llamadas solo se cargaran a un dataframe de pandas. Después solo usaremos la función KDTree(temp1.iloc[:, 0:-1]) para cargar el csv. Para hallar los k vecinos más cercanos con sus respectivas distancias usaremos la función dist, ind = tree.query(face_encoding,k). Por último el algoritmo devolverá una lista de  tuplas que contendrán las distancias y la dirección de la imagen encontrada.

## Frontend

# Maldición de la dimensionalidad
La ampliación del número de dimensiones puede intensificar considerablemente muchos de los desafíos que ya se presentan en dimensiones menores, un fenómeno conocido como la "maldición de la dimensionalidad". Esto es especialmente evidente al calcular los KNN o vecinos más cercanos, ya que las distancias generadas pueden hacer que los valores parezcan similares. Una solución para mitigar este problema es disponer de un mayor volumen de datos y reducir la cantidad de dimensiones.

## KD-Tree
El KD-Tree es una estructura de datos que divide el espacio para organizar puntos en un espacio de múltiples dimensiones (k-dimensiones). Este árbol es valioso para usos como la búsqueda por rango y la identificación del vecino más cercano, que son parte de la meta de nuestro proyecto. Utilizando la biblioteca sklearn, podemos acceder a nuestra estructura de datos KDTree. Mediante la función query(imagen, k), podemos determinar los k vecinos más próximos a la imagen especificada. Todo este proceso se realiza comparando las 128 dimensiones previamente representadas con la ayuda de la biblioteca face_recognition.

## Análisis y discusión
Los tests demuestran que las consultas indexadas en Rtree y KDTree son considerablemente más eficaces que las consultas secuenciales, lo que significa que no nos vemos afectados por la maldición de la dimensionalidad en comparación con las implementaciones secuenciales. Finalmente, hemos logrado implementar el proyecto que devuelve los rostros más similares en nuestra base de datos para cualquier consulta introducida.
