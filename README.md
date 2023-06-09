# Proyecto 1 de DAA: Los Espías

### Equipo: <team_name>
- Lauren Guerra Hernández C-412
- Dennis Fiallo Muñoz C-411


### Problema
Durante la segunda guerra mundial una parte importante de la información era transmitida en cartas encriptadas en buzones públicos que eran depositadas en estos por espias. Funcionaba de la siguiente manera:

* En la ciudad solo había un buzón usado para temas militares que era compartido para todas estas operaciones.

* En un período dos generales hacían cada uno una lista de órdenes: s y t, de tamaños cualesquiera.

* La lista de órdenes de un general era una secuencia de comandos, cada uno podía ser de enviar información o de ir al buzon a recogerla, Ej:
L1: r,r,e,r L2: e,e,r (para r: recoger y e: enviar)

* Si cuando un espía iba al buzón a recoger información se encontraba varias cartas, solo recogía una.

* Si cuando un espía iba al buzón a recoger información, no encontraba nada, le reportaba al general como un posible caso de información filtrada y se daba la orden de fusilar a todos los implicados.

* Si al finalizar el período quedan cartas en el buzón, un cartero común las lee, y se da un caso de información filtrada y se fusila a todos los implicados también.

Usted es un mediador de paz, por tanto su tarea es construir una lista de órdenes que contenga las listas de los dos generales como subsecuencias, agregando la menor cantidad de órdenes posibles (al principio en el medio o al final), ya sea de enviar o recoger información, de manera que no fusilen a nadie.




### Solución 

La interpretación del problema es la siguiente tenemos dos string $s$ y $t$, conformados únicamente por los caracteres: *e* y *r*. De estos se quiere buscar un algoritmo que dados cualquier $s$ y cualquier $t$ encuentre la menor cadena que contenga como subsecuencias a $s*$ y a $t$ y que además sea una cadena de "paréntesis balanceados". Para facilitar el trabajo y entendimiento del problema se toma a *e* como *"("* y a *r* como *")"*.

Por lo que para que una cadena $q$ sea solución de nuestro problema debe cumplir con las siguientes condiciones:
1- Ser una cadena de "paréntesis balanceados".
2- Ser $s$ una subsecuencia de $q$.
3- Ser *t* una subsecuencia de $q$.
4- Ser la cadena de menor longitud posible que cumpla con las condiciones anteriores.

##### Definiciones
- Sea una subcadena una secuencia de caracteres que aparece de forma consecutiva en una cadena.
- Sea una subsecuencia una secuencia de caracteres que aparece en una cadena, pero no necesariamente de forma consecutiva.
- Sea el factor de desbalance de una cadena la cantidad de "(" que quedan sin cerrar y la cantidad de ")" que aparecen sin haber sido abiertos, por lo cual el factor de desbalance de una cadena representa la cantidad de paréntesis abiertos y cerrados a agregar a esta para que este balanceada. - Si el factor de desbalance es 0, la cadena esta balanceada.

Demostración a través de la construcción de una solución, de que siempre existe una cadena balanceada que que cumple que $s$ y $t$ sean subsecuencias de esta y ademas este balanceada $\Rightarrow$ el problema tiene solución.

Sean $s$ y $t$ cadenas definidas en el lenguaje `("("|")")*` arbitrarias de tamaños $n$ y $m$ respectivamente y sea $q = s + t$ con tamaño $n+m \Rightarrow$ que $s$ y $t$ al ser subcadenas de $q$, son subsecuencias de $q$, pero como $s$ y $t$ no son cadenas balanceadas, no necesariamente $q$ es una cadena balanceada.

Para balancear $q$ se busca su factor de desbalance, para tener la cantidad de  ")" y "(" que deben ser agregados, al ser $q$ de tamaño $n+m \Rightarrow$ factor de desbalance de $q$ siempre es menor o igual que $n + m \Rightarrow$  se tiene la cadena $q$ después de ser balanceada con tamaño $\leq 2(n+m) = 2(q) \Rightarrow q$ es una cadena balanceada que cumple que $s$ y $t$ son subsecuencias de $q$ y ademas $q$ está balanceada $\Rightarrow$ el problema tiene solución y está acotada por $2(q)=2(n+m)$.

