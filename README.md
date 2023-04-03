# DAA
 
## Los Espías

#### Problema
Durante la segunda guerra mundial una parte importante de la información era transmitida en cartas encriptadas en buzones públicos que eran depositadas en estos por espias. Funcionaba de la siguiente manera:

* En la ciudad solo había un buzón usado para temas militares que era compartido para todas estas operaciones.

* En un período dos generales hacían cada uno una lista de órdenes: s y t, de tamaños cualesquiera.

* La lista de órdenes de un general era una secuencia de comandos, cada uno podía ser de enviar información o de ir al buzon a recogerla, Ej:
L1: r,r,e,r L2: e,e,r (para r: recoger y e: enviar)

* Si cuando un espía iba al buzón a recoger información se encontraba varias cartas, solo recogía una.

* Si cuando un espía iba al buzón a recoger información, no encontraba nada, le reportaba al general como un posible caso de información filtrada y se daba la orden de fusilar a todos los implicados.

* Si al finalizar el período quedan cartas en el buzón, un cartero común las lee, y se da un caso de información filtrada y se fusila a todos los implicados también.

Usted es un mediador de paz, por tanto su tarea es construir una lista de órdenes que contenga las listas de los dos generales, agregando la menor cantidad de órdenes posibles (al principio en el medio o al final), ya sea de enviar o recoger información, de manera que no fusilen a nadie.




#### Solución 

La interpretación del problema es la siguiente tenemos dos string $s$ y $t$, conformados únicamente por los caracteres: *e* y *r*. De estos se quiere buscar un algoritmo que dados cualquier $s$ y cualquier $t$ encuentre la menor cadena que contenga como subsecuencias a $s*$ y a $t$ y que además sea una cadena de "paréntesis balanceados". Para facilitar el trabajo y entendimiento del problema se toma a *e* como *"("* y a *r* como *")"*.

Por lo que para que una cadena $q$ sea solución de nuestro problema debe cumplir con las siguientes condiciones:
1- Ser una cadena de "paréntesis balanceados".
2- Ser $s$ una subsecuencia de $q$.
3- Ser *t* una subsecuencia de $q$.
4- Ser la cadena de menor longitud posible que cumpla con las condiciones anteriores.

##### Definiciones
- Sea una subcadena una secuencia de caracteres que aparece de forma consecutiva en una cadena.
- Sea una subsecuencia una secuencia de caracteres que aparece en una cadena, pero no necesariamente de forma consecutiva.
- Sea el factor de desbalance de una cadena la cantidad de "(" que quedan sin cerrar y la cantidad de ")" que aparecen sin haber sido abiertos, por lo cual el factor de desbalance de una cadena representa la cantidad de parentesis abiertos y cerrados a agregar a esta para que este balanceada. - Si el factor de desbalance es 0, la cadena esta balanceada.

Demostración a traves de la construcción de una solución, de que siempre existe una cadena balanceada que que cumple que $s$ y $t$ sean subsecuencias de esta y ademas este balanceada $\Rightarrow$ el problema tiene solución.

Sean $s$ y $t$ cadenas definidas en el lenguaje `("(",")")*` arbitrarias de tamaños $n$ y $m$ respectivamente y sea $q = s + t$ con tamaño $n+m \Rightarrow$ que $s$ y $t$ al ser subcadenas de $q$, son subsecuencias de $q$, pero como $s$ y $t$ no son cadenas balanceadas, no necesariamente $q$ es una cadena balanceada.

Para balancear $q$ se busca su factor de desbalance, para tener la cantidad de  ")" y "(" que deben ser agregados, al ser $q$ de tamaño $n+m \Rightarrow$ factor de desbalance de $q$ siempre es menor o igual que $n + m \Rightarrow$  se tiene la cadena $q$ después de ser balanceada con tamaño $\leq 2(n+m) = 2(q) \Rightarrow q$ es una cadena balanceada que cumple que $s$ y $t$ son subsecuencias de $q$ y ademas $q$ está balanceada $\Rightarrow$ el problema tiene solución y está acotada por $2(q)=2(n+m)$.

Apoyándonos en que siempre existe una cadena $q$ que cumple con 1, 2, 3 el objetivo es buscar la cadena de menor longitud posible.

#### Soluciones

En un principio la primera idea que se nos ocurre para resolver el problema es hacer un backtracking que recorra todas las posibles combinaciones de *"("* y *")"* y que encuentre la cadena que cumpla con las condiciones del problema. Para esto se tiene en el archivo `first_solve.py` el método `solve` el cual hace lo siguiente:

