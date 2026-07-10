# Crítica Feroz y Útil — *Geometría de la Información*

Short name: `critica-IG`
Status: Fase 1 del plan estratégico (F1). Diagnóstico crudo antes de F2-F6.
Referencia: `src/main.tex`, `src/capitulo0.tex`–`src/capitulo7.tex`, `src/apendice_mathematica.tex`, `src/respuestas.tex`, `prerequisitos.md`.

---

## 0. Veredicto global (TL;DR)

El libro es **elegante matemáticamente** y **fiel al canon** (Amari, Chentsov, Fisher-Rao, Bregman, Pitman–Koopman–Darmois). Pero como vehículo de **auto-aprendizaje con LLMs** tiene tres déficits graves y siete mejorables:

| # | Déficit | Impacto |
|---|---|---|
| 1 | **Hueco entre teoría y código ejecutable.** Cada capítulo tiene definiciones y fórmulas pero el código es decorativo (NumPy clásico, sin reproducir resultados ni visualizar la geometría). | El alumno no puede "tocar" la geometría. |
| 2 | **Saltos argumentativos brutales.** Hay demasiados "`definimos X` → 3 párrafos → `esta conexión es profunda`". Falta el camino intermedio: dibujo, ejemplo numérico, contraejemplo. | LLM no puede "rellenar" lo que falta. |
| 3 | **Ratio ejercicios demasiado bajo vs. masa teórica.** Hay ~70 ejercicios totales pero algunos capítulos (Cap. 7) tienen 6-8. Un "experto" necesita ≥25 por capítulo en esta taxonomía. | El alumno no internaliza. |

Los 7 mejorables: motivación filosófica al inicio de cada capítulo; visualizaciones con `tikz` que faltan (geodésicas en $(\mu,\sigma)$, α-geodésica vs mixture, RKHS embedding); conexión con PyTorch/JAX (no NumPy solo); mención sistemática de "qué preguntarle al LLM"; reordenamiento Cap. 5/6 (la geometría de la inferencia y las aplicaciones a veces se solapan); inclusion de Wasserstein en Cap. 6 con código; revisión cuidadosa de los Teoremas ★★★ que tienen errores oscuros (Cap. 1, Cap. 4 Christoffel).

---

## 1. Por capítulo

### Capítulo 0 — Ejercicios de Prerrequisitos (`capitulo0.tex`)

**Fortalezas.** Cubre 7 frentes (álgebra lineal, cálculo multivariado, probabilidad, estadística, convexo, geo. diferencial, info. theory, procesos estocásticos). Es la columna vertebral del libro.

**Crítica feroz.**
- **No hay motivación.** Arranca con "edding de espacios vectoriales" sin decir para qué. *Decir al inicio: "Si quieres entender Fisher-Rao, antes tienes que manejar estas herramientas como respirar."*
- **Las respuestas son minúsculas.** `"Sí; el determinante es $-2\neq 0$"` no enseña a pensar. El alumno no puede distinguir entre un cálculo y una verificación. Reemplazar por respuestas con **una línea de intuición** al inicio.
- **Falta código computacional.** "¿Cómo verifico que una matriz es PD en Python?" — debería ser 2-3 ejercicios con `np.linalg.eigvalsh`, condicionamiento, etc.
- **No hay proyectos mini.** Para 7 temas × 3 niveles, son 21 ejercicios cuando deberían ser 60+.
- **Sin graduación visual de la dificultad** hasta finales (cap 10+). Las estrellas ★ están en Cap. 1-7; aquí no hay.

**Sugerencias concretas.**
- Aumentar a ~30 ejercicios (5 por sección × 6 secciones = 30).
- Añadir una pregunta filosófica al final: *"¿Por qué la covarianza es la métrica natural para variables aleatorias? ¿Por qué el Hessiano define una distancia?"* (esto prepara Hilbert).
- Incluir **ejercicios-traviesos** que usan LLMs: *"Pídele a tu LLM que demuestre que $A^TA$ es PSD para $A\in\mathbb{R}^m\times\mathbb{R}^n$ con distintos $m,n$. Compara con la prueba simbólica."*

---

### Capítulo 1 — Fundamentos Geométricos (`capitulo1.tex`)

**Fortalezas.** Bien hilado: espacio de probabilidades → variedades → métrica de Fisher → invariancia (Chentsov) → cota CR. Ejemplos de cálculo (Bernoulli, Poisson, Exponential, Normal) bien elegidos.

