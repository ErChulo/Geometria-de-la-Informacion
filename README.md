# 🌈🌀 **Geometría de la Información**

[![license: MIT](https://img.shields.io/badge/license-MIT-ff5fd2.svg)](./LICENSE)
[![version: v0.2.0](https://img.shields.io/badge/version-v0.2.0-0F766E.svg)]()
[![math](https://img.shields.io/badge/matemáticas-Riemann%2C%20Fisher%E2%80%93Rao-8a2be2.svg)]()
![vibe: psicodélico](https://img.shields.io/badge/vibe-psicodélico-%F0%9F%8C%88.svg)
[![PRs welcome](https://img.shields.io/badge/contributions-welcome-00c2ff.svg)]()

> ✨ *La incertidumbre como territorio; la curvatura de la creencia como brújula.*

Un libro LaTeX (~137 páginas) + cuadernos Jupyter ejecutables que enseñan la **geometría de la información** como un idioma invariante para el espacio de distribuciones de probabilidad: Fisher–Rao, divergencias de Bregman, α-conexiones de Amari, espacios de Hilbert para variables aleatorias (KRR / GP / NTK), e inferencia geométrica (EM / VI / gradiente natural).

Pensado para el lector que ya conoce cálculo, probabilidad básica y algo de álgebra lineal y quiere **convertir intuiciones sueltas sobre distribuciones en principios que sobreviven a reparametrizaciones**.

---

## 📝 Novedades de v0.2.0 (14-jul-2026)

- **Capítulos 0–8 completamente reescritos** con *signposting* ensayístico: cada definición y cada teorema se conecta explícitamente con el resto del libro (motivación → invariantes → consecuencias → enlaces hacia capítulos siguientes).
- **Pase de ortografía castellana** en tres entradas del TOC y cuerpo: `Definición` (cap4), `Geodésicas` (cap4), `Cramér–Rao` con em-dash (cap1, ejercicio final).
- **Versión bumped** a `v0.2.0` (`src/version.tex`) con badge sincronizado en este README.
- **Historial** mantenido en [`CHANGELOG.md`](./CHANGELOG.md); tag anotado `v0.2.0` en `origin`.

---

## 🎯 ¿Para qué este libro?

Cuando analistas y estudiantes aplican modelos probabilísticos (regresión logística, mezclas gaussianas, redes neuronales bayesianas, modelos de lenguaje), las preguntas centrales son:

- *¿Son comparables mis conclusiones cuando cambio de coordenadas?* (Fisher–Rao, Chentsov)
- *¿Cómo aproximo una distribución “complicada” por una familia tratable?* (proyecciones e/m, pitagórico KL)
- *¿Cómo actualizo de forma coherente?* (gradiente natural, EM geométrico, dualidad α = ±1)
- *¿Cuándo dos muestras provienen de la misma distribución?* (MMD, RKHS)

Geometría de la Información responde con **una sola maquinaria geométrica** a todas estas preguntas. Este libro es el desarrollo unificado, con motivación filosófica, derivaciones formales, ejemplos numéricos y ejercicios graduados (★ a ★★★★).

---

## 📚 Contenido de un vistazo

| Cap | Título | Foco |
|---|---|---|
| 0 | Prerrequisitos | Cálculo vectorial, probabilidad, convexidad, autodiff |
| 1 | Fundamentos | Información de Fisher, teorema de Chentsov, geometría del semiplano de Poincaré |
| 2 | Divergencias y Bregman | $f$-divergencias, KL, dualidad de Legendre, JSD, χ² |
| 3 | Familias exponenciales | Pitman–Koopman–Darmois, parámetro natural vs expectativa, mínimos suficientes |
| 4 | α-conexiones | Conexión dual, geodésicas mixtas, dualidad plana, Christoffel |
| 5 | Inferencia | e/m-proyecciones, EM geométrico, gradiente natural, Jeffreys, AIC |
| 6 | Aplicaciones | GLMs, credibilidad bayesiana, mezclas, inferencia variacional, info máx |
| 7 | Avanzado | Métrica de Fisher no estándar (Cauchy, Student), Wasserstein 1D, info de Bures |
| 8 | Geometría de Hilbert | $L^2$, RKHS, MMD, KRR / GP / NTK, puente Fisher ↔ Hilbert |

El libro se imprime a dos caras (`twoside`) con portada tipo CARTA completa y contraportada estilo eclipse solar.

---

## 🚀 Quickstart

### Construir el libro (PDF)

```bash
cd src
make           # build → genera main.pdf (~137 pp)
make clean     # borra artefactos LaTeX
make notebooks # smoke-test rápido de los notebooks
```

Requiere una distribución TeX reciente (TeXLive 2024+, `pdfLaTeX`, `latexmk`).

### Ejecutar los cuadernos (Python)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/   # carpeta con todos los .ipynb
```

Cada cuaderno fija una semilla determinística por hash del título (`setup_seed(título)`), así que dos ejecuciones con la misma versión dan los mismos números.

### Wolfram Mathematica (opcional)

Los `.nb` son complementarios para cálculos simbólicos (símbolos de Christoffel, dualidad de Legendre). Requieren Wolfram Engine 13.0+ (gratuito para uso personal).

---

## 📓 Cuadernos compañero (companion notebooks)

Cada ejercicio ★★★★ (mini-proyecto) tiene un cuaderno ejecutable en `notebooks/`. La plantilla pedagógica del cuaderno:

1. Celda inicial: cita textual del enunciado del libro + enlace a la sección.
2. `setup_seed` (reproducibilidad determinística).
3. Código numerérico paso a paso (4–8 bloques).
4. Celda final: criterio de verificación contra `respuestas.tex`.

Total proyectado: ~30 cuadernos Python + 8 Mathematica (ver `companeros-ejecutables-spec.md`).

---

## 🗂 Estructura del repositorio

```
.
├── src/                 # fuente LaTeX (capitulo[0-8].tex, respuestas, bibliografía)
│   ├── frontmatter/     # titlepage.tex (cover), backcover.tex (eclipse solar)
│   └── assets/          # cover-figure.pdf (used by titlepage)
├── notebooks/           # cuadernos Jupyter + utils.py + helpers
├── coqui-negro.jpg      # foto del coquí usada en el eclipse del back cover
├── requirements.txt     # deps Python pinned para los notebooks
├── Makefile             # build LaTeX (src/Makefile)
├── .gitignore           # ignora .pdf, .aux, .cache/, __pycache__/
├── LICENSE              # MIT
├── README.md            # este archivo
└── specs/ (md)          # critica-por-capitulo, plan-ejercicios, companeros-ejecutables, capitulo8-spec
```

---

## 📜 Licencia

MIT © 2026 Herick Lopez Cardona. Ver [LICENSE](./LICENSE) para el texto completo. Eres libre de copiar, modificar y redistribuir con atribución.

---

## 🪪 Citación

Si este libro te resulta útil en clase o en investigación, cítalo como:

```bibtex
@book{geometria_informacion_2026,
  author    = {Cardona, Herick Lopez},
  title     = {Geometría de la Información: metricas de Fisher–Rao,
               divergencias de Bregman, α-conexiones y RKHS},
  year      = {2026},
  publisher = {self-published},
  note      = {Open educational text, MIT license}
}
```

---

## 🙏 Agradecimientos

A la tradición matemática activa (Rao, Fisher, Chentsov, Amari, Čencov, Bregman) cuyo trabajo es la materia prima, a los autores de `style-book.sty` y de los paquetes LaTeX utilizados, y a los lectores y estudiantes cuyas preguntas y errores siguen alimentando revisiones.

---

<div align="center">

✷ ⋆｡° ✩ **Que tu gradiente sea suave, y tu divergencia, mínima** ✩ °｡⋆ ✷

</div>
