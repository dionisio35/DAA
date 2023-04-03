
######Solucion dinamica 1
Una de las primeras soluciones que ideamos para atacar el problema es la siguiente:
- Crear una matriz de tamaño $n+1 \times m+1$ donde $n$ y $m$ son los tamaños de las cadenas *s* y *t* respectivamente.
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

En cada posici'on i,j de la matriz para i $\in$ [1,n] y  j $\in$ [1,m] se va a guardar la menor cadena que cumpla 2 y 3 
- Llenar la matriz de la siguiente forma:
    - Si el caracter en la fila i y columna j de la cadena *s* es igual al caracter en la fila i y columna j de la cadena *t* entonces se copia el valor de la celda diagonal superior izquierda.
 