**Crítica feroz.**
- **El teorema de Chentsov aparece sin prueba ni intuición.** Dice "el único" pero no muestra geometría de Choquet ni por qué es razonable. Es el teorema MÁS importante del libro y lo despacha en una idea de 5 líneas.
- **La métrica de Fisher en 2D (Normal) se reduce a 4 renglones.** Un alumno no sabe visualizar $(\mu,\sigma)$ como semiplano hiperbólico.
- **Caso Bernoulli: $I(p)=1/(p(1-p))$ sin discusión intuitiva.** ¿Por qué diverge? ¿Por qué simétrico en $p=0.5$? Sin una sola palabra.
- **Curvatura escalar = 2 para Bernoulli** sin motivación.
- **El "qué gana con GI" no tiene ejemplo concreto.** Dice "cualquier conclusión derivada… es independiente de cómo parametrices". Muéstralo: reparametriza Bernoulli con $\eta=\text{logit}(p)$, calcula $I(\eta)$, verifica $\eta(-p)=??$.
- **Una sola ecuación y no hay código de visualización.** Falta: plot de geodésica en $(\mu,\sigma)$ con un par de puntos, plot de $I(p)$ vs $p$.

**Sugerencias concretas.**
- Antes de Chentsov, una **sub-sección de motivación geométrica**: ¿por qué la covarianza del score?
- Después del Teorema de CR, **2-3 ejercicios** que pidan: *"Re-deriva la covarianza del score usando exactamente la definición de $I(\theta)=\text{Var}(\partial\ell/\partial\theta)$. Verifica numéricamente muestreando."*
- **Inclusión de $\eta=\text{logit}$ para Bernoulli** como ejemplo de reparametrización: el alumno ve explícitamente que la información se transforma como un tensor 2-covariante.
- Una figura TikZ del semiplano de Poincaré con la geodésica entre dos Gaussianas.

---

### Capítulo 2 — Divergencias y Geometría de Bregman (`capitulo2.tex`)

**Fortalezas.** La estructura KL → $f$-divergencias → Bregman → dualidad de Legendre → teorema pitagórico es el camino correcto. Las demostraciones de no-negatividad (Gibbs) están bien expuestas.

**Crítica feroz.**
- **El teorema pitagórico está mal dibujado.** La figura TikZ muestra un triángulo rectángulo pero el ángulo "recto en el sentido de KL" no es un ángulo euclidiano — es una **identidad entre divergencias**. Etiquétalo bien: *"No hay perpendicularidad espacial aquí; hay ortogonalidad en el sentido de la segunda variación."*
- **Las $f$-divergencias aparecen como tabla** sin motivación. ¿Por qué hay 6 funciones convexas emblemáticas? ¿Por qué no 60?
- **La dualidad de Legendre-Fenchel se introduce pero el lector no sabe por qué le importa.** Un alumno lo lee y dice "OK, una nueva transformada", pero no la conecta con nada.
- **El código es pobre.** Solo 3 listing, todos mecánicos. Falta: visualizar la divergencia de Bregman como área entre la curva y la tangente; experimentar con la asimetría ($D_KL(p||q) \neq D_KL(q||p)$) graficando ambas.

**Sugerencias concretas.**
- **Nueva subsección: asimetría de KL visualizada.** Una figura TikZ donde $D(p||q)$ y $D(q||p)$ se pintan como áreas distintas bajo la misma curva. (Esta sola figura vale 5 páginas de explicación.)
- **Ejercicios de "meta-razonamiento":** *"Demuestra que toda $f$-divergencia es invariante bajo cambio de variable biyectiva medible. ¿Qué propiedad de $f$ lo garantiza?"* — un ejercicio que el alumno NECESITA discutir con un LLM porque exige reconocer cuándo una propiedad es topológica y cuándo algebraica.
- **Añadir sección "Por qué KL falla"** mostrando un ejemplo en el que dos distribuciones tienen soportes disjuntos y KL($\cdot$) = $\infty$.

---

### Capítulo 3 — Familias Exponenciales y Variedades Dualmente Planas (`capitulo3.tex`)

**Fortalezas.** Pitman-Koopman-Darmois aparece con claridad. La tabla de "¿es exponencial?" con Bernoulli, Cauchy, $U(0,\theta)$ es muy efectiva. Dualidad de Legendre bien enlazada.

**Crítica feroz.**
- **PKD ocupa solo 1 página pero es FUNDAMENTAL.** Merece una subsección propia mostrando las hipótesis (suficiencia de dimensión finita, identificabilidad) con un ejemplo.
- **Dualidad $\mu = \nabla A(\eta)$ se da con una igualdad, no con una intuición geométrica.** Falta: visualización de cómo el Hessiano $\nabla^2 A$ es la matriz de covarianza del estadístico suficiente. Es el primer puente con Hilbert.
- **Falta la conexión con machine learning moderna.** Softmax = exponential family de categóricas. Regresión logística = Bernoulli en familia exponencial. Sin esta conexión, el alumno se queda en los años 80.
- **El ejemplo Gamma tiene $\eta = \alpha - 1$ y $T(x) = \log x$.** El lector promedio no entiende por qué $\log x$. ¿Por qué "log-statistic"? Esto conecta directamente con **KX 21** (Wald) y con la RKHS.

