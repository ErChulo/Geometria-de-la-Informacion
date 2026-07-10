# `companeros-ejecutables-spec.md`

> **Short name:** `companeros-ejecutables`
> **Status:** Diseño previo a la implementación. NO se han hecho cambios al código aún.
> **Trigger:** Suggest followup tras F6 ~ "¿Publica companion notebooks ejecutables para los ★★★★ mini-proyectos?"

---

## 1. Filosofía y objetivo

El libro (*Geometría de la Información*, LaTeX, ~133 pp) ya define los enunciados de los mini-proyectos ★★★★ en `capitulo[1–8].tex`, con la plantilla pedagogía-llm (Pregunta/Pista/Verifica-con). **Lo que falta**: ejecución real y verificable. El propósito de los "Compañeros Ejecutables" es dar al lector + LLM un punto de partida copy-paste-run cada vez que aparezca un ★★★★.

Tres propiedades deseadas:

1. **Reproducible offline.** Cualquier notebook corre end-to-end sin instalación extra más allá de un `pip install -r requirements.txt`, sin claves de API, sin descargas masivas (excepto datos grandes opcionales vía URL con cache).
2. **Bilingüe Python + Mathematica.** Python para numérico/ML, Mathematica para simbólico (Christoffel, Legendre, métrica de Fisher de Pareto). Menos duplicación: cada ejercicio elige el lenguaje que aporta más.
3. **Bidireccional libro ↔ repo.** Cada ★★★★ cita su notebook inline (`\href{...}`); cada notebook referencia la sección del libro en una celda markdown inicial.

## 2. Alcance (de las 4 rondas de entrevista)

### 2.1 Cobertura de capítulos
- **Todos los capítulos** reciben al menos un notebook introductorio (cap0 → cap8, 9 notebooks).
- **Mini-proyectos ★★★★** reciben un notebook dedicado cada uno (≈15 notebooks en cap6/7/8, donde están los ★★★★ más algorítmicos).
- **Total: ~30 notebooks** distribuidos como:
  | Cap | Notebooks | Tipo |
  |---|---|---|
  | 0 | 1 | intro prerequisitos (numpy/scipy) |
  | 1 | 2 | intro Fisher + Chentsov empírico (★) |
  | 2 | 3 | KL/f-div/Bregman/Bernoulli KL numeric |
  | 3 | 3 | Exp-fam decomposition + Softmax PKD + Mixture normal |
  | 4 | 4 | α-geodesic visualizer + Christoffel + Curvature + Duality |
  | 5 | 4 | Information + Cramér-Rao + MLE proj. + Cauchy not exp |
  | 6 | 5 | Credibilidad + Cross-entropy=Bregman + GLM mini-proy ★★★★ |
  | 7 | 5 | Cauchy Fisher + Bures qubit + Wasserstein 1D + t-Student ★★★★ |
  | 8 | 3 | KRR/GP/NTK ★★★★ + Hilbert-statistical bridge ★★★★ |
  | **TOTAL** | **30** | |

### 2.2 Formato y cantidad
- **Jupyter `.ipynb`** (Python, ejecutable).
- **Wolfram Mathematica `.nb`** (simbólico, ejecutable en Wolfram Engine / wolframscript).
- **Py complementario a MMA**: Python para numérico/ML; Mathematica donde aporta algebra simbólica que Python no hace bien (símbolos de Christoffel, dualidad de Legendre de Gamma, etc.).

## 3. Convenciones

### 3.1 Naming
- `notebooks/cap{N}_{slug}.ipynb` para Python; `.nb` para Mathematica.
- Slugs kebab-case (e.g., `cap2_kl_jensen_shannon.ipynb`).
- Directorio de datos: `notebooks/data/{filename}.csv|npy`.
- Utilidades comunes: `notebooks/utils.py` (Python), `notebooks/utils.m` (Mathematica).

### 3.2 Estructura de cada notebook (Python)
1. **Celda 0 (markdown):** Referencia al libro: `## Libro: §X.Y del Capítulo Z — <Título>`. Quote del enunciado del ★★★★ verbatim.
2. **Celda 1 (code):** Imports + `np.random.seed(SEED)` donde `SEED = abs(hash(título)) % 2**32`. Reproducibilidad determinística.
3. **Celda 2 (markdown):** "@ Pregunta a tu LLM: «¿…?»" — 1 línea, copiada del enunciado del libro.
4. **Celda 3+: Código secuencial con 4–8 pasos lógicos** (cargar datos → función principal → plot si aplica → afirmación/impresión clave).
5. **Celda final (markdown):** "@ Verifica con: «…»" — qué línea/fórmula/output debe coincidir con la respuesta del libro (sección respuestas.tex).

### 3.3 Estructura de cada notebook (Mathematica)
1. Cell 0 (texto): Mismo bloque markdown de referencia al libro.
2. Cell 1 (input): `SeedRandom[IntegerPart[27 Hash[ToString[Title]]]];` reproduce el seed determinístico.
3. Cells 2+: Comandos secuenciales con bloques `(* Comentario *)` cortos. Símbolos de Christoffel vía `ChristoffelSymbol[g, {i, j, k}]` de paquete `RiemannianGeometry`; divergencias/duales con función custom `kullbackLeibler[p_, q_] := ...`.

