
#####Solucion dinamica 1
Una de las primeras soluciones que ideamos para atacar el problema es la siguiente:
- Crear una matriz dp de tamaño $n+1 \times m+1$ donde $n$ y $m$ son los tamaños de las cadenas *s* y *t* respectivamente.
- Llenar la primera fila y la primera columna con las subcadenas del tamanno del indice de la fila o columna respectivamente de la cadena *s* y *t*.
ej: si s = ")(()" y t = "())))" entonces la matriz queda de la siguiente forma:


$$
\begin{pmatrix}
'' & '(' & '()' & '())' & '()))' & '())))'\\
 ')' &''& ''& ''& '' &''\\
 ')(' &'' &'' &'' &'' &''\\
 ')((' &'' &'' &''& ''& ''\\
 ')(()' &'' &'' &'' &'' &''
\end{pmatrix}
$$

En cada posici'on i,j de la matriz para i $\in$ [1,n] y  j $\in$ [1,m] se va a guardar la menor cadena que cumpla  que *s[0:i]* y *t[0:j]* son subsecuencias de esta.



Esta cadena est'a construida a partir de las cadenas que se encuentra en las posiciones *[i-1][j]* y *[i][j-1]* de la matriz, de la siguiente forma:

- Se comprueba si la cadena en la posicion *[i-1][j]* cumple que *t[0:j]* es subsecuenncia de esta, en este caso se guarda como posible cadena seleccionada.
- Igualmente se comprueba que la cadena en la posicion *[i][j-1]* cumple que *s[0:i]*   es subsecuenncia de esta, en este caso se guarda como posible cadena seleccionada.
- Luego se guardan a ser seleccionadas las cadenas *dp[i-1][j]+t[j]*  y *dp[i][j-1]+s[i]* ya que ambas cumplen que *s[0:i]* y *t[0:j]* son subsecuenncias de esta. Porque si a es subsecuencia de b =>a+c es subsecuencia de b+c.
- Teniendo las cadenas guardadas anteriormente se selecciona la o una de las que cumpla que la suma de la cantidad de par'entesis a agregarle para balancearla con su tamanno sea m'inima.

Cuando la dp est'e completa se retorna la cadena que se encuentra en la posicion *[n+1][m+1]* de la matriz.

Como se puede ver esta funci'on tiene de costo *nm* al recorrer cada una de las posiciones de la matriz, adem'as del costo de buscar las posibles soluciones a seleccionar y de estos buscar la mejor teniendo un costo todos estos procesos  $\leq$ max(n,m)   =>*T(n,m)=nm max(m,n)* => *O(nm max(m,n))*.

Este algoritmo es bastante m'as eficiente que lo que se ten'ia hasta el momento pero no siempre da la cadena m'inima, para muy pocos casos da cadenas erroneas porque no se garantiza que partiendo de un optimo de s[i] y t[j] se pueda llegar a un optimo de s y t.

######Contraejemplo que demuestra que partiendo de una solucion optima de s[0:i] y t[0:j] no siempre se llega a una solucion optima de s y t.
Se tienen las cadenas
s="()())" 
t="(()))"
$s_{i}$="()()"
$t_{j}$ ="(())"
Donde $s_{i}$ es prefijo de s y $t_{j}$ es prefijo de t.
Una solucion optima de nuestro problema para las cadenas $s_{i}$ y la solucion que da dinamica 1 es "(())()()" apoyandose en la cadena anterior, pero la solucion correcta para s y t es "(()())"
=> No se puede garantizar que partiendo de una solucion optima de s[0:i] y t[0:j] se pueda llegar a una solucion optima de s y t.

#####Solucion dinamica 2

Para solucionar los problemas del algoritmo anterior se propone un ajuste a esta soluci'on en el cual en cada espacio de la matriz en lugar de estar guardando una cadena optima, se van a estar guardando todas las cadenas


