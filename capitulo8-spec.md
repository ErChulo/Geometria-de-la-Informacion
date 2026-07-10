# Spec — Capítulo 8: *Geometría de Hilbert de las variables aleatorias*

Short name: `capitulo8-hilbert`
Status: Fase 4 del plan estratégico (F4). Diseño detallado **previo** a F5 (redacción).

---

## 1. Motivación y prerrequisitos

### 1.1 ¿Por qué este capítulo?

Capítulos 1-3 construyen geometría de **parámetros** (espacio de distribuciones parametrizadas).
Capítulos 5-6 aplican esa geometría a inferencia (MLE, EM, etc.).

**Lo que falta:** una geometría directamente sobre las **realizaciones** de variables aleatorias. Si $X$ es una v.a., podemos verla como un vector en un **espacio de Hilbert** ($L^2(\Omega,\mathcal{F},P)$). Su producto interno es $\langle X, Y\rangle = E[XY]$, su norma $\|X\| = \sqrt{E[X^2]}$, y la covarianza es exactamente una **matriz de Gram** sobre v.a. centradas.

Este ángulo es lo que une la geometría de la información con:
- Regresión lineal (proyección ortogonal en $L^2$),
- Métodos kernel (RKHS, kernel embedding),
- MMD (Maximum Mean Discrepancy) en tests de hipótesis,
- Conexión con información de Fisher de 2º orden (= Hessiana = covarianza del score = gram matrix del score).

### 1.2 Prerrequisitos

Definidos en `prerequisitos.md` y a verificar antes de F5:

- Espacios normados y de Hilbert:
  - Definición de espacio de Hilbert.
  - Ortogonalidad en Hilbert.
  - Proyección ortogonal sobre subespacios cerrados.
  - Teorema de representación de Riesz (mencionado, no probado).
- $L^2$ spaces:
  - $\|X\|_2^2 = E[X^2]$, definición formal.
  - Completitud (mencionado).
- Funciones kernel:
  - Definición de kernel definido positivo.
  - Kernels经典: linear, polynomial, RBF/Gaussian.
- Álgebra lineal:
  - Matrices PSD como kernels.
  - Descomposición espectral.

El alumno que haya pasado Capítulos 0-3 del libro ya tiene casi todo. **Lo único que hay que añadir al `prerequisitos.md` es una nota sobre "Análisis funcional básico"** (~10 líneas).

---

## 2. Outline del capítulo

| § | Título | Función pedagógica |
|---|---|---|
| 8.1 | Variables aleatorias como vectores en $L^2$ | El "puente" de pensamiento |
| 8.2 | Covarianza como matriz de Gram | Gram + covarianza = mismo objeto |
| 8.3 | Regresión lineal como proyección ortogonal | Caso conocido reinterpretado |
| 8.4 | Distancia de Mahalanobis | Geometría de la covarianza |
| 8.5 | Reproducing Kernel Hilbert Spaces (RKHS) | Elevando datos a dimensión infinita |
| 8.6 | Mean embeddings: distribuciones como puntos en RKHS | La distribución completa como $\mu_P$ |
| 8.7 | Maximum Mean Discrepancy (MMD) | Test de dos muestras con kernel |
| 8.8 | El puente con Información de Fisher | **Conecta con Cap. 1-3** |
| 8.9 | Experimentos con Python | Todo en código |
| 8.10 | Ejercicios (★ a ★★★★) | Convertir en experto |

---

## 3. Contenido detallado por sección

### 8.1 Variables aleatorias como vectores en $L^2$

**Definición 8.1** *(Espacio $L^2$)*. Sea $(\Omega, \mathcal{F}, P)$ un espacio de probabilidad. Entonces
$$L^2(\Omega, \mathcal{F}, P) = \left\{ X : \Omega \to \mathbb{R} \mid E[X^2] < \infty \right\}$$
dotado del producto interno $\langle X, Y \rangle = E[XY]$ es un espacio de Hilbert.

**Proposición 8.1** *(Ortogonalidad = incorrelación)*. $X \perp Y$ en $L^2$ (con $E[X]=E[Y]=0$) si y solo si $\text{Cov}(X, Y) = 0$.

