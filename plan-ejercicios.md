# Plan de Expansión de Ejercicios + Soluciones — *Geometría de la Información*

Short name: `plan-ejercicios`
Status: Fase 2 del plan estratégico (F2). Entregable **previo** a F3 (la implementación).
Synchronization: `critica-por-capitulo.md`, `prerequisitos.md`, todos los `capituloX.tex`.

---

## 1. Visión y Taxonomía

**Meta:** que el alumno (con ayuda de LLMs) se vuelva **experto** después de pasar por el libro.

**Definición de experto (operacional):** puede, dado un problema real,
1. Identificar qué estructura geométrica aplica (espacio de parámetros, espacio de v.a., Hilbert, mixtas).
2. Calcular a mano la métrica/Fisher/Christoffel/distancia correcta.
3. Implementar en JAX/PyTorch los pasos numéricos (proyección KL, gradiente natural, MMD).
4. Explicar POR QUÉ eligió esa estructura.
5. Cuestionar las hipótesis (suficiencia, regularidad) y proponer contraejemplos.

**Taxonomía con cuatro niveles (★ a ★★★★):**

| Nivel | Tipo | Señal de dominio | Muchos ejercicios así |
|---|---|---|---|
| ★ rompehielos | Conceptual / V/F / 1 línea | "¿Entendiste la definición?" | 25% |
| ★★ algorítmico | Cálculo matricial / sustitución | "¿Sabes operar?" | 35% |
| ★★★ teórico | Demostraciones / contraejemplos | "¿Puedes defender la estructura?" | 25% |
| ★★★★ mini-proyecto | Código real + análisis | "¿Puedes resolver un problema nuevo?" | 15% |

**Distribución objetivo por capítulo:**

| Capítulo | Ejercicios totales | Nuevos a añadir | ★ | ★★ | ★★★ | ★★★★ |
|---|---|---|---|---|---|---|
| 0 (prereq) | 30 | ~30 | 8 | 12 | 7 | 3 |
| 1 (Fundamentos) | 30 | ~20 | 5 | 8 | 5 | 2 |
| 2 (Bregman) | 30 | ~25 | 6 | 10 | 6 | 3 |
| 3 (Exp. families) | 30 | ~20 | 5 | 8 | 5 | 2 |
| 4 (α-conexiones) | 30 | ~25 | 6 | 9 | 7 | 3 |
| 5 (Inferencia) | 25 | ~20 | 4 | 8 | 5 | 3 |
| 6 (Aplicaciones) | 30 | ~25 | 5 | 8 | 6 | 6 |
| 7 (Avanzado) | 25 | ~22 | 4 | 8 | 6 | 4 |
| 8 (Hilbert/nuevo) | 25 | ~25 | 5 | 8 | 7 | 5 |
| **Total** | **255** | **~212** | **48** | **79** | **56** | **33** |

---

## 2. Mecanismo para auto-aprendizaje con LLMs

Cada ejercicio debe tener:

- **Cuadro de inicio para LLM** ("Pregúntale a tu LLM: …") — 1 línea.
- **Esqueleto de respuesta** ("Pista: …") — 0–2 líneas para no revelar la solución.
- **Criterio de verificación** ("Verifica con: …") — la línea de código o la fórmula que debe coincidir.

Esto convierte el ejercicio en una **micro-conversación con el LLM**:
1. Alumno lee el ejercicio, lee "Pregúntale a tu LLM".
2. Alumno encola esa pregunta al LLM en su sesión (con system prompt incluyendo el contexto del libro).
3. LLM responde, alumno verifica con el "criterio de verificación".
4. Si discrepan, alumno repregunta. Si coincide, alumno registra la respuesta en su cuaderno.

Para los ★★★★ el "criterio de verificación" NO es una sola línea sino un test (e.g., "tu implementación debe pasar estos 3 asserts"; "el plot debe mostrar esta forma").

---

