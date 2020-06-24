# Aplicación del algoritmo de la colonia de hormigas para resolver el problema de reposición de bicicletas en BiciMAD

## Descripción:

TFG del grado en Ingeniería Informática de la UOC, área Inteligencia Artificial, consistente en la implementación del algoritmo de la colonia de hormigas (Ant Colony Optimization) con el fin de encontrar la ruta más corta para la reposición de bicicletas entre las estaciones de BiciMAD. 


## Contenidos:

- Bicimad0618.csv: archivo con los nombres y coordenadas de todas las estaciones de BiciMAD correspondientes a junio de 2018.

- bases_csv.py: carga el csv de las estaciones y les asigna una demanda de bicicletas aleatoria.

- solucion1: solución naive. Ordena las estaciones de mayor excedente a mayor demanda y las recorre en dicho orden.

- solucion2: elige la siguiente estación a visitar aleatoriamente y comprueba que se satisface la demanda.

- solucion3: Ant Colony Optimization. Parámetros ajustables preestablecidos a 1000 hormigas, evaporación = 0.5, alfa = 1, beta = 2.

- Tests para cada solución.


## Ejecución:

Ejecutar cualquiera de las soluciones (posibilidad de ajustar parámetros en solucion3).
Si se desea utilizar otra lista de estaciones, cargar el csv en bases_csv.py.

El resultado es una lista ordenada con el nombre de las estaciones a visitar y la distancia euclidiana de la ruta obtenida.