- Cuenta con dos métodos auxiliares: `is_valid` y `is_subsequence` que verifican si una cadena es válida y si es subsecuencia respectivamente(esto aparece en el archivo `tools.py` siendo usados por otras soluciones, junto con otro conjunto de herramientas que ahí aparecen).
    - En el caso de la validez se verifica si la cadena resultante es balanceada iterando por esta y contando el número de *"("* sumando $1$ y *")"* restando $1$ que se van encontrando, si al finalizar el recorrido el contador es 0 entonces la cadena es válida, mientras que si en el camino el contador pasa a tener un número negativo esto indica que contiene un *")"* que no tiene un *"("* correspondiente y por lo tanto no es válida.
    - Para verificar si una cadena es subsecuencia de otra se recorre la cadena más grande y se va comparando con la cadena más pequeña, si se encuentra un caracter que no coincide se aumenta el índice de la cadena más grande y se vuelve a comparar, si se llega al final de la cadena más pequeña y no se ha encontrado un caracter que no coincida entonces la cadena más pequeña es subsecuencia de la más grande.

- Este va a generar todas las cadenas posibles desde la cadena vacía hasta las cadenas de longitud $2*(s+t)$ como se demostró anteriormente que siempre existe una solución con tamaño menor o igual que este. En cada iteración se extrae una cadena de la lista y si no supera la longitud máxima se agregan dos nuevas cadenas a la lista formadas por esta cadena agregando al final "(" y ")".

- Cuando una cadena cumple con las condiciones de `is_valid` y `is_subsequence`(de s y de t), se agrega a una lista de soluciones de la cual al final del proceso nos vamos a quedar con todas las soluciones de menor tamaño.

- A pesar de generar correctamente todas las posibles soluciones, este algoritmo es muy ineficiente ya que explora todo el árbol de soluciones hasta $2*(s+t)$, teniendo una complejidad de $O(2^n)$ donde n es el tamaño de la suma de las cadenas *s* y *t*. Por tanto, nos apoyaremos en este para probar algoritmos más eficientes.


En un segundo intento tenemos en el archivo `second_solve.py` en el cual se usa el mismo algoritmo de `first_solve.py` pero haciéndole algunas podas para reducir el tiempo de ejecución. Una primera poda es que si al verificar el factor de balance con el método `is_balanced`(el cual retorna el factor de balance de la cadena, y para el caso de llegar a ser en algún momento menor que cero se retorna $-1$) tenemos que se descartan todos los casos en que se tenga un factor de balance menor que cero pues esto indica que existe un ")" que no tiene un "(" correspondiente y por lo tanto no es una cadena válida y nunca va a poder ser válida. Además, se agrega una segunda poda que es que si la cadena que se está generando tiene una cantidad de "(" mayor o igual que $s+t +1$ entonces se descarta la posibilidad de que aparezca una solución válida pues harían falta $s+t +1$ de ")" para que se balancee la cadena y esto exedería el tamaño máximo de la cadena planteado anteriormente de $2*(s+t)$. Como ya se había comprobado anteriormente que este método genera todas las soluciones posibles, se puede decir que este también las genera pues solo se descartan ramas que no nos llevan a soluciones válidas.

Este se ejecuta igualmente con una complejidad temporal de $O(2^n)$, pero con un tiempo de ejecución más bajo debido a las podas en el árbol de búsqueda.

#### Ejecución

Para ejecutar el proyecto primeramente se debe ejecutar el siguiente comando `pip install -r requirements.txt` para instalar los módulos de Python necesarios para ejecutar el proyecto. 

Luego para correr el test de las soluciones se corre el archivo `testing.py` al cual se le puede hacer `python testing.py -h` y este muestra todas las opciones posibles de prueba, como es el caso de:
- -s: para colocar una semilla para la generación de las cadenas aleatorias.
- -t: para colocar la cantidad de pruebas que se quieren hacer.
- -l: para colocar el tamaño fijo de las cadenas aleatorias.
- -r: para colocar el rango de tamaño de las cadenas aleatorias.
- -m: para seleccionar el método a usar para resolver el problema entre una lista de posibles.




<!-- Para resolver el problema se toma como base el algoritmo de Longest Common Subsequence (LCS) que es un algoritmo de programación dinámica que encuentra la subsecuencia más larga común entre dos cadenas. Este algoritmo se puede encontrar en la [Wikipedia](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) y en [GeeksforGeeks](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/). -->