## 3. Plan por capítulo: temas y catálogo de ejercicios modelo

A continuación, mapeo concreto de ejercicios modelo (no la lista completa — el detalle total se escribe en F3). Estos son **ejemplos canónicos** que muestran el tipo de problemas que llenarán las ~30 posiciones por capítulo.

### Capítulo 0 — Prerrequisitos (capital crucial)

**Nuevos ~30 ejercicios:**

Tema: "Por qué necesitas estos prerequisitos"

1. ★ **(filosófico)** Lee el Prólogo del libro (página i). En 200 palabras, explica por qué la probabilidad aparece ANTES que la geometría diferencial en este libro.
2. ★ (V/F) Si $A\in\mathbb{R}^{n\times n}$ y $\det A \neq 0$, entonces $A$ define un difeomorfismo lineal.
3. ★★ **Cuándo un problema de ML es lineal vs. no-lineal:** dado el siguiente dataset sintético $(x_i, y_i)$ con $y = \sin(x) + \epsilon$, explica por qué mínimos cuadrados falla.
4. ★★ Verifica con NumPy que $\nabla^2 f \succeq 0$ implica convexidad para 5 funciones distintas. Reporta eigenvalues.
5. ★★ Calcula el Jacobiano de $(x, y) \mapsto (\exp(x)\cos(y), \exp(x)\sin(y))$ en $(1,1)$. Reporta determinante — ¿es invertible?
6. ★★★ Demuestra que $E[X^2] \geq (E[X])^2$. Discute con el LLM por qué esto es Cauchy-Schwarz.
7. ★★★ Sea $X \sim \mathcal{N}(\mu,\sigma^2)$. Razona por qué $E[X]$ y $\text{Var}(X)$ son suficientes y por qué NO lo es la mediana.
8. ★★★★ **Mini-proyecto:** implementa una clase `DistributionLite` en Python con métodos `pdf`, `log_likelihood`, `kl_to`, `fisher_information(theta)` para 5 distribuciones.

Tema: "Por qué los conceptos importan"

9-15. Cobertura de cada tema con 1 ★★★ y 1 ★★.
16. ★★★★ Implementa softmax desde cero y verifica que sus derivadas coinciden con autodiff de JAX.

### Capítulo 1 — Fundamentos

**Nuevos ~20 ejercicios** (junto a los ~30 existentes):

**Tema: Información de Fisher como tensor**

17. ★★ Calcula la matriz de Fisher para Multinomial($\pi_1,\pi_2,\pi_3$). Verifica que $\det I = 0$ en el interior (por qué?).
18. ★★ **(con código)** Muestrea 10000 realizaciones de $\text{Bernoulli}(0.3)$ y estima $I(p)$ empíricamente. Compara con $1/(p(1-p))$. Repite para $p=0.01$ y comenta.
19. ★★★ Demuestra la invariancia tensorial de la métrica de Fisher. Usa la regla de transformación bajo $\eta=\log(p/(1-p))$ y verifica que las dos métricas satisfacen $g^{\eta}_{\eta\eta} = g^p_{pp} (dp/d\eta)^2$.
20. ★★★ **(código)** Calcula Fisher para Pareto con $\theta$ desconocido Y verifica numéricamente que la cota CR se cumple con un estimador eficiente.
21. ★★★★ **Mini-proyecto:** visualización del semiplano de Poincaré. Implementa una función que grafique dos puntos $(\mu_1, \sigma_1), (\mu_2, \sigma_2)$ y dibuje las tres geodésicas (euclidiana, $\alpha=1$, $\alpha=-1$). Discute cuál es la "más corta".

**Tema: Chentsov**

22. ★★★ Enuncia el teorema de Chentsov sin mirar el libro. Pídele a tu LLM que valide tu entendimiento.
23. ★★★★ **Mini-proyecto:** demuestra empíricamente que la métrica ANY covariante invariante bajo Markov morphisms es proporcional a Fisher. Usa familia exponencial Bernoulli.