## 4. Stack y dependencias

### 4.1 Python (`requirements.txt` con versiones pinned)
```
numpy==1.26.4
scipy==1.13.0
matplotlib==3.9.2
scikit-learn==1.4.2
torch==2.4.0
torchvision==0.19.0
jax==0.4.30
jaxlib==0.4.30
statsmodels==0.14.2
pandas==2.2.2
```

### 4.2 Mathematica
- Versión mínima Wolfram 13.0 LTS.
- Paquetes necesarios: `RiemannianGeometry` (símbolos de Christoffel, Riemann tensor), `VariationalMethods` (Legendre), `VectorAnalysis` (cuando se usen índices).

## 5. Datos

Política mixta, decidida en ronda 2:
- **Sintético** prioritario (reproducible, sin internet). Generadores `np.random.default_rng(seed)`.
- **sklearn built-ins** (`from sklearn.datasets import load_iris, fetch_openml`) para los ★★★★ con dataset real pequeño: iris, MNIST 8×8, diabetes, California Housing.
- **CSVs propios** (`notebooks/data/{slug}.csv`) ≤1 MB para ejemplos custom (e.g., tabla de credibilidad acturarial).
- **Datasets grandes opcionales** (MNIST 60k, etc.) vía URL en README con cache local en `notebooks/.cache/`. El notebook los descarga sólo si `notebooks/.cache/file.npz` no existe — fallback a sintético si no hay conexión.

`.gitignore` para `notebooks/.cache/` (datos descargados masivos), `__pycache__/`, `.ipynb_checkpoints/`, `*.pyc`.

## 6. Reproducibilidad

De la ronda 3:
- **Tests:** sin CI; autor regenera manualmente. Cada notebook se ejecuta al cierre de F3) en su IDE. Documenta el comportamiento esperado en una celda "Esperado:" antes del output para comparación.
- **Output handling:** `.gitignore` para `__pycache__/`, `.ipynb_checkpoints/`, `*.pyc`, `notebooks/.cache/`. Los notebooks commiteados **con outputs** limpios sólo si el autor decide (`jupyter nbconvert --clear-output` antes de commit).
- **Seed RNG:** determinístico por título: `SEED = abs(hash("cap{N}_{slug}")) % 2**32` en Python; `SeedRandom[IntegerPart[27 Hash[ToString["Cap N: Slug"]]]]` en Mathematica. Si el lector cambia el seed, los resultados cuantitativos cambian pero las conclusiones son idénticas.

## 7. Layout físico

```
proyecto/
├── src/
│   ├── capitulo[0-8].tex       # LaTeX (existente)
│   ├── respuestas.tex
│   └── ...
├── notebooks/                  # NUEVO, al raíz, paralelo al src/
│   ├── cap0_prerequisites.ipynb / .nb
│   ├── cap1_fisher_tensor.ipynb / .nb
│   ├── cap1_chentsov_empirical.ipynb / .nb
│   ├── ...
│   ├── cap8_hilbert_krr_gp_ntk.ipynb / .nb
│   ├── cap8_hilbert_statistical_bridge.ipynb / .nb
│   ├── data/
│   │   ├── iris_subsample.csv
│   │   └── credibility_table.csv
│   ├── utils.py              # carga_dataset(), fisher_analytic(), etc.
│   ├── utils.m               # paquete Mathematica: kullbackLeibler[], legendreDual[]
│   ├── README.md             # cómo correr los notebooks
│   └── .cache/                # GITIGNORED; MNIST 60k, etc.
├── Makefile                    # añadir target `notebooks-fast`, `notebooks-all`
├── requirements.txt            # PINNED, ver §4.1
└── .gitignore                  # nuevo: notebooks/.cache/, __pycache__, *.pyc, *.ipynb_checkpoints/
```

Justificación de "notebooks/ al raíz" (decisión de ronda 4): el build LaTeX no necesita los notebooks; viven independientemente de `src/`. Permite más fácil publicación como repo aparte en el futuro, sin tocar el árbol `src/`.

## 8. Citación desde el libro

Cada mini-proyecto ★★★★ al final de su enunciado añade una línea inline (estilo hyperlink LaTeX):

```latex
\textit{Acompañante ejecutable:} \href{https://github.com/heeckh/geometria-IG/blob/main/notebooks/cap8_hilbert_krr.ipynb}{notebooks/cap8_hilbert\_krr.ipynb} (Python) y \href{https://github.com/heeckh/geometria-IG/blob/main/notebooks/cap8_hilbert_krr.nb}{cap8\_hilbert\_krr.nb} (Mathematica).
```

25 ejercicios ★★★★ reciben este bloque (~4–6 líneas por ejercicio). Pasada de compilación con `make build` no necesita resolver los hyperlinks (compilan incluso sin internet).