Apoyándonos en que siempre existe una cadena $q$ que cumple con 1, 2, 3 el objetivo es buscar la cadena de menor longitud posible.


#### Primera solución
En un principio la primera idea que aparece para resolver el problema es hacer un backtracking que recorra todas las posibles combinaciones de *"("* y *")"* y que encuentre la cadena que cumpla con las condiciones del problema. Para esto se tiene en el archivo `first_solve.py` el método `solve` el cual hace lo siguiente:

- Cuenta con dos métodos auxiliares: `is_valid` y `is_subsequence` que verifican si una cadena es válida y si es subsecuencia respectivamente(esto aparece en el archivo `tools.py` siendo usados por otras soluciones, junto con otro conjunto de herramientas que ahí aparecen).
    - En el caso de la validez se verifica si la cadena resultante es balanceada iterando por esta y contando el número de *"("* sumando $1$ y *")"* restando $1$ que se van encontrando, si al finalizar el recorrido el contador es 0 entonces la cadena es válida, mientras que si en el camino el contador pasa a tener un número negativo esto indica que contiene un *")"* que no tiene un *"("* correspondiente y por lo tanto no es válida.
    - Para verificar si una cadena es subsecuencia de otra se recorre la cadena más grande y se va comparando con la cadena más pequeña, si se encuentra un caracter que no coincide se aumenta el índice de la cadena más grande y se vuelve a comparar, si se llega al final de la cadena más pequeña y no se ha encontrado un caracter que no coincida entonces la cadena más pequeña es subsecuencia de la más grande.

- Este va a generar todas las cadenas posibles desde la cadena vacía hasta las cadenas de longitud $2*(s+t)$ como se demostró anteriormente que siempre existe una solución con tamaño menor o igual que este. En cada iteración se extrae una cadena de la lista y si no supera la longitud máxima se agregan dos nuevas cadenas a la lista formadas por esta cadena agregando al final "(" y ")".

- Cuando una cadena cumple con las condiciones de `is_valid` y `is_subsequence`(de s y de t), se agrega a una lista de soluciones de la cual al final del proceso nos vamos a quedar con todas las soluciones de menor tamaño.

- A pesar de generar correctamente todas las posibles soluciones, este algoritmo es muy ineficiente ya que explora todo el árbol de soluciones hasta $2*(s+t)$, teniendo una complejidad de $O(2^n)$ donde n es el tamaño de la suma de las cadenas *s* y *t*. Por tanto, nos apoyaremos en este para probar algoritmos más eficientes.

#### Segunda solución

En un segundo intento tenemos en el archivo `second_solve.py` en el cual se usa el mismo algoritmo de `first_solve.py` pero haciéndole algunas podas para reducir el tiempo de ejecución. Una primera poda es que si al verificar el factor de balance con el método `is_balanced`(el cual retorna el factor de balance de la cadena, y para el caso de llegar a ser en algún momento menor que cero se retorna $-1$) tenemos que se descartan todos los casos en que se tenga un factor de balance menor que cero pues esto indica que existe un ")" que no tiene un "(" correspondiente y por lo tanto no es una cadena válida y nunca va a poder ser válida. Además, se agrega una segunda poda que es que si la cadena que se está generando tiene una cantidad de "(" mayor o igual que $s+t +1$ entonces se descarta la posibilidad de que aparezca una solución válida pues harían falta $s+t +1$ de ")" para que se balancee la cadena y esto exedería el tamaño máximo de la cadena planteado anteriormente de $2*(s+t)$. Como ya se había comprobado anteriormente que este método genera todas las soluciones posibles, se puede decir que este también las genera pues solo se descartan ramas que no nos llevan a soluciones válidas.

Este se ejecuta igualmente con una complejidad temporal de $O(2^n)$, pero con un tiempo de ejecución más bajo debido a las podas en el árbol de búsqueda.

#### Fuerza bruta

Como tercer interto tenemos el algoritmo que se encuentra en `brute_force.py` es un algoritmo de fuerza bruta que en cada iteración genera para toda $i$ comprendida entre $1$ y $2*(n+m)$ todas las posibles cadenas de longitud $i$ y verifica si entre ellas existe una o varias que cumplan [1], [2] y [3], en este caso se retornan todas las estas cadenas de tamaño $i$ mínimo. Siempre devuelve todas las soluciones de tamaño mínimo porque genera y comprueba las cadenas de forma creciente, nunca va a buscar soluciones de tamaño $i+1$ si no verificó todas las de tamaño $i$.

