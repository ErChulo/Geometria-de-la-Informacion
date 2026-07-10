## Materias - prerequisitos

- **Álgebra lineal**  
  - Espacios vectoriales, bases y cambio de base  
  - Productos internos, normas, ortogonalidad y proyecciones  
  - Autovalores/autovectores, descomposición espectral y SVD  
  - Matrices simétricas/definidas positivas, traza y determinante  
  - Cálculo matricial (reglas de traza, gradientes básicos) y pseudoinversa

- **Cálculo multivariable**  
  - Gradiente, Hessiana y expansiones de Taylor de segundo orden  
  - Regla de la cadena y del producto; jacobianos  
  - Optimizadores de primer/segundo orden y condiciones de optimalidad  
  - Cambio de variables en integrales  
  - Teorema de la función implícita (nociones)

- **Probabilidad (convergencias, LLN/CLT)**  
  - Espacio de probabilidad, variables aleatorias y sigma-álgebras  
  - Esperanza, varianza, covarianza y esperanza condicional  
  - Modos de convergencia: a.s., en probabilidad, en distribución, en \(L^p\)  
  - Leyes de los grandes números y Teorema Central del Límite  
  - Herramientas asintóticas: Slutsky, Cramér–Wold, teorema delta (nociones)

- **Estadística matemática (verosimilitud, estimación y contraste básicos)**  
  - Verosimilitud y máximo verosímil; consistencia y normalidad asintótica  
  - Información de Fisher y cota de Cramér–Rao  
  - Suficiencia (factorización de Fisher–Neyman) y Rao–Blackwell  
  - Contrastes: Neyman–Pearson y razón de verosimilitudes  
  - Intervalos de confianza y pruebas de Wald/score/LR (nociones)

- **Análisis convexo y optimización (dualicidad, proyecciones, KKT)**  
  - Conjuntos y funciones convexas; convexidad fuerte y Lipschitz  
  - Subgradientes, conjugado de Fenchel y desigualdad Fenchel–Young  
  - Divergencias de Bregman y proyecciones sobre conjuntos convexos  
  - Lagrangiano, dualidad de Fenchel y condiciones KKT  
  - Operadores proximales y regularización (nociones)

- **Geometría diferencial (nociones introductorias de variedades y métricas)**  
  - Variedades suaves, cartas y atlas; aplicaciones suaves  
  - Espacios tangentes, pushforward/pullback  
  - Métrica Riemanniana, gradiente y geodésicas  
  - Conexión de Levi–Civita, curvatura y mapa exponencial  
  - Invariancia por reparametrizaciones (nociones)

- **Teoría de la información (entropía, divergencia KL)**  
  - Entropía, entropía cruzada y divergencia KL  
  - Información mutua y reglas de cadena  
  - Desigualdad de procesamiento de datos  
  - \(f\)-divergencias (KL, Hellinger, \(\chi^2\), Jensen–Shannon)  
  - Familias exponenciales y momentos (nociones)

- **Procesos estocásticos (p. ej., cadenas de Markov básicas)**  
  - Cadenas de Markov en tiempo discreto: matriz de transición  
  - Distribuciones estacionarias, ergodicidad y mezcla  
  - Reversibilidad y balance detallado  
  - Ley fuerte del número grande en cadenas ergódicas (nociones)  
  - Ideas básicas de MCMC (transiciones e invarianza)

- **Programación científica (Python/NumPy; opcional: Wolfram/MATLAB)**  
  - NumPy: arreglos, broadcasting y álgebra lineal  
  - SciPy: integración, optimización y stats  
  - Automatización y reproducibilidad (notebooks, entornos, semillas)  
  - Visualización básica (matplotlib)  
  - Diferenciación automática (JAX/Autograd; nociones)

- **Métodos numéricos para optimización**  
  - Descenso por gradiente, line search y criterios de parada  
  - Newton y quasi-Newton (BFGS/L-BFGS)  
  - Métodos estocásticos (SGD, momentum)  
  - Proyección, penalizaciones y barreras para restricciones  
  - Regulares numéricas: condicionamiento y estabilidad

---

## Lista de Teoremas Previos - prerequisitos