### Capítulo 2 — Divergencias y Bregman

**Nuevos ~25 ejercicios:**

**Tema: $f$-divergencias**

24. ★★ Calcula KL entre dos Categorical(0.7, 0.2, 0.1) y Categorical(0.4, 0.4, 0.2). ¿Cuánto vale Jensen-Shannon?
25. ★★ Implementa tu propio cálculo de 5 $f$-divergencias y grafica la asimetría $D_f(p\|q) - D_f(q\|p)$ para 1000 pares.
26. ★★★ Sea $f(t)=(t-1)^2$. Demuestra que la divergencia asociada es $\sum (p-q)^2/q$. Vincula con $\chi^2$ clásico.
27. ★★★★ **Mini-proyecto:** comparación KL / Wasserstein en clasificación de imágenes. Usa MNIST, entrena un clasificador con pérdida KL y otro con Wasserstein. Reporta accuracy y robustez adversaria.

**Tema: dualidad de Legendre**

28. ★★★ Para Softmax($\eta_1, \eta_2, \eta_3$) con $\sum \exp(\eta_i) = 1$, encuentra la transformación de Legendre. ¿Es una involución?
29. ★★★ ★ (importante) Demuestra $D_F(p\|q) = D_{F^*}(\nabla F(q) \| \nabla F(p))$ a mano para $F(x) = x^2/2$.

### Capítulo 3 — Familias Exponenciales

**Nuevos ~20:**

30. ★★ Descompón Gamma($\alpha=3, \beta=2$) en forma exponencial. Identifica $\eta, T, A, h$.
31. ★★★ Demuestra PKD en familia Bernoulli: ¿por qué basta $T(x)=x$?
32. ★★★ ★ (crítico) Muestra que Softmax($\eta_1,\eta_2,\eta_3$) es familia exponencial. Identifica todos los componentes.
33. ★★★★ **Mini-proyecto:** compara máximo verosímil con momento matching en mezclas Gaussianas. ¿Cuándo difieren? Vincular con Pitman-Koopman-Darmois.

### Capítulo 4 — α-conexiones

**Nuevos ~25** (el capítulo necesita esto más):

34. ★★ En Bernoulli, grafica las tres geodésicas $\alpha=-1, 0, 1$ entre $p=0.2$ y $p=0.8$. Comenta cuál pasa más cerca de $p=0.5$.
35. ★★★ Demuestra que $\nabla^{(\alpha)}$ tiene torsión si y solo si la familia NO es dualmente plana.
36. ★★★★ **Mini-proyecto:** Implementa cálculo numérico de geodésica $\alpha$ en $(\mu,\sigma)$. Visualízalas en 2D. Hipótesis: ¿cuál cruza el "infinito" $\sigma=0$?

### Capítulo 5 — Inferencia

**Nuevos ~20:**

37. ★★★ Muestra que EM para mezclas Gaussianas es una sucesión de proyecciones alternadas (m-proyección y e-proyección).
38. ★★★★ **Mini-proyecto:** compara MCMC (Gibbs) vs VI en un modelo jerárquico. Reporta wall-clock y ELBO.

### Capítulo 6 — Aplicaciones

**Nuevos ~25:**

39. ★★★★ **Mini-proyecto GLM (estrella del libro):** implementa regresión Poisson con offset, regularization L2, y compara:
    - GD sobre parámetros naturales $\eta$.
    - GD sobre parámetros canónicos $\mu$.
    - Newton sobre ambos.
    - Natural gradient (Fornás).
    Reporta convergencia y métricas.

### Capítulo 7 — Avanzado

**Nuevos ~22:**

40. ★★★★ **Mini-proyecto Wasserstein:** entrena un flow normalizado (NICE/RealNVP simplificado) usando Wasserstein loss en MNIST 8x8. Reporta FID-like.

### Capítulo 8 — Hilbert (nuevo, descrito en `capitulo8-spec.md`)