Su complejidad es $O(2^n)$ donde n es el tamaño de las soluciones encontradas, acotadas superiormente por $2*(n+m)$. Es de esta forma porque en cada iteración se generan todas las posibles cadenas de longitud $i$ ya que por cada cadena de tamaño $i-1$ se genera una cadena de tamaño $i$ agregando un "(" y un ")" al final de la cadena $\Rightarrow$ por cada $i$ se generan $2*i$ cadenas $\Rightarrow$ en $n$ iteraciones se generan $2^n$ cadenas a esto se le debe adicionar el costo de verificar en cada iteración si cada una de estas cadenas es válida y es subsecuencia de $s$ y $t$ $\Rightarrow T(n)=2^n + n^2$ por lo tanto la complejidad total es $O(2^n)$.

Al ser una solución lenta e ineficiente pero que siempre brinda todas las soluciones correctas y en las pruebas demora un menor tiempo que las planteadas anteriormente, nos apoyaremos en ella para probar la correctitud las soluciones de algoritmos más eficientes.



#### Solucion dinámica 1
Una de las primeras soluciones que ideamos para atacar el problema (se encuentra en `dp.py`) utilizando la programación dinámica es la siguiente:
- Crear una matriz $dp$ de tamaño $n+1 \times m+1$ donde $n$ y $m$ son los tamaños de las cadenas $s$ y $t$ respectivamente.
- Colocar en la primera fila y la primera columna las subcadenas del tamaño del índice de la fila o columna respectivamente de la cadena $s$ y $t$.

- Ej: si $s =$ ")(()" y $t =$ "())))" entonces la matriz queda de la siguiente forma:


$$
\begin{pmatrix}
'' & '(' & '()' & '())' & '()))' & '())))'\\
 ')' &''& ''& ''& '' &''\\
 ')(' &'' &'' &'' &'' &''\\
 ')((' &'' &'' &''& ''& ''\\
 ')(()' &'' &'' &'' &'' &''
\end{pmatrix}
$$

En cada posición $i,j$ de la matriz para $i \in [1,n]$ y  $j \in [1,m]$ se va a guardar la menor cadena que cumpla que $s[0:i]$ y $t[0:j]$ son subsecuencias de esta.


Esta cadena está construída a partir de las cadenas que se encuentra en las posiciones $[i-1][j]$ y $[i][j-1]$ de la matriz, de la siguiente forma:

- Se comprueba si la cadena en la posicion $[i-1][j]$ cumple que $t[0:j]$ es subsecuencia de esta, en este caso se guarda como posible cadena seleccionada.
- Igualmente se comprueba que la cadena en la posición $[i][j-1]$ cumple que $s[0:i]$ es subsecuencia de esta, en este caso se guarda como posible cadena seleccionada.
- Luego se guardan para ser seleccionadas las cadenas $dp[i-1][j]+t[j]$  y $dp[i][j-1]+s[i]$ ya que ambas cumplen que $s[0:i]$ y $t[0:j]$ son subsecuencias de esta. Porque si $a$ es subsecuencia de $b =>a+c$ es subsecuencia de $b+c$.
- Teniendo las cadenas guardadas anteriormente se selecciona la o una de las que cumpla que la suma de la cantidad de paréntesis a agregarle para balancearla con su tamaño sea mínima.

Cuando la $dp$ esté completa se retorna la cadena que se encuentra en la posición $[n+1][m+1]$ de la matriz.

Como se puede ver esta función tiene de costo $nm$ al recorrer cada una de las posiciones de la matriz, además del costo de buscar las posibles soluciones a seleccionar la mejor y de estos buscar e iterar por estas soluciones para comprobar si cumplen que s y t hasta los indices i,j respectivamente son subsecuencias de esta,estos procedimientos  teniendo un costo todos estos procesos  $\leq$ max(n,m)   =>*T(n,m)=nm max(m,n)* => *O(nm max(m,n))*.

Este algoritmo es bastante más eficiente que lo que se tenía hasta el momento pero no siempre da la cadena mínima, para muy pocos casos da cadenas erróneas porque no se garantiza que partiendo de un óptimo de $s[i]$ y $t[j]$ se pueda llegar a un optimo de $s$ y $t$.