* Ley de los Grandes Números (débil y fuerte)
* Teorema de Glivenko–Cantelli
* Teorema de Cramér–Wold
* Teorema Central del Límite (Lindeberg–Feller, Lyapunov)
* Teorema delta
* Principio de invariancia de Donsker
* Lema de Neyman–Pearson
* Teorema de factorización de Fisher–Neyman (suficiencia)
* Teorema de Rao–Blackwell
* Teorema de Lehmann–Scheffé
* Teorema de Pitman–Koopman–Darmois (familias exponenciales)
* Desigualdad de Cramér–Rao
* Desigualdad de Gibbs (no negatividad de KL)
* Teorema de proyección de Csiszár (I-proyección)
* Teorema pitagórico para divergencias KL/Bregman
* Teorema de Čencov/Chentsov (unicidad de la métrica de Fisher)
* Consistencia de Wald (y marco de decisión de Wald)
* Local Asymptotic Normality (LAN) de Le Cam
* Lemas de Le Cam (especialmente el tercero)
* Teorema de convolución de Hájek–Le Cam
* Teorema de Bernstein–von Mises
* Teorema de Sanov (grandes desvíos)
* Teorema de Gärtner–Ellis (LDP)
* Teorema de Varadhan (principio variacional)
* Teorema de equipartición asintótica / Shannon–McMillan–Breiman
* Teorema de Hammersley–Clifford
* Teorema de de Finetti (intercambiabilidad)

---

## Teoremas con su enunciado

* Ley de los Grandes Números (débil y fuerte)

  1. Si $X_1,\dots,X_n$ son i.i.d. con $\mathbb E[X_i]=\mu$, entonces $\bar X_n \xrightarrow{p} \mu$ (débil) y $\bar X_n \xrightarrow{a.s.} \mu$ (fuerte).
  2. El promedio muestral se acerca al valor esperado verdadero al aumentar el tamaño de muestra.

* Teorema de Glivenko–Cantelli

  1. $\sup_x |F_n(x)-F(x)| \xrightarrow{a.s.} 0$.
  2. La CDF empírica converge uniformemente a la CDF verdadera.

* Teorema de Cramér–Wold

  1. $X_n \Rightarrow X$ en $\mathbb R^k$ $\iff$ $a^\top X_n \Rightarrow a^\top X$ para todo $a\in\mathbb R^k$.
  2. Para convergencia en distribución multivariante basta chequear todas las proyecciones unidimensionales.

* Teorema Central del Límite (Lindeberg–Feller, Lyapunov)

  1. Si $X_i$ i.i.d. con media $\mu$ y varianza $\sigma^2$, entonces $\sqrt n(\bar X_n-\mu)\Rightarrow \mathcal N(0,\sigma^2)$.
  2. La media, reescalada, se vuelve aproximadamente normal bajo condiciones generales.

* Teorema delta

  1. Si $\sqrt n(T_n-\theta)\Rightarrow \mathcal N(0,V)$ y $g$ es diferenciable en $\theta$, entonces $\sqrt n\big(g(T_n)-g(\theta)\big)\Rightarrow \mathcal N\big(0,; g'(\theta),V,g'(\theta)^\top\big)$.
  2. Funciones suaves de estimadores asintóticamente normales siguen siendo asintóticamente normales.

* Principio de invariancia de Donsker

  1. $\sqrt n,(F_n-F)\Rightarrow \mathbb G_F$ (puente Browniano); equivalente: FCLT para sumas parciales $\Rightarrow$ movimiento Browniano.
  2. El proceso empírico converge a un proceso gaussiano límite.

* Lema de Neyman–Pearson

  1. Para $H_0:f_0$ vs $H_1:f_1$, la prueba más potente de nivel $\alpha$ es: rechazar si $\frac{f_1(x)}{f_0(x)}>k$.
  2. El test de razón de verosimilitudes es óptimo entre pruebas del mismo nivel.

* Teorema de factorización de Fisher–Neyman (suficiencia)

  1. $T$ es suficiente $\iff$ $f_\theta(x)=g_\theta(T(x)),h(x)$.
  2. La verosimilitud se separa en una parte que depende de $T$ y otra que no.

* Teorema de Rao–Blackwell

  1. Para $T$ suficiente, $\tilde\delta= \mathbb E[\delta(X)\mid T]$ cumple $\operatorname{Var}*\theta(\tilde\delta)\le \operatorname{Var}*\theta(\delta)$.
  2. Mejorar un estimador condicionando en un estadístico suficiente no empeora la varianza.

* Teorema de Lehmann–Scheffé

  1. Si $T$ es suficiente y completo, entonces $\phi(T)$ es el único UMVU.
  2. Con suficiencia+completitud, existe y es único el mejor insesgado.

* Teorema de Pitman–Koopman–Darmois (familias exponenciales)

  1. i.i.d. con soporte fijo y estadístico suficiente de dimensión finita para todo $n$ $\Rightarrow$ la familia es exponencial.
  2. Sólo las familias exponenciales admiten suficiencia finita uniforme en $n$.