**Sugerencias concretas.**
- **Nueva sección 3.X: "Familia exponencial y RKHS".** Mostrar que si $T(X) \in L^2$ y la acotas en un espacio con kernel, obtienes un RKHS. Esto es el puente con Cap. 8 (Hilbert).
- **Ejercicios de "verificación computacional con JAX":** *"Calcula $\nabla^2 A(\eta)$ para función exponencial con $\eta$ = log-rate y verifica que coincide con la varianza de $T$."* (El autodiff lo hace trivialmente.)
- **PKD: añadir prueba detallada** o al menos, una "intuición topológica" suficiente para discutirla con un LLM.

---

### Capítulo 4 — α-conexiones de Amari (`capitulo4.tex`)

**Fortalezas.** La fórmula $\nabla^{(\alpha)} = (1+\alpha)/2 \nabla^{(1)} + (1-\alpha)/2 \nabla^{(-1)}$ es elegante y bien presentada. La mención de dualidad.

**Crítica feroz.**
- **Es el capítulo más abstracto y el menos motivado.** "$\alpha$ elige la manera de medir rectitud" — pero ¿cuándo importa? ¿Cómo decides si usar $\alpha = -1,0,1$? No hay un solo ejemplo aplicado.
- **Símbolos de Christoffel en Bernoulli se vuelven fórmulas en línea.** La fórmula `Gamma^{(α)}_{ijk} = E[½(∂³ log p ... + ...])]` no se interpreta.
- **Tensor de curvatura α = ±1** sin ejemplo concreto, sin visualización de cómo la geodésica α se ve diferente de otras.
- **El "qué gana con GI" es declarativo**, no demuestra cómo la elección de α cambia la respuesta en inferencia.

**Sugerencias concretas.**
- **Reorganizar el capítulo como: motivación → definiciones → ejemplos completos en Bernoulli → generalización.** Pon un EJEMPLO COMPLETO de geodésica α en $(\mu,\sigma)$ cuando mucho en la página 2.
- **Visualización TikZ required:** la misma figura Cap. 1 pero mostrando las tres geodésicas α=-1,0,1 entre dos puntos en el plano $(\mu,\sigma)$.
- **Ejercicio estrella:** *"Demuestra empíricamente que, en el caso de mezcla de dos Gaussianas con parámetros conocidos, la α-proyección con α=-1 preserva los momentos esperados pero la α-proyección con α=+1 preserva los parámetros naturales."* Esto es exactamente el tipo de ejercicio que un LLM puede guiar paso a paso.

---

### Capítulo 5 — Geometría de la Inferencia (`capitulo5.tex`)

**Fortalezas.** Cramér-Rao, suficiencia, Rao-Blackwell correctamente enunciados. Código de "MLE y varianza asintótica" funciona.

**Crítica feroz.**
- **Hay solapamiento con Cap. 1 y Cap. 6.** Cap. 1 introduce Fisher; Cap. 5 lo repite; Cap. 6 lo aplica. Sugerencia: fusionar o referirse a Cap. 1 sin redefinir.
- **EM como proyección alternada** se menciona ROZANDO pero no se demuestra. Un alumno que termina Cap. 5 debería poder reproducir el paso E y M geométricamente.
- **No se discute LAN (Local Asymptotic Normality) de Le Cam** — y es el camino para conectar Fisher con inferencia moderna (test序, Bernstein-von Mises, Hájek convolution theorem).
- **El código no incluye estimación eficiente** (mínima varianza). Solo compara MLE.
- **Falta discusión del "gradiente natural ≈ scoring de Fisher"**, que es el verdadero punto elegante.

**Sugerencias concretas.**
- **Fusionar Cap. 1 y Cap. 5** (Fisher como métrica → cómo se usa en inferencia) sería coherente, pero es un cambio MAYOR; mejor añadir referencias cruzadas explícitas.
- **Nueva subsección: EM como proyecciones alternadas en KL.** Mostrar con 2 distribuciones simples (mezcla de 2 Gaussianas) la trayectoria de parámetros en el plano $(\mu_1,\mu_2)$.
- **Mini-proyecto:** *"Reproduce el experimento clásico de mostrar que MLE no es eficiente cuando la dimensión del parámetro crece con $n$ (caso no regular). Discute con tu LLM por qué Cramér-Rao no se aplica."*

---

### Capítulo 6 — Aplicaciones (`capitulo6.tex`)

**Fortalezas.** Cubre 4 dominios reales (credibilidad, ML, VI, gradiente natural). Menciona Poisson-Gamma con detalle.