##### Contraejemplo que demuestra que partiendo de una solucion optima de $s[0:i]$ y $t[0:j]$ no siempre se llega a una solucion óptima de $s$ y $t$.
Se tienen las cadenas:
$s=$ "()())" 
$t=$ "(()))"
$s_{i}=$ "()()"
$t_{j}= $"(())"

Donde $s_{i}$ es prefijo de $s$ y $t_{j}$ es prefijo de $t$.
Una solución óptima de nuestro problema para las cadenas $s_{i}$ y la solución que da "dinamica 1"(método del que hablamos anteriormente) es "(())()()" apoyandose en la cadena anterior, pero la solución correcta para $s$ y $t$ es "(()())" $\Rightarrow$ No se puede garantizar que partiendo de una solución óptima de $s[0:i]$ y $t[0:j]$ se pueda llegar a una solucion optima de $s$ y $t$.



#### Solucion dinámica 2

Para solucionar los problemas del algoritmo anterior se propone un ajuste a esta solución (se encuentra en `dp2.py` ) en el cual en cada espacio de la matriz $dp$ en lugar de estar guardando una cadena óptima, se van a estar guardando todas las cadenas generadas de la misma forma que el algoritmo anterior que tengan a $s[0:i]$ y $t[0:j]$ como subsecuencias (se intentó hacer este algoritmo también guardando todas las cadenas que tenían menor valor del tamaño de la cadena + factor de desbalance e igualmente fallaba en algunos casos). Cuando ya la matriz está completa se balancean todas las cadenas y se elige de todas la menor.

Esto está garantizado, es una solución correcta de nuestro problema porque basicamente lo que hace es buscar todas las posibles cadenas que cumplan [2] y [3] en cada caso y de generar la siguiente cadena a partir de las posibles soluciones anteriores, por lo que se garantiza que se llega a una solución óptima.

Su complejidad es bastante cercana a la del caso inicial de fuerza bruta pero con la ventaja de que no se generan cadenas que no cumplen con [2] y [3]. Si el algoritmo anterior tiene complejidad *O(nm max(m,n))* este tiene por cada espacio de la matriz busca por todas las cadenas que se guardan y a partir de estas genera la siguiente posicion por lo que la complejidad temporal de esta parte es exponencial por lo que es mucho mayor que *O(nm max(m,n))* lo que implica que el algoritmo aunque eficaz es muy lento e ineficiente.

#### Solucion dinámica 3 y Solución Óptima

Luego de un arduo período de trabajo, pruebas e investigaciones hallamos un algoritmo con el que apoyarnos para lograr la solución óptima al problema: *Shortest Common Supersequence*.

Para mejorar las dos soluciones anteriores tanto en efectividad como en complejidad se proponen algunos cambios en la conformación de la matriz $dp$, en cada posición de la matriz $dp[i][j]$ se va a añadir un diccionario en el cual las llaves $b$ van a ser los factores de desbalance con los que se llega a esa posición y los valores asociados a estas llaves serán el tamaño (int) de la menor cadena que cumple 2 y 3 para esas posiciones $i,j$ y tiene factor de desbalance $b$. En este caso específico en el factor de desbalance solamente se están contando los paréntesis abiertos que faltarían por colocarle a la cadena, ya que siempre se tiene en cuenta contar un paréntesis abierto por cada paréntesis cerrado que aparezca y que el factor de desbalance sea $0$.

Por cada $dp[i][j]$ se itera por cada llave del diccionario, por cada $b$ y a partir de esta se generan para la matriz los valores de $dp[i+1][j]$, $dp[i][j+1]$ y $dp[i+1][j+1]$ siguiendo la lógica de tomar los valores de $s[i]$, $t[j]$ o ambos, respectivamente para cada caso y compararlos con *")"*, si esta comparación es true y  el factor de desbalance $b = 0$ se aumenta el tamaño en $2$ y se mantiene $b=0$, si $b>0$ se aumenta en $1$ y $b$ disminuye en $1$ y en caso de que la comparación inicial sea falsa o sea que sea igual a *"("* se aumenta $b$ en $1$ al igual que el tamaño de la cadena, todo esto guardándolos en cada una de las posiciones mencionadas anteriormente. Todos estos valores se guardan si no había un factor de balance igual anterior en esta posición $i,j$ o que sea el mínimo valor de tamaño entre este y el que ya estaba en esa posición.