* Desigualdad de Cramér–Rao

  1. $\operatorname{Var}_\theta(\hat\theta);\ge; I(\theta)^{-1}$ (escalar), con $I(\theta)$ la información de Fisher.
  2. Cota inferior para la varianza de estimadores insesgados.

* Desigualdad de Gibbs (no negatividad de KL)

  1. $D_{\mathrm{KL}}(P|Q)\ge 0$, con igualdad ssi $P=Q$ a.s.
  2. La divergencia KL nunca es negativa.

* Teorema de proyección de Csiszár (I-proyección)

  1. Si $\mathcal C$ es convexa cerrada, existe $Q^\star=\arg\min_{Q\in\mathcal C} D(P|Q)$, único.
  2. La mejor aproximación a $P$ dentro de una clase convexa (en KL) existe y es única.

* Teorema pitagórico para divergencias KL/Bregman

  1. Si $Q^\star$ es proyección de $P$ sobre $\mathcal C$, entonces $D(P|Q)=D(P|Q^\star)+D(Q^\star|Q)$ para $Q\in\mathcal C$.
  2. La “ortogonalidad” en divergencias descompone el error en suma.

* Teorema de Čencov/Chentsov (unicidad de la métrica de Fisher)

  1. Toda métrica Riemanniana invariante bajo morfismos de Markov es proporcional a la métrica de Fisher.
  2. La métrica de Fisher es esencialmente la única compatible con coarse-graining estocástico.

* Consistencia de Wald (y marco de decisión de Wald)

  1. Bajo identificabilidad y regularidad, $\hat\theta_n \xrightarrow{p}\theta_0$ para estimadores de riesgo mínimo (M-/Z-estimadores).
  2. Los estimadores “bien portados” convergen al parámetro verdadero.

* Local Asymptotic Normality (LAN) de Le Cam

  1. $\ell_n(\theta_0+h/\sqrt n)-\ell_n(\theta_0)=h^\top\Delta_n-\tfrac12 h^\top I(\theta_0)h+o_{\mathbb P}(1)$, con $\Delta_n\Rightarrow \mathcal N(0,I)$.
  2. Localmente, el modelo se parece a un experimento gaussiano con información $I(\theta_0)$.

* Lemas de Le Cam (especialmente el tercero)

  1. Bajo contigüidad, si $Z_n\Rightarrow Z$ y $\log \frac{dQ_n}{dP_n}\Rightarrow \tfrac12|t|^2+t^\top Z$, entonces $Z_n$ bajo $Q_n$ $\Rightarrow Z+t$.
  2. Relacionan cambios de medida locales con desplazamientos gaussianos.

* Teorema de convolución de Hájek–Le Cam

  1. Cualquier límite de estimadores regulares: $\mathcal L(\sqrt n(\hat\theta_n-\theta))= \mathcal N(0,I^{-1}) * M$, eficiente ssi $M=\delta_0$.
  2. La parte no gaussiana mide ineficiencia; eficiencia ⇔ sin “ruido extra”.

* Teorema de Bernstein–von Mises

  1. La posterior: $\sqrt n(\theta-\hat\theta_n)\mid X_{1:n}\Rightarrow \mathcal N(0,I^{-1})$.
  2. Asintóticamente, la inferencia bayesiana coincide con la frecuentista eficiente.

* Teorema de Sanov (grandes desvíos)

  1. Para medidas empíricas $\hat P_n$, $\displaystyle \lim_{n\to\infty}\frac1n\log \mathbb P(\hat P_n\in A) = -\inf_{Q\in A^\circ} D(Q|P)$.
  2. Las probabilidades de desviaciones raras de la ley empírica decaen exponencialmente con tasa KL.

* Teorema de Gärtner–Ellis (LDP)

  1. Si $\Lambda_n(t)=\tfrac1n\log \mathbb E e^{t S_n}\to \Lambda(t)$ diferenciable esencialmente convexa, entonces hay LDP con tasa $I(x)=\sup_t{tx-\Lambda(t)}$.
  2. Un LDP puede deducirse de funciones generadoras de momentos límite.

* Teorema de Varadhan (principio variacional)

  1. Para $X_n$ con LDP tasa $I$, $\displaystyle \lim_{n\to\infty}\frac1n\log \mathbb E\big[e^{n f(X_n)}\big]=\sup_x{f(x)-I(x)}$ (bajo regularidad).
  2. Evalúa integrales exponenciales vía un principio del máximo.