Texto LaTeX adicional que se añade a `capitulo[6,7,8].tex`: solo el bloque `\textit{Acompañante ejecutable:}` después de cada enunciado ★★★★. Localizar exactamente cuáles (de los 30 ★★★★ listados en el plan-ejercicios.md) recibirán el link es manual y debe coordinarse con los nuevos enunciados añadidos en F3.

## 9. Publicación

De ronda 4:
- **GitHub único** en el repo del libro (`notebooks/`).
- **Binder** adicional: badge "Open in Binder" en `notebooks/README.md` y en la tabla centralizada.

Configuración Binder:
- `notebooks/binder/environment.yml` con las pinned dependencies de Python.
- `notebooks/binder/postBuild` ejecuta `pip install -e .` (futuro si se crea paquete) o cualquier notbook hook.
- URL del binder: `https://mybinder.org/v2/gh/heeckh/geometria-IG/main?filepath=notebooks/`

Costo: configurar `binder/` con ~20 líneas YAML. Único punto frágil: que Binder mantenga el runtime estable con PyTorch+torchvision (a veces corta a <500MB).

**NO** se elige GitHub Pages ni Colab (decisiones de ronda 4 lo descartaron).

## 10. Riesgos y mitigaciones

| # | Riesgo | Mitigación |
|---|---|---|
| 1 | MNIST 60k no descarga → notebook falla en Binder | Fallback sintético (mini-MNIST desde `sklearn.datasets.load_digits()` que es 8×8 e inline). |
| 2 | PyTorch cambia API entre versiones | `torch==2.4.0`, `torchvision==0.19.0` pinned. |
| 3 | Mathematica .nb no ejecuta sin licencia Wolfram | README declara "wolframscript o Wolfram Desktop ≥ 13". Los .ipynb son el camino principal; .nb es bonus opcional. |
| 4 | Outputs muy grandes (plots) inflan el repo | `.gitignore` + nbconvert --clear-output antes de commit. |
| 5 | Notebook no coincide con respuesta en libro | Celda final `@ Verifica con:` referencia exactamente la sección de respuestas.tex. |
| 6 | Browser-render del .ipynb en GitHub da basura (en particular, símbolos de Christoffel) | README declara "abrir localmente con VS Code + Jupyter". |
| 7 | Seed determinístico por hash() de Python es platform-dependent | Versión Python del hash es estable (no randomiza). Documentado en utils.py. |
| 8 | Falta de coherencia entre los libros Python: cada autor usa su propio estilo | `notebooks/utils.py` con: `setup_seed(slug)`, `load_or_generate(slug)`, `plot_fisher()` centralizados. |

## 11. Criterio de "hecho"

- [ ] `notebooks/README.md` explica instalación y ejecución.
- [ ] 30 notebooks par Python (15 .ipynb mínimo viables; los demás en drafts).
- [ ] 8 notebooks Mathematica (.nb) cubriendo los ejercicios simbólicos principales.
- [ ] `requirements.txt` pinned con todas las librerías de §4.1.
- [ ] `notebooks/utils.py` + `notebooks/utils.m` con helpers compartidos.
- [ ] `Makefile` target `notebooks-fast` que ejecuta los 5-8 más rápidos como smoke test.
- [ ] Citas inline añadidas a cada ★★★★ del libro (cap1-cap8) con hyperlinks al repo.
- [ ] `notebooks/binder/environment.yml` y binder funcionando (badge verificado).
- [ ] `.gitignore` actualizado.
- [ ] Compilación LaTeX no afectada (los hyperlinks son opcionales para LaTeX; se compilan sin internet).

## 12. Plan de implementación sugerido (~5 fases)

1. **Setup Fase:** crear `notebooks/`, `requirements.txt`, `utils.py`, `.gitignore`, README inicial. **1 sesión.**
2. **Notebook piloto:** 1 notebook end-to-end (e.g., `cap1_fisher_tensor.ipynb`) con seeds determinístico, datos sintéticos, plot, verificación. Valida el patrón antes de los 30 restantes. **1 sesión.**
3. **Notebooks básicos (cap0-cap5):** 15 notebooks cubriendo los capítulos introductorios y teóricos. **2-3 sesiones.**
4. **Notebooks avanzados (cap6-cap8) + Mathematica:** 15 notebooks Python + 8 Mathematica, incluyendo ★★★★. **3-4 sesiones.**
5. **Integración con libro + Binder:** citas inline en `cap6/7/8.tex`, badge Binder, tabla centralizada. **1 sesión.**

Total estimado: **8-10 sesiones.**

## 13. Decisiones explícitas del usuario (de las 4 rondas)

A tener presente durante la implementación (para no renegociar):

- **Ronda 1:** Cobertura = todos los capítulos + solo ★★★★. Cantidad ≈ 30. Formato = `.ipynb` + `.nb`.
- **Ronda 2:** Python complementario a MMA (no emparejado). Stack = NumPy/SciPy/sklearn/PyTorch/JAX/statsmodels. Datos = sintético + sklearn + CSV + URL descargables.
- **Ronda 3:** Tests: ninguno (manual). Outputs: gitignored. Seed: hash del título.
- **Ronda 4:** Layout: `notebooks/` al raíz. Cita libro: inline `\href`. Publicación: GitHub + Binder.