**Figura TikZ 8.1**: Diagrama del espacio $L^2$ con varios vectores (v.a.) y un subespacio spanned por $\{1, X\}$ como ilustración.

**Idea intuitiva**: cambia el chip mental — la v.a. no es un "número aleatorio que sale", sino un **vector** en un espacio vectorial concreto. La geometría de ese espacio codifica toda la estructura de segundo orden.

---

### 8.2 Covarianza como matriz de Gram

**Definición 8.2** *(Matriz de Gram)*. Para v.a. $X_1, \dots, X_k$ centradas, la matriz de covarianza es la matriz de Gram de sus productos:
$$\Sigma_{ij} = E[X_i X_j] = \langle X_i, X_j \rangle.$$

**Proposición 8.2** *($\Sigma$ es PSD)*. Por Cauchy-Schwarz en $L^2$, $\Sigma \succeq 0$. Es $\Sigma \succ 0$ si y solo si las $\{X_i\}$ son linealmente independientes.

**Reformulación**: Una matriz $K \in \mathbb{R}^{n\times n}$ es una **matriz kernel** (definida positiva) si y solo si existe un embedding $\phi: \mathcal{X} \to L^2$ tal que $K_{ij} = \langle \phi(x_i), \phi(x_j) \rangle$.

**Esto es el corazón del kernel method**: cualquier PSD $K$ es un kernel.

---

### 8.3 Regresión lineal como proyección ortogonal

**Teorema 8.1** *(Proyección ortogonal en $L^2$)*. Sea $Y$ un v.a. y $\mathcal{S} = \text{span}\{1, X_1, \dots, X_p\} \subseteq L^2$. La proyección ortogonal $\pi_{\mathcal{S}}(Y)$ minimiza $E[(Y - \hat{Y})^2]$ sobre $\hat{Y} \in \mathcal{S}$. Es la regresión lineal clásica.

**Figura TikZ 8.2**: Plano $\mathcal{S}$ en $L^2$, vector $Y$, proyección ortogonal con marca del ángulo recto.

**Conexión con ML**: mínimos cuadrados ordinarios = proyección en $L^2$.

---

### 8.4 Distancia de Mahalanobis

**Definición 8.3** *(Distancia de Mahalanobis)*. Para $x \in \mathbb{R}^p$ con covarianza empírica $\hat{\Sigma}$:
$$d_M(x, y) = \sqrt{(x - y)^T \hat{\Sigma}^{-1} (x - y)}.$$

**Proposición 8.3** *(Mahalanobis = distancia en $L^2$ bajo blanqueo)*. Si $Z = \hat{\Sigma}^{-1/2}(x - \mu)$, entonces $d_M(x, y) = \|Z_x - Z_y\|$ en $L^2$. Geométricamente: estiras el espacio según $\hat{\Sigma}$ y luego mides distancia euclidiana.

**Aplicación**: detección de outliers, blanqueo, LDA.

---

### 8.5 Reproducing Kernel Hilbert Spaces (RKHS)

**Definición 8.4** *(Kernel)*. $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ es un kernel definido positivo si $k(x, x') = \langle \phi(x), \phi(x') \rangle$ para algún feature map $\phi: \mathcal{X} \to \mathcal{H}$, donde $\mathcal{H}$ es un Hilbert.

**Teorema 8.2** *(RKHS y la propiedad de reproducción)*. Si $k$ es un kernel, existe un único espacio de Hilbert $\mathcal{H}_k$ de funciones $f: \mathcal{X} \to \mathbb{R}$ tal que
$$k(x, \cdot) \in \mathcal{H}_k, \quad f(x) = \langle f, k(x, \cdot) \rangle_{\mathcal{H}_k}$$
para toda $f \in \mathcal{H}_k$.