De esta manera estamos asegurando el recoger tamaños de cadenas válidos que cumplan que $s$ y $t$ sean subsecuencias de la cadena formada y que además sean el mínimo posible. Asegurando (aunque no demostrando) que en la posición $n,m$ de $dp$, la menor suma de $b$,$b \Rightarrow value$ es el tamaño de la menor cadena que resuelve nuestro problema.


Luego que se tiene la longitud de cada cadena resultante y su factor de desbalance procedemos a quedarnos con la cadena de menor tamaño. Como ya se planteó anteriormente solo van a existir saltos entre casillas de la matríz de hasta $2$ máximo. Teníendo esto se comienza por la mejor cadena final ya seleccionada anteriormente y se reconstruye volviendo hacia atrás en el camino teniendo como opción moverse en sentido vertical, horizontal y diagonal como:

- Tener un camino con diferencia de $1$, por tanto ocurre un cambio de balance. Moviéndose en la lista de balances debido al cambio de factoe de balance según el paréntesis que aparezca(si es un *"("* queda $b - 1$ y si es *")"* tenemos $b + 1$). Esto solo es posible cuando el factor de desbalance es mayor que $0$.
- Tener un camino de diferencia $2$, manteniendose la misma posición en la lista de balances con longitudes, pues esto solo ocurre cuando el factor de desbalance es igual a cero y se tiene un *")"*, lo cual indica que no va a exixtir un *"("* para cerrarlo por lo que se agrega en ese punto la cadena "( )" pues la posición en que se agrega el paréntesis no afecta al resultado final.

Como se está contruyendo la cadena de atrás hacia adelante todas las subcadenas que se agregan se ponen al inicio de la cadena actual: *current_string* = *new_string* + *current_string*. Y al finalizar el recorrido se agregan los paréntesis *")"* necesarios según el factor de desbalance que se había planteado al principio.


Para los casos de movernos en distancia de $1$ se agrega el paréntesis correspondiente al lugar del movimiento, mientras que en el otro caso se agrega la cadena "( )" en ese momento el factor de desbalance es $0$ y se tiene un paréntesis cerrado el cual no va a tener paréntesis abierto, y se agrega aquí pues no afecta la posición en la que se agrega el parentesis al resultado final.


La complejidad de este algoritmo es $nm$ a la hora de recorrer toda la tabla generando los tamaños de las futuras cadenas, luego queda recorrer todos los $b$ generados en cada posición de la matriz, como los factores de desbalance nunca serán mayores que el tamaño de la solución y la solución sismpre está acotada por $2(n+m) \Rightarrow$ en cada $i,j$ nunca habrán más de $2(n+m)$  valores de $b$ distintos y $2(n+m)$  es $O(max(n,m)) \Rightarrow T(n,m)= nm 2(n+m)$ y $2(n+m) \Rightarrow T(n)=O(nm max(n,m))$. No se toma en cuenta la complejidad de la construcción de la cadena a través de la matriz porque es mucho menor que la construcción de esta.


**Nota**: Es este último caso se habla de $dp$ como una matríz de diccionarios pero se encuentra implementado como un diccionario de diccionarios, teniendo el primero como llave una tupla que simula las posiciones en una matríz.



### Ejecución

Para ejecutar el proyecto primeramente se debe ejecutar el siguiente comando `pip install -r requirements.txt` para instalar los módulos de Python necesarios para ejecutar el proyecto. 

Los casos de prueba utilizados en el tester se generan en `generator.py` en los cuales se crean cadenas del tamaño especificado de forma totalmente aleatoria, por lo que se generan todos los posibles casos de prueba de nuestro problema.

Luego para correr el test de las soluciones se corre el archivo `testing.py` al cual se le puede hacer `python testing.py -h` y este muestra todas las opciones posibles de prueba, como es el caso de:
- -s: para colocar una semilla para la generación de las cadenas aleatorias.
- -t: para colocar la cantidad de pruebas que se quieren hacer.
- -l: para colocar el tamaño fijo de las cadenas aleatorias.
- -r: para colocar el rango de tamaño de las cadenas aleatorias.
- -m: para seleccionar el método a usar para resolver el problema entre una lista de posibles.