**Ejercicios definidos en F4.**
- Estimado ~25 distribuidos similarmente.

---

## 4. Cómo se escriben los ejercicios (plantilla LaTeX)

Para facilitar consistencia, cada ejercicio nuevo **debe seguir este esqueleto** dentro de `*Archivos LaTeX`:

```latex
\begin{enumerate}[...]
  \item[$\star$] % Nivel 1 — rompehielos
  \textbf{[Tema corto].} % 3-5 palabras, ej. "Invariancia tensorial"
  % Texto del ejercicio (2-4 líneas)
  %
  % Pregunta LLM (1 línea)
  \textit{Pregunta a tu LLM:} «¿Por qué $[$reformular la pregunta$]$?»
  % Pista opcional
  \textit{Pista:} $[$0-2 líneas$]$
  % Criterio verificación
  \textit{Verifica con:} $[$1 línea de código o fórmula$]$

  \item[$\star\star$] % Nivel 2 — algorítmico
  % similar
```

Esto es **inversión estándar** en todos los `capituloX.tex`. Las soluciones en `respuestas.tex` van en una nueva sección:

```latex
\section*{Capítulo X — Nivel N}
\begin{enumerate}
  \item \textbf{[Tema].} \textit{Solución.}
\end{enumerate}
```

---

## 5. Archivos a tocar en F3 (implementación)

| Archivo | Cambios |
|---|---|
| `capitulo0.tex` | Añadir 1 sección "Tema: Por qué estos prerequisitos" con 30 ejercicios siguiendo plantilla |
| `capitulo1.tex` | Añadir 20 ejercicios en subsecciones existentes |
| `capitulo2.tex` | Añadir 25 ejercicios, expandiendo $f$-divergencias |
| `capitulo3.tex` | Añadir 20 ejercicios + nueva subsección sobre RKHS preliminar |
| `capitulo4.tex` | Añadir 25 ejercicios reorganizando visualizaciones |
| `capitulo5.tex` | Añadir 20 ejercicios, nueva subsección "EM como proyección" |
| `capitulo6.tex` | Añadir 25 ejercicios (mini-proyectos con datasets reales) |
| `capitulo7.tex` | Añadir 22 ejercicios, gran mini-proyecto Wasserstein |
| `capitulo8.tex` | (nuevo, descrito en `capitulo8-spec.md`) 25 ejercicios |
| `respuestas.tex` | Añadir ~190 soluciones nuevas |
| `main.tex` | Incluir `\include{capitulo8}` antes de `\backmatter` |

---

## 6. Riesgos en F3

- **LATEX overflows:** Muchos listings dentro de `\begin{lstlisting}...\end{lstlisting}` rompen el build. Mitigación: verificación con `make build` después de cada capítulo.
- **Listings demasiado largos** (código que excede `\textwidth`). Mitigación: usar `\begin{lstlisting}[basicstyle=\scriptsize\ttfamily]` para los más densos.
- **Hyperref warnings** al añadir \label/ \ref. Mitigación: usar etiquetas semánticas (`eq:bernoulli_fisher_1` en lugar de `eq:1`).
- **Conflicto con existing exercises** (numeración). Mitigación: usar `\begin{enumerate}[resume]` con tags explícitos por nivel.

---

## 7. Criterio de "hecho" para F3

- [ ] Capítulo por capítulo, los nuevos ejercicios están escritos con plantilla.
- [ ] Las soluciones correspondientes están en `respuestas.tex`.
- [ ] `make build` compila dos veces sin ERRORES (warnings tolerados).
- [ ] El PDF resultante tiene la numeración correcta y los ejercicios se ven limpios.

---

## 8. Recomendación para iniciar F3

Proceder **capítulo por capítulo**, comenzando por Cap. 0 (más fácil, menos dependencias) y terminando en Cap. 7. El nuevo Cap. 8 se hace en F5 después de F4.