**Ejemplos**:
- Lineal: $k(x, x') = \langle x, x' \rangle$.
- Polinomial: $k(x, x') = (\langle x, x' \rangle + c)^d$.
- RBF/Gaussian: $k(x, x') = \exp(-\|x-x'\|^2 / (2\sigma^2))$.

**Figura TikZ 8.3**: El kernel como feature map de input space $\mathcal{X}$ (curva en 2D) a $\mathcal{H}_k$ (curva en un espacio de Hilbert de dimensión alta).

---

### 8.6 Mean embeddings

**Definición 8.5** *(Mean embedding)*. Para distribución $P$ sobre $\mathcal{X}$ y kernel $k$:
$$\mu_P = \mathbb{E}_{X \sim P}[k(X, \cdot)] \in \mathcal{H}_k.$$

**Teorema 8.3** *(Caracterización de distribuciones)*. Si $k$ es **characteristic** (e.g., RBF, Laplace, polynomial de grado alto), entonces $\|\mu_P - \mu_Q\|_{\mathcal{H}_k}^2 = 0 \iff P = Q$.

**Consecuencia**: una distribución $P$ **queda completamente codificada** en su mean embedding, bajo un kernel caractéristique.

**Figura TikZ 8.4**: Imagen: cada distribución $P$ como un punto $\mu_P$ en el RKHS.

---

### 8.7 Maximum Mean Discrepancy (MMD)

**Definición 8.6** *(MMD)*.
$$\text{MMD}^2(P, Q; \mathcal{F}) = \sup_{f \in \mathcal{F}} \left( E_{P}[f] - E_{Q}[f] \right)^2$$
donde $\mathcal{F}$ es la bola unidad en un RKHS $\mathcal{H}_k$:
$$\text{MMD}^2(P, Q; k) = \| \mu_P - \mu_Q \|^2_{\mathcal{H}_k}.$$

**Versión empírica** (con muestras $X_1, \dots, X_n$ de $P$ y $Y_1, \dots, Y_m$ de $Q$):
$$\widehat{\text{MMD}}^2 = \frac{1}{n^2} \sum_{i,j} k(X_i, X_j) - \frac{2}{nm} \sum_{i,j} k(X_i, Y_j) + \frac{1}{m^2} \sum_{i,j} k(Y_i, Y_j).$$

**Aplicación**: test de dos muestras (Gretton et al., 2012) sin density estimation.

**Figura TikZ 8.5**: Diagrama de bloques mostrando las dos distribuciones y el cálculo de MMD empírico.

---

### 8.8 El puente con Información de Fisher

**Teorema 8.4** *(Crucial — conexión con Cap. 1)*. Sea $S_i = \partial \log p_\theta(X_i)/\partial \theta$ el score. Entonces:
1. $I(\theta) = \text{Var}_\theta(S) = E_\theta[S^2] = \langle S, S \rangle_{L^2}$.
2. El vector score $S(\theta, X)$ es un elemento de $L^2(\Omega, \mathcal{F}, P_\theta)$.
3. La métrica de Fisher es la **métrica del espacio de Hilbert de scores**:
$$g_{ij}(\theta) = E_\theta[\partial_i \ell \cdot \partial_j \ell] = \langle \partial_i \ell, \partial_j \ell \rangle_{L^2}.$$
4. **Conexión RKHS**: si modelas el score como $\ell(\theta, x) = \langle \eta(\theta), \phi(x) \rangle - A(\theta)$ (familia exponencial), entonces un **kernel apropiado** sobre el espacio de muestras es $k(x, x') = \langle \phi(x), \phi(x') \rangle$, y la geometría de Fisher es un RKHS del score localmente.

**Proposición 8.4** *(El score como embedding)*. Para familia exponencial, el score $\nabla \ell(\theta, X) = T(X) - \mu \in L^2$. Así que:
- Familias exponenciales $\Leftrightarrow$ el score es un vector en $L^2$ en una subvariedad afín.
- Geometría de Fisher = geometría inducida en este subvariedad.

**Esto cierra el arco**: lo que empezaste como geometría Riemanniana en Cap. 1 era en realidad geometría de un subespacio de $L^2$.

---

### 8.9 Experimentos con Python

**Listing 8.1** — Covarianza como Gram:
```python
import numpy as np

def gram_from_samples(samples, centered=True):
    """Compute Gram matrix from samples of random variables."""
    if centered:
        samples = samples - samples.mean(axis=0, keepdims=True)
    n = samples.shape[0]
    return (samples.T @ samples) / n  # Covariance == Gram matrix
```

**Listing 8.2** — Proyección ortogonal (regresión):
```python
def ols_projection(X, y):
    """OLS as orthogonal projection in L^2."""
    # X tiene primera columna de 1s
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return X @ beta
```

**Listing 8.3** — MMD empírico:
```python
def rbf_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x - y)**2 / (2 * sigma**2))

def mmd2(X, Y, sigma=1.0):
    """MMD al cuadrado con kernel RBF."""
    n, m = len(X), len(Y)
    Kxx = sum(rbf_kernel(X[i], X[j], sigma) for i in range(n) for j in range(n)) / n**2
    Kyy = sum(rbf_kernel(Y[i], Y[j], sigma) for i in range(m) for j in range(m)) / m**2
    Kxy = sum(rbf_kernel(X[i], Y[j], sigma) for i in range(n) for j in range(m)) / (n*m)
    return Kxx - 2*Kxy + Kyy
```

**Listing 8.4** — Two-sample test con MMD (p-value por permutaciones):
```python
def mmd_test(X, Y, sigma=1.0, n_perm=1000):
    observed = mmd2(X, Y, sigma)
    combined = np.vstack([X, Y])
    p_values = []
    for _ in range(n_perm):
        idx = np.random.permutation(len(combined))
        Xp, Yp = combined[idx[:len(X)]], combined[idx[len(X):]]
        p_values.append(mmd2(Xp, Yp, sigma))
    return observed, np.mean(np.array(p_values) >= observed)
```

**Listing 8.5** — Verificación numérica del Teorema 8.4:
```python
def fisher_vs_l2_geometry(theta, distribution, n_samples=10000):
    """Verify that Fisher metric = L^2 metric on scores."""
    # Sample scores from distribution
    samples = distribution.sample(n_samples, theta)
    scores = distribution.score(theta, samples)
    # Fisher metric (analytic)
    fisher_ij = distribution.fisher_information(theta)
    # L^2 metric on scores (empirical)
    l2_ij = np.cov(scores)
    return fisher_ij, l2_ij
```

**Listing 8.6** — Kernel ridge regression (opcional para ★★★★):
```python
def kernel_ridge(K, y, lam=1.0):
    n = len(y)
    return np.linalg.solve(K + lam * np.eye(n), y)
```

---

### 8.10 Ejercicios (★ a ★★★★)

Nivel 1 **(★, 5 ejercicios)** — rompehielos:

- ★ (V/F) Toda matriz PSD es una matriz de covarianza para alguna distribución.
- ★ Verifica que $\|X\|_2^2 = E[X^2]$ con un ejemplo concreto (Bernoulli, Uniforme).
- ★ (V/F) Si $X, Y$ son independientes, entonces $X \perp Y$ en $L^2$.
- ★ ¿Cuál es la dimensión del subespacio spanned por $\{1, X, X^2\}$ en $L^2(\Omega, P)$ para $X \sim \text{Uniforme}(0,1)$?
- ★ ¿Es $k(x, x') = \|x - x'\|$ un kernel válido?

Nivel 2 **(★★, 8 ejercicios)** — algorítmicos:

- ★★ Implementa `embed(X, kernel)` que mapea una matriz de muestras $X$ a su embedding empírico en un RKHS (con RBF).
- ★★ Verifica numéricamente que la covarianza = Gram matrix para 3 distribuciones distintas. Reporta error máximo.
- ★★ Computa MMD entre dos muestras de $\mathcal{N}(0,1)$ y $\mathcal{N}(0.5,1)$. Repite para $\mathcal{N}(0,1)$ y $\mathcal{N}(0,2)$ con tamaño de muestra $n=500$.
- ★★ Implementa whitening (transformación que convierte covarianza en identidad). Verifica en un dataset sintético.
- ★★ Para la distribución Beta, calcula $\|X\|_2^2$ analíticamente y verifica con simulación.
- ★★ Encuentra el kernel asociado a la matriz $K = \begin{pmatrix} 4 & 1 \\ 1 & 0.5 \end{pmatrix}$. ¿Es PSD?
- ★★ Computa la matriz de Mahalanobis para los datos `iris` entre las clases setosa y versicolor.
- ★★ Implementa `rbf_kernel_matrix(X, sigma)` y verifica que es PSD.

Nivel 3 **(★★★, 7 ejercicios)** — teóricos:

- ★★★ Demuestra que toda matriz PSD es realizable como covarianza de un vector aleatorio (usa descomposición espectral).
- ★★★ Demuestra Teorema 8.4 (Fisher $\Leftrightarrow$ producto interno en $L^2$ sobre scores).
- ★★★ Demuestra que RBF kernel es característico (idea).
- ★★★ Demuestra propiedad de reproducción del RKHS para el kernel lineal.
- ★★★ Demuestra equivalencia: MMD = 0 $\iff$ $P = Q$ para kernel característico.
- ★★★ (código) Verifica empíricamente la consistencia asintótica del test MMD (poder vs. tamaño de muestra).
- ★★★ ¿Por qué $L^2$ es completo? (Idea: usa sucesión de Cauchy y convergencia en $L^2$.)

Nivel 4 **(★★★★, 5 ejercicios)** — mini-proyectos:

- ★★★★ **Principal Component Analysis (PCA) = SVD en $L^2$.** Implementa PCA desde cero usando la matriz de Gram (sin centrar), verifica en `iris`, y compara con `sklearn.decomposition.PCA`.
- ★★★★ **Two-sample test completo.** Genera 3 datasets sintéticos (misma distribución, medias distintas, distribuciones distintas). Implementa el test MMD con RBF y reporta poder estadístico. Discute la elección de $\sigma$.
- ★★★★ **RKHS regression.** Usa `KernelRidge` de sklearn sobre un dataset sintético no-lineal. Visualiza el ajuste. Experimenta con $\sigma$.
- ★★★★ **Kernel mean embedding de distribuciones sintéticas.** Genera 5 distribuciones distintas. Embedding en RKHS con RBF. Visualiza los embeddings en 2D usando t-SNE. Discute.
- ★★★★ **El puente con Cap. 1.** Para 5 familias exponenciales distintas, genera muestras, calcula scores, verifica empíricamente que la métrica de Fisher coincide con el producto interno en $L^2$ sobre scores.

---

## 4. Figuras TikZ planificadas (5 figuras)

| # | Título | Tipo |
|---|---|---|
| 8.1 | $L^2(\Omega)$ vector space con varios v.a. como puntos | Diagrama vectorial |
| 8.2 | Proyección ortogonal de $Y$ sobre plano $\mathcal{S}$ | Geométrico con ángulo recto |
| 8.3 | Feature map: 1D $\to$ RKHS dim. alta | Curva en plano + curva 2D elevada |
| 8.4 | Distribuciones como puntos en el RKHS | 3 puntos etiquetados $P, Q, R$ |
| 8.5 | Pipeline MMD test | Diagrama de flujo |

(En F5 se incluyen los códigos TikZ completos; aquí solo se documentan para implementación futura.)

---

## 5. Salidas computacionales esperadas

Cada listing de 8.9 debe producir:

| Listing | Output esperado |
|---|---|
| 8.1 | Matriz PSD simétrica, eigenvalues reales ≥ 0 |
| 8.2 | Predicciones que minimizan MSE(error estándar de sklearn) |
| 8.3 | MMD² ≥ 0, simétrico en X,Y |
| 8.4 | p-value ∈ [0,1]. p≈ 1 si distribuciones idénticas, p ≈ 0 si distintas |
| 8.5 | Comparación matriz-analítica vs empírica, error ≤ 5% para n ≥ 10000 |
| 8.6 | Predicciones estables, sin overfitting a $\lambda$ moderado |

Todos deben correr en Python 3.10+ con: `numpy`, `scipy`, `scikit-learn`, `matplotlib`, opcionalmente `jax` para los listados que usen autodiff.

---

## 6. Estructura de archivos a tocar en F5

| Archivo | Cambio |
|---|---|
| `prerequisitos.md` | Añadir al final:## Análisis funcional básico (10 líneas) |
| `main.tex` | Añadir `\include{capitulo8}` después de `\include{capitulo7}` y antes de `\backmatter` |
| `capitulo8.tex` | **NUEVO** — el contenido del capítulo (~30 páginas) |
| `respuestas.tex` | Nueva sección "Capítulo 8" con ~25 soluciones |

---

## 7. Criterio de "hecho" para F5

- [ ] `capitulo8.tex` existe y compila integrado en `main.tex`.
- [ ] Las 5 figuras TikZ están dibujadas y referenciadas.
- [ ] Los 6 listings Python están escritos y pueden copiarse a un Jupyter Notebook.
- [ ] Las 25 soluciones están en `respuestas.tex`.
- [ ] `make build` compila dos veces sin ERRORES.
- [ ] El capítulo se conecta explícitamente con Cap. 1 (Fisher) — referencias cruzadas.

---

## 8. Riesgos y mitigaciones

- **El alumno necesita un cuaderno en blanco de Cap. 3.** Sin haber visto dualidad de Legendre, el puente con RKHS es opaco. Mitigación: F5 incluye un resumen de 1 página al inicio de Cap. 8 que repasa lo necesario.
- **El test MMD depende mucho de la elección de $\sigma$.** Mitigación: sección 8.7 incluye heurística "median heuristic".
- **El Teorema 8.4 es abstracto.** Mitigación: descomponer en 3 lemas (Fisher = Var(score), score $\in L^2$, score en familia exponencial es afín).
- **Hay doble conteo con Cap. 2 (KL en distribuciones).** MMD es una forma diferente de comparar distribuciones; aclararlo explícitamente.

---

## 9. Cómo se escribe el cap8.tex (esqueleto LaTeX)

```latex
% src/capitulo8.tex — Geometría de Hilbert de las variables aleatorias

\chapter{Geometría de Hilbert de las variables aleatorias}

\begin{quotation}
  \itshape
  ``Las variables aleatorias son vectores en un espacio de Hilbert; la geometría de la información es geometría de ese espacio.''
\end{quotation}

% Macro: \Rnds para R n samples draw notation, \ML para mahalanobis, etc.
% ...
```

(En F5 se desarrolla el contenido completo; aquí solo el esqueleto.)

---

## 10. Acceso a LLMs (recomendado)

Cada sección sugiere un "pregunta a tu LLM" para que el alumno dialogue y profundice:

| § | Pregunta sugerida al LLM |
|---|---|
| 8.1 | "¿Por qué $\|X\|_2 = \sqrt{E[X^2]}$ es la 'norma natural' y no otra?" |
| 8.2 | "¿Por qué cualquier matriz PSD es un kernel?" |
| 8.3 | "¿Cómo es la regresión lineal una proyección en $L^2$ y NO una proyección en $\mathbb{R}^n$?" |
| 8.4 | "¿Cuándo Mahalanobis coincide con euclidiana?" |
| 8.5 | "¿Por qué RBF induce un espacio de dimensión infinita?" |
| 8.6 | "Dame un ejemplo de un kernel NO característico y explica cuándo falla." |
| 8.7 | "¿Por qué la elección de $\sigma$ es el talón de Aquiles del MMD test?" |
| 8.8 | "¿Cómo se conecta la métrica de Fisher con el RKHS del score?" |

---

## 11. Estado del plan F1-F6

- [x] **F1** — Crítica feroz: `critica-por-capitulo.md`
- [x] **F2** — Plan de ejercicios: `plan-ejercicios.md`
- [x] **F4** — Spec del Cap. Hilbert: este documento
- [ ] **F3** — Implementación de nuevos ejercicios en cap0-7 + respuestas
- [ ] **F5** — Redacción del Capítulo 8 en LaTeX + integración + respuestas
- [ ] **F6** — Pulido final + `make build` limpio

Recomendación: tras tu aprobación de F2 y F4, ejecutar F3 cap por cap (empezando por Cap. 0 por menor complejidad) y F5 al final integrando el nuevo Cap. 8 antes de `\backmatter`.