* Teorema de equipartición asintótica / Shannon–McMillan–Breiman

  1. Para proceso estacionario ergódico, $-\tfrac1n\log P(X_{1:n}) \xrightarrow{a.s.} H$.
  2. Secuencias largas son “típicas” y su probabilidad se concentra cerca de la entropía.

* Teorema de Hammersley–Clifford

  1. Si $P$ es estrictamente positivo, entonces $P$ es Markov respecto a $G$ $\iff$ $P$ factoriza sobre las cúspides (cliques) de $G$.
  2. La independencia condicional gráfica equivale a factorización.

* Teorema de de Finetti (intercambiabilidad)

  1. $X_1,X_2,\dots$ intercambiables $\iff$ existe medida $\mu$ tal que $P(X_{1:n}\in\cdot)=\int \prod_{i=1}^n P_\theta(\cdot), d\mu(\theta)$.
  2. Secuencias intercambiables son mezclas de i.i.d.

---

## Lista de Simbolos

| Símbolo                            | Significado                                             |   |                |
| ---------------------------------- | ------------------------------------------------------- | - | -------------- |
| $X_1,\dots,X_n$                    | variables aleatorias muestrales                         |   |                |
| i.i.d.                             | independientes e idénticamente distribuidas             |   |                |
| $\mathbb E[X_i]$                   | valor esperado                                          |   |                |
| $\mu$                              | media poblacional                                       |   |                |
| $\bar X_n$                         | media muestral                                          |   |                |
| $\xrightarrow{p}$                  | convergencia en probabilidad                            |   |                |
| $\xrightarrow{a.s.}$               | convergencia casi segura                                |   |                |
| $F_n$                              | función de distribución empírica                        |   |                |
| $F$                                | función de distribución verdadera                       |   |                |
| $\sup_x$                           | supremo sobre $x$                                       |   |                |
| $                                  | \cdot                                                   | $ | valor absoluto |
| $X_n, X$                           | (vector) variable aleatoria límite                      |   |                |
| $\Rightarrow$                      | convergencia en distribución                            |   |                |
| $\mathbb R^k$                      | espacio euclidiano $k$-dimensional                      |   |                |
| $a^\top$                           | vector/forma lineal (traspuesta)                        |   |                |
| $\sigma^2$                         | varianza poblacional                                    |   |                |
| $\mathcal N(m,\Sigma)$             | distribución normal con media $m$ y covarianza $\Sigma$ |   |                |
| $\sqrt n$                          | factor de escalamiento                                  |   |                |
| $g$                                | función diferenciable                                   |   |                |
| $g'(\theta)$                       | derivada/gradiente en $\theta$                          |   |                |
| $V$                                | matriz de varianzas–covarianzas asintótica              |   |                |
| $\mathbb G_F$                      | puente Browniano (proceso gaussiano)                    |   |                |
| $H_0, H_1$                         | hipótesis nula y alternativa                            |   |                |
| $f_0, f_1$                         | densidades bajo $H_0$ y $H_1$                           |   |                |
| $\dfrac{f_1(x)}{f_0(x)}$           | razón de verosimilitudes                                |   |                |
| $k$                                | umbral de decisión                                      |   |                |
| $T$                                | estadístico (p. ej., suficiente)                        |   |                |
| $f_\theta(x)$                      | densidad/verosimilitud del modelo                       |   |                |
| $g_\theta, h$                      | funciones en la factorización                           |   |                |
| $\theta$                           | parámetro                                               |   |                |
| $\operatorname{Var}_\theta(\cdot)$ | varianza bajo $P_\theta$                                |   |                |
| $\delta(X)$                        | estimador inicial                                       |   |                |
| $\tilde\delta$                     | estimador condicionado en $T$                           |   |                |
| $\phi(T)$                          | función de $T$                                          |   |                |
| $I(\theta)$                        | información de Fisher                                   |   |                |
| $I^{-1}$                           | inversa de la información de Fisher                     |   |                |
| $D_{\mathrm{KL}}(P|Q)$             | divergencia Kullback–Leibler                            |   |                |
| $D(\cdot|\cdot)$                   | divergencia (KL/Bregman)                                |   |                |
| $P, Q$                             | medidas/distribuciones                                  |   |                |
| $\mathcal C$                       | conjunto convexo/clase de modelos                       |   |                |
| $Q^\star$                          | proyección $I$-óptima de $P$ en $\mathcal C$            |   |                |
| $\arg\min$                         | argumento que minimiza                                  |   |                |
| $\ell_n(\theta)$                   | log-verosimilitud                                       |   |                |
| $h$                                | desplazamiento local (LAN)                              |   |                |
| $\Delta_n$                         | score centralizado/normalizado                          |   |                |
| $o_{\mathbb P}(1)$                 | término que va a $0$ en probabilidad                    |   |                |
| $*$                                | convolución de distribuciones                           |   |                |
| $M$                                | medida/ruido adicional en la convolución                |   |                |
| $\delta_0$                         | masa de Dirac en $0$                                    |   |                |
| $\hat\theta_n$                     | estimador (p. ej., MLE)                                 |   |                |
| $\hat P_n$                         | medida empírica                                         |   |                |
| $A, A^\circ$                       | conjunto e interior                                     |   |                |
| $S_n$                              | suma/estadístico agregado                               |   |                |
| $\Lambda_n(t)$                     | CGF escalada (función generadora de cumulantes)         |   |                |
| $\Lambda(t)$                       | límite de $\Lambda_n(t)$                                |   |                |
| $I(x)$                             | función de tasa (LDP)                                   |   |                |
| $t$                                | parámetro dual / desplazamiento                         |   |                |
| $x$                                | valor de la variable                                    |   |                |
| $f$                                | función de prueba (Varadhan)                            |   |                |
| $H$                                | entropía                                                |   |                |
| $X_{1:n}$                          | bloque muestral de longitud $n$                         |   |                |
| $G$                                | grafo no dirigido                                       |   |                |
| clique                             | cúspide máxima del grafo                                |   |                |
| $\mu$ (de Finetti)                 | medida de mezcla                                        |   |                |
| $P_\theta$                         | distribución componente                                 |   |                |
| $Q_n, P_n$                         | sucesiones de medidas                                   |   |                |
| $\dfrac{dQ_n}{dP_n}$               | derivada de Radon–Nikodým                               |   |                |
| $Z_n, Z$                           | vector gaussiano límite                                 |   |                |
| $\mathcal L(\cdot)$                | ley/distribución                                        |   |                |
| $\mathbb P$                        | medida de probabilidad                                  |   |                |
| $\mathbb E$                        | operador esperanza                                      |   |                |

