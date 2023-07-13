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

- [Experimentación](#Experimentación)
   * [Análisis y discusión](#Análisis-y-discusión)


# Cuadro de Actividades:

<table>
  <tbody>
    <tr>
      <th>Lista de actividades realizadas</th>
      <th align="center">Responsable</th>
    </tr>
    <tr>
      <td>Implementación de la función range_search y knn para el Rtree </td>
      <td align="center">Nincol Quiroz</td>
    </tr>
    <tr>
      <td>Implementación de la función preprocesamiento</td>
      <td align="center">Franco Pacheco</td>
    </tr>
    <tr>
      <td>Implementación de la función range_search y knn secuencial</td>
      <td align="center">Fabian Alvarado</td>
    </tr>
    <tr>
      <td>Implementación del Frontend</td>
      <td align="center">Franco Pacheco</td>
    </tr>
    <tr>
      <td>Escritura del informe</td>
      <td align="center">Fabian Alvarado y Albert Loayza</td>
    </tr>
    <tr>
      <td>Implementación de la función knn para el KDtree </td>
      <td align="center">Albert Loayza</td>
    </tr>
  </tbody>
</table>

# Cuadro de Participación:

<table>
  <tbody>
    <tr>
      <th>Integrantes</th>
      <th align="center">Participación</th>
    </tr>
    <tr>
      <td>Albert Loayza</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Nincol Quiroz</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Franco Pacheco</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td>Fabian Alvarado</td>
      <td align="center">100%</td>
    </tr>
  </tbody>
</table>


# Introducción:
- El reconocimiento facial es una analizador facial capaz de identificar o verificar a un sujeto a través de una imagen, vídeo o cualquier elemento audiovisual de su rostro. En este proyecto usaremos las librerías necesarias del procesamiento de imágenes en la cual crearemos un programa que reconozca el rostro de una imagen y devuelve los rostros más similares en comparación a nuestra query o consulta.

## Librerías:
### Face Recognition
- La identificación facial es un método que permite confirmar o determinar la identidad de un individuo a través de su rostro. Los sistemas de identificación facial pueden aplicarse para reconocer personas en imágenes, vídeos o en tiempo real. En este proyecto, mediante el uso de bibliotecas específicas para el procesamiento de imágenes, desarrollaremos una aplicación que pueda identificar la cara en una imagen y encontrar las caras más similares dentro de una base de datos.

### RTree
- Esta biblioteca emplea un RTree que indexa los vectores distintivos de las imágenes. La estructura que se ha implementado en esta biblioteca está optimizada para abordar eficientemente el problema de localizar los vecinos más próximos.

### KD-Tree
- El KD-Tree es una estructura de datos que divide el espacio para organizar puntos en un espacio de múltiples dimensiones (k-dimensiones). Este árbol es valioso para usos como la búsqueda por rango y la identificación del vecino más cercano, que son parte de la meta de nuestro proyecto. Utilizando la biblioteca sklearn, podemos acceder a nuestra estructura de datos KDTree. Mediante la función query(imagen, k), podemos determinar los k vecinos más próximos a la imagen especificada. Todo este proceso se realiza comparando las 128 dimensiones previamente representadas con la ayuda de la biblioteca face_recognition.

# Implementación
## Backend

### Procesamiento
- Se utiliza bloques para procesar las imagenes. Cada 1000 imagenes procesadas se sube al archivo en memoria secundaria y se limpia el diccionaria para mejorar el rendimiento y la velocidad de procesamiento. Aproximadamente toma 10 a 15 min.

### Sequential
- Para el **`range_search()`**, realiza una búsqueda por rango en un diccionario de rostros codificados. Primero, carga la imagen de entrada y obtiene las codificaciones del rostro utilizando la biblioteca face_recognition. Luego, compara estas codificaciones con las del diccionario indexado utilizando operaciones de álgebra lineal de la biblioteca numpy. Si la distancia entre las codificaciones es menor que un radio de búsqueda dado, se considera que los rostros son similares y se agregan a los resultados de búsqueda.

- Para el **`knn_search()`**, ealiza una búsqueda k-NN en el diccionario de rostros codificados. Al igual que en la búsqueda por rango, carga la imagen de entrada y obtiene las codificaciones del rostro. Luego, calcula la distancia entre las codificaciones y las almacena en una cola de prioridad. La cola de prioridad se ordena en función de la distancia, de modo que los vecinos más cercanos tienen una mayor prioridad. Finalmente, extrae los k vecinos más cercanos de la cola de prioridad y los devuelve como resultados de búsqueda.


### R-tree
- Para aprovechar al máximo el R-tree en Python, utilizamos *`idx.intersect`* y   *`idx.nearest`* * para la búsqueda por rango y para encontrar los vecinos más cercanos (knn), respectivamente. Aquí, idx representa el índice que se usa de manera adecuada.

- En el caso de los vecinos más cercanos, devolvemos la ruta de la imagen y un 'dist' que representa el vector característico de la imagen.

- En cuanto a la búsqueda por rango con el R-tree, su implementación no es directa, ya que es necesario crear un MBR (Minimum Bounding Rectangle) para restar y sumar las 128 dimensiones.
 
### KDtree
- Para mejorar la facilidad en la carga de los datos los vectores representativos de 128 dimensiones se guardaron en un csv. Este archivo solo se creará y procesa la primera vez y posteriores llamadas solo se cargaran a un dataframe de pandas. Después solo usaremos la función KDTree(temp1.iloc[:, 0:-1]) para cargar el csv. Para hallar los k vecinos más cercanos con sus respectivas distancias usaremos la función dist, ind = tree.query(face_encoding,k). Por último el algoritmo devolverá una lista de  tuplas que contendrán las distancias y la dirección de la imagen encontrada.

## Frontend

## Maldición de la dimensionalidad
- La ampliación del número de dimensiones puede intensificar considerablemente muchos de los desafíos que ya se presentan en dimensiones menores, un fenómeno conocido como la "maldición de la dimensionalidad". Esto es especialmente evidente al calcular los KNN o vecinos más cercanos, ya que las distancias generadas pueden hacer que los valores parezcan similares. Una solución para mitigar este problema es disponer de un mayor volumen de datos y reducir la cantidad de dimensiones.

## Experimentación
- Para testear las implementaciones, se usa una imagen de Tom Cruise como query. Mostraremos el tiempo que demora para 100,200,400,800,1600,3200,6400,12800 datos.

![image](https://github.com/Fabian9533/BD2-P3/assets/56895239/31ee48cf-c208-4f93-92d8-f77477a91e03)

![image](https://github.com/Fabian9533/BD2-P3/assets/56895239/e1c4ef67-21db-4613-a63b-05fc85a4361a)


## Análisis y discusión
- Los tests demuestran que las consultas indexadas en Rtree y KDTree son considerablemente más eficaces que las consultas secuenciales, lo que significa que no nos vemos afectados por la maldición de la dimensionalidad en comparación con las implementaciones secuenciales. Finalmente, hemos logrado implementar el proyecto que devuelve los rostros más similares en nuestra base de datos para cualquier consulta introducida.
