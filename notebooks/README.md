# 🌀 Companion Notebooks — *Geometría de la Información*

Cuadernos ejecutables que acompañan los mini-proyectos ★★★★ del libro
[*Geometría de la Información*](../README.md). Cada cuaderno replica un
enunciado del libro y produce los resultados referenciados en el
`\subsection*{Verifica con:}` del libro.

> 📖 Cada `.ipynb` cita la sección del libro al inicio (celda 0).
> 🔗 Cada ★★★★ en `capitulo[1–8].tex` enlaza a su notebook vía `\href{}` inline.

---

## 📦 Instalación

Requiere Python ≥ 3.10. Las dependencias pinned viven en `requirements.txt`.

```bash
# desde el directorio raíz del proyecto (donde está requirements.txt)
python -m venv .venv
source .venv/bin/activate     # Linux / macOS
# .venv\Scripts\activate      # Windows PowerShell

pip install --upgrade pip
pip install -r requirements.txt
```

> **Nota sobre PyTorch:** el `requirements.txt` usa el build CPU
> (`+cpu`). Si tienes GPU NVIDIA/CUDA y quieres usar aceleración:
> ```bash
> pip install torch==2.4.0+cu118 torchvision==0.19.0+cu118 --index-url https://download.pytorch.org/whl/cu118
> ```

> **Binder** (opcional): el repo está configurado para correr notebooks
> en [Binder](https://mybinder.org/) — busca el badge en este README
> (Fase 4 lo activará). El runtime ya tiene PyTorch CPU preinstalado.

---

## 🧭 ¿Cómo correr un notebook?

```bash
# 1. Lanza Jupyter (notebook clásico)
jupyter notebook notebooks/

# 2. Abre cap1_fisher_tensor.ipynb en el browser.

# 3. Run All (Cell → Run All). Los notebooks son auto-contenidos:
#    el primer bloque instala el seed determinístico,
#    los siguientes reproducen el resultado del libro.

# Para CLI (headless):
jupyter nbconvert --to notebook --execute \
    notebooks/cap1_fisher_tensor.ipynb \
    --output cap1_fisher_tensor_executed.ipynb
```

---

## 🌱 Reproducibilidad

- Cada notebook fija `SEED = setup_seed("cap{N}_{slug}")` al inicio.
  El seed es **determinístico y cross-platform** (hash SHA-256 del slug),
  así que el mismo cuaderno produce los mismos números siempre.
- Si cambias el seed explícitamente, los resultados cuantitativos cambian
  pero las conclusiones son idénticas.

---

## 🧱 Convenciones

| Aspecto | Convención |
|---|---|
| Naming | `cap{N}_{slug}.ipynb` y `cap{N}_{slug}.nb` (Mathematica) |
| Slugs | kebab-case (e.g., `cap2_kl_jensen_shannon`) |
| Directorio | `notebooks/` al raíz, paralelo a `src/` (independiente del build LaTeX) |
| Imports | siempre empezar con `from utils import setup_seed, …` |
| Primera celda markdown | cita `## Libro: §X.Y del Capítulo Z — Título` + quote del enunciado verbatim |
| Última celda markdown | `@ Verifica con:` — qué línea/output debe coincidir con `respuestas.tex` |
| Datos | sintético + sklearn built-ins (iris, MNIST 8×8) + CSVs propios en `data/` + grandes opcionales en `.cache/` |
| Math sym | `numpy/scipy/sklearn/statsmodels` + opcional `torch/jax` |

---

## 🗂 Estructura actual

```
notebooks/
├── README.md           # este archivo
├── utils.py            # helpers compartidos
├── data/.gitkeep       # datasets versionados pequeños (≤1MB)
├── .cache/             # GITIGNORED; descarga opcional grande
├── cap0_prerequisites.ipynb
├── cap1_fisher_tensor.ipynb
├── ...
└── cap8_hilbert_krr_gp_ntk.ipynb
```

---

## 💡 Smoke test rápido (sin abrir Jupyter)

```bash
# Verifica que el setup funciona sin correr nada
python -c "import sys; sys.path.insert(0, 'notebooks'); import utils; exit(utils._smoke_test())"

# O vía Makefile (target notebooks-fast del proyecto raíz)
make -C src notebooks-fast
```

---

## 🤝 Cómo contribuir un nuevo notebook

1. Usa la herramienta `make notebooks-fast` para correr el smoke test antes.
2. Sigue las convenciones anteriores (slug, celdas 0/final).
3. Si el notebook necesita CSV ≤ 1MB, commiteálo en `data/{slug}.csv`.
4. Si necesita datos grandes, **no** los commitees; usa `notebooks/.cache/`
   (gitignored) y descarga condicionalmente.
5. Borrá los outputs molestos antes de commit:
   ```bash
   jupyter nbconvert --clear-output --inplace notebooks/cap{N}_{slug}.ipynb
   ```

---

## 📚 Catálogo (en construcción)

| Cap | Notebook | Tipo | Enunciado |
|---|---|---|---|
| 0  | `cap0_prerequisites.ipynb` | intro | numpy/scipy warm-up |
| 1  | `cap1_fisher_tensor.ipynb` | ★ | Fisher como tensor |
| ... | ... | ... | ... |

(Ver `companeros-ejecutables-spec.md` para el catálogo completo de 30.)