---

# Prefacio filosófico

### ¿Qué es la Geometría de la Información?

Es un modo de pensar la inferencia como una **elección normativa** de “qué significa que dos distribuciones estén cerca”, a partir de la cual emergen la métrica de Fisher–Rao y, con ella, la geometría (métricas, conexiones duales, variedades dualmente planas) que respeta las reparametrizaciones por estadísticos suficientes . Esa dualidad —formalizada por las α-conexiones de Amari— refleja que no hay una única “línea recta” entre creencias parciales: distintos geodésicos codifican diferentes modos pragmáticos de actualizarse . En ese sentido, la disciplina trata la **incertidumbre como sustancia primaria** y ofrece un lenguaje común para sistemas cuyo “estado” es una distribución de probabilidad . Un hilo unificador es la familia de **divergencias de Bregman** (incluida KL), que cuantifican el coste asimétrico de representar una “realidad” (p) con un “modelo” (q) .

### ¿Qué ventaja tiene saber Geometría de la Información?

Provee una **tecnología de autocorrección**: moverse por el “manifold estadístico” es seguir trayectorias que **minimizan divergencias**, es decir, organizar expectativas para reducir futuras sorpresas . Esta mirada unifica inferencia, decisión y optimización: la elección de una función convexa (F) fija la geometría y el **criterio de coste/regret** con el que se aprende o se decide; en particular, KL (caso Bregman con (F(x)=x\log x)) conecta con métodos bayesianos variacionales y selección de modelos . El resultado es un **lenguaje compartido** que atraviesa estadística, aprendizaje, termodinámica y otros dominios donde lo central es gestionar la incertidumbre .

### Breve historia

Desde **Fisher y Rao**, la métrica que queda al exigir invariancia bajo suficiencia sirve como “punto de partida” técnico de la teoría . **Amari** introduce la estructura dual (α-conexiones) que hace explícitas las dos nociones complementarias de rectitud y actualización en espacios estadísticos . En paralelo, las **divergencias de Bregman** (con **KL** como caso emblemático) se consolidan como el instrumento que conecta geometría, optimización, decisión y Bayesianismo moderno (p. ej., inferencia variacional) . Así, la disciplina cristaliza una consigna práctica: *comienza con Fisher–Rao; deja que la curvatura de tu propia incertidumbre sea la brújula* .