**Crítica feroz.**
- **El código usa `iris` completo, no ejemplos sintéticos controlados.** El alumno no puede "experimentar" — solo ejecuta un bloque. Un buen mini-proyecto deja los datos como argumento.
- **Gradiente natural sin comparación convincente con GD.** Falta un plot de loss vs iteraciones para un problema con condición mala.
- **VI sin discutir la elección de familia variacional.** Si $q$ se elige mal, ¿qué pasa? ¿Qué divergencia quedó?
- **Credibilidad sin suficientes ejercicios** — son 8 ejercicios en una sola subsección.

**Sugerencias concretas.**
- **Mini-proyecto ★★★★:** *"Implementa un comparador GD vs NG en regresión logística con dos features de escalas muy distintas ($X_1 \sim U(0,1)$, $X_2 \sim U(0, 1000)$). Reporta # iteraciones a convergencia. Explica por qué NG es invariante."*
- **Ejercicios aplicados:** un problema con datos reales (e.g., reclamos de seguros de un dataset público) + credibilidad.
- **Comparación GLM/MCMC:** "cómo hacer credibilidad con muestreo, no con conjugadas."

---

### Capítulo 7 — Temas Avanzados (`capitulo7.tex`)

**Fortalezas.** Cubre cuantica, Wasserstein, transporte óptimo. Mención de bath normalization como proyección.

**Crítica feroz.**
- **Wasserstein y Bures introducidos sin rigor.** Wasserstein $W_1$ y Kantorovich-Rubinstein sin motivación. Bures sin ejemplo de qubit.
- **"Aprendizaje de variedades" (manifold learning) muy superficial** — mencion Isomap/LLE/t-SNE y les da una oración. Esto es un agujero pedagógico.
- **α-β divergencias** sin ejemplo.
- **Casi 0 ejercicios** (~8 vs los ~30 de Cap. 1).
- **No menciona Jacobian-based, Wasserstein gradient flow, Score-based generative models** — la conexión moderna con deep learning.

**Sugerencias concretas.**
- **Fusión con Cap. 6**: mover Wasserstein a Cap. 6 (aplicaciones) como "comparación con KL".
- **Aumentar ejercicios a 25**: distribuidos entre α-β, Wasserstein, Bures, gradient flows.
- **Mini-proyecto estrella:** *"Implementa gradient flow de Wasserstein (algoritmo de Jordan-Kinderlehrer-Otto) para conectar dos distribuciones Gaussianas 1D. Visualiza la trayectoria en 2D."*

---

### Apéndice Mathematica (`apendice_mathematica.tex`)

**Fortalezas.** Rutinas multiparamétricas y uniparamétricas bien estructuradas. Funciones comentadas.

**Crítica feroz.**
- **Las rutinas no se ejercitan en los capítulos.** Apéndice "muerto" — el alumno lo ve pero no sabe cuándo aplicarlo.
- **No hay un apéndice análogo en Python/JAX** — los capítulos usan Python pero el apéndice es Mathematática. Inconsistencia para auto-aprendizaje.
- **Las firmas de las funciones asumen Mathematica, no Wolfram Engine gratuito o wolframscript.** Para un alumno sin licencia Mathematica, este apéndice es inútil.

**Sugerencias.**
- Convertir en `apendice_python_fisher.md` con NumPy+JAX (accesible) y mantener Mathematica aparte como bonus.
- Crear un notebook Jupyter que use las rutinas para reproducir el experimento del capítulo.

---

## 2. Conclusiones Críticas → Input para F2-F6

Con base en este diagnóstico, **F2-F6 deben**:

**(F2) Crecer ejercicios** a:
- 30 en Cap. 0, 30 en Cap. 1, 30 en Cap. 2, 30 en Cap. 3, 30 en Cap. 4, 25 en Cap. 5, 30 en Cap. 6, 25 en Cap. 7.
- Total ~210 nuevos ejercicios, distribuidos en 4 niveles (★, ★★, ★★★, ★★★★).
- Al menos **30 mini-proyectos** globales (4-5 por capítulo Cap. 1-7).

**(F3) Implementar esos ejercicios** con sus soluciones completas en `respuestas.tex`.

**(F4-F5) Capítulo Hilbert** diseñado para añadir lo que falta en Cap. 3: el puente entre exponential families y RKHS, más el marco $L^2$ de variables aleatorias con covarianza como Gram, mean embeddings y MMD.

**(F6) Validar** todo con `make build` sin warnings.

---

## 3. Riesgo si no se hace nada

El alumno intenta "auto-aprender con LLMs" pero:
1. Pega una definición al LLM y el LLM responde correctamente, pero el alumno no tiene cómo verificar empíricamente.
2. Hace ejercicios mecánicos que no lo llevan a experto.
3. Pierde la motivación porque 30% del libro son fórmulas que no puede "tocar".

Las fases F2-F6 atacan exactamente esto.
