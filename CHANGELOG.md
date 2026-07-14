# Changelog — Geometría de la Información

Todas las versiones notables del libro se documentan aquí. El formato sigue (con permiso) [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/), y el versionamiento adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [v0.2.0] — 2026-07-14

Primera versión con los ocho capítulos **completamente reescritos** mediante inserciones-glue quirúrgicas estilo-ensayo, y un pase de ortografía castellana en las entradas del TOC.

### Añadido
- Rewrites completos de `Prologo.tex`, `capitulo0.tex` … `capitulo8.tex` con un patrón consistente de *signposting* ensayístico: cada definición y cada teorema se conecta con el resto del libro (motivación → invariantes → consecuencias → conexiones a capítulos siguientes).
- `CHANGELOG.md` (este archivo) — historial legible de cambios por release.
- Badge `version: v0.2.0` en `README.md`, alineado al color `Accent` (`#0F766E`) definido en `src/style-book.sty`.

### Cambiado
- `src/version.tex`: `\BookVersion` bumped de `v0.1.0` → `v0.2.0` (bump menor; sin cambios incompatibles en la API matemática del libro).
- `README.md`: badges reestructurados (license → version → math → vibe → contributions) y nueva sección «Novedades de v0.2.0» enlazando a este changelog.

### Corregido
- `src/capitulo4.tex` L41 — ortografía castellana en la entrada opcional del TOC:
  `\section[Definicion de alpha-conexiones]` → `\section[Definición de $\alpha$-conexiones]`.
- `src/capitulo4.tex` L134 — ortografía castellana en la entrada opcional del TOC:
  `\section[Geodesicas alpha]` → `\section[Geodésicas $\alpha$]`.
- `src/capitulo1.tex` L278 — guion tipográfico castellano en ejercicio final del capítulo:
  `Cramér-Rao` → `Cramér--Rao` (renderiza como em-dash `Cramér–Rao` en el PDF).

### Notas técnicas
- Tres pases de `pdflatex` confirmados sin errores fatales. Los 6 overfull `hbox` pre-existentes no son introducidos por estos cambios.
- Compilación reproducible: la `Makefile` usa `pdflatex` dos veces (refs cruzadas + TOC); `texput.log` y `*.bbl/*.blg` añadidos a `src/.gitignore`.

---

## [v0.1.0] — 2026

### Publicado
- Borrador inicial distribuido: capítulos 0–8 con material base (definiciones, teoremas, ejemplos, ejercicios), estructura tipográfica definida en `style-book.sty`, portada tipo CARTA y back-cover eclipse solar.
- Sin los rewrites-glue quirúrgicos y sin pase de ortografía castellana que llegan en v0.2.0.

---

[v0.2.0]: ver `git log v0.2.0`
[v0.1.0]: ver `git log v0.1.0`
