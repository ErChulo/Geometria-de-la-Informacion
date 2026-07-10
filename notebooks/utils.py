"""
utils.py — Helpers compartidos para los companion notebooks del libro
"Geometría de la Información".

Convención de uso (en cada notebook):

    from utils import setup_seed, plot_fisher_bernoulli, load_or_generate

    SEED = setup_seed("cap1_fisher_tensor")  # determinístico por título
    rng = np.random.default_rng(SEED)
    ...

Diseño:
  * `setup_seed(slug)` devuelve un entero estable cross-platform derivado
    del hash del título (no usamos `random.seed` para que no choque con
    nada en el kernel de Jupyter).
  * `load_or_generate(...)` carga un dataset versiónado si existe y, si no,
    genera uno sintético reproducible con la semilla pasada.
  * `plot_fisher_bernoulli(...)` es la firma estándar que cualquier
    notebook del cap1 usa para graficar I(p) = 1/(p(1-p)).
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Paths ------------------------------------------------------------------

# notebooks/ es la raíz de los companion notebooks. Asumimos que este
# archivo (utils.py) vive exactamente en notebooks/ (no en un subdir).
THIS_DIR = Path(__file__).resolve().parent
DATA_DIR = THIS_DIR / "data"
CACHE_DIR = THIS_DIR / ".cache"

DATA_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)


# --- Seed determinístico ----------------------------------------------------


def setup_seed(title: str) -> int:
    """Devuelve un entero 0 <= seed < 2**32, determinístico y platform-independent.

    El hash es SHA-256 truncado a 4 bytes, lo que:
      * No depende del PYTHONHASHSEED (que randomiza `hash()` entre procesos).
      * Es estable cross-platform (Linux + macOS; mismo slug → mismo seed).
      * Está acotado al rango válido de np.random.default_rng.
    """
    digest = hashlib.sha256(title.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % (2**32)


# --- Imports opcionales seguros --------------------------------------------


def safe_import(name: str):
    """Importa un módulo; si falla, devuelve None (no rompe el notebook)."""
    try:
        return __import__(name)
    except ImportError:
        return None


# --- Datasets --------------------------------------------------------------


def load_or_generate(
    slug: str,
    rng: np.random.Generator,
    n: int = 1000,
    fallback: Union[str, callable] = "uniform",
) -> pd.DataFrame:
    """Carga `notebooks/data/{slug}.csv` si existe; si no, genera un dataset sintético.

    Args:
        slug: nombre del archivo (sin `.csv`).
        rng: instancia de `np.random.Generator` con seed fija.
        n: tamaño del dataset sintético en fallback.
        fallback: un callable `(rng, n) -> DataFrame`, o uno de los presets
            ``"uniform"``, ``"gaussian_mixture"``, ``"bernoulli"``.

    Returns:
        DataFrame con la columna `x` (applies por defecto), o columnas según
        el preset.
    """
    path = DATA_DIR / f"{slug}.csv"
    if path.exists():
        return pd.read_csv(path)

    if isinstance(fallback, str):
        presets = {
            "uniform": _preset_uniform,
            "gaussian_mixture": _preset_gaussian_mixture,
            "bernoulli": _preset_bernoulli,
        }
        if fallback not in presets:
            raise ValueError(
                f"Preset '{fallback}' no reconocido. "
                f"Usa uno de {list(presets.keys())} o pasa un callable."
            )
        return presets[fallback](rng, n)

    return fallback(rng, n)


def _preset_uniform(rng: np.random.Generator, n: int) -> pd.DataFrame:
    return pd.DataFrame({"x": rng.uniform(-3.0, 3.0, size=n)})


def _preset_gaussian_mixture(rng: np.random.Generator, n: int) -> pd.DataFrame:
    half = n // 2
    a = rng.normal(loc=-1.0, scale=0.8, size=half)
    b = rng.normal(loc=2.0, scale=1.2, size=n - half)
    return pd.DataFrame({"x": np.concatenate([a, b])})


def _preset_bernoulli(rng: np.random.Generator, n: int) -> pd.DataFrame:
    return pd.DataFrame({"x": (rng.uniform(0, 1, size=n) < 0.35).astype(int)})


# --- Plots estándar --------------------------------------------------------


def plot_fisher_bernoulli(
    p_max: float = 0.95,
    figsize: tuple[float, float] = (8.0, 4.0),
    title: str = r"$I(p) = \dfrac{1}{p(1-p)}$ — Bernoulli",
) -> plt.Figure:
    """Graficá la métrica de Fisher de Bernoulli en (0,1) con el pico en p=1/2.

    Esta firma es estándar para los notebooks del Cap. 1 (`★` rompehielos
    sobre cálculo de Fisher). Devuelve la figura; el caller decide si
    usar `plt.show()`, `display(fig)` o guardarla.
    """
    p = np.linspace(0.01, p_max, 400)
    I = 1.0 / (p * (1.0 - p))
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(p, I, color="#0F766E", linewidth=2.0)
    ax.set_xlabel(r"$p$")
    ax.set_ylabel(r"$I(p)$")
    ax.set_title(title)
    ax.axvline(0.5, color="gray", linestyle="--", linewidth=0.8)
    ax.set_ylim(0, 20)
    return fig


# --- CLI ------------------------------------------------------------------


def _smoke_test() -> int:
    """`python -c "import utils; utils._smoke_test()"` debe devolver 0."""
    s1 = setup_seed("cap1_fisher_tensor")
    s2 = setup_seed("cap1_fisher_tensor")
    assert s1 == s2, f"Seed no determinístico: {s1} != {s2}"
    print(f"Seed determinístico OK: {s1}")
    rng = np.random.default_rng(s1)
    df = load_or_generate("iris_subsample", rng, n=5, fallback="uniform")
    assert isinstance(df, pd.DataFrame) and df.shape == (5, 1)
    print(f"load_or_generate OK: shape={df.shape}, head=\n{df.head()}")
    fig = plot_fisher_bernoulli()
    assert fig is not None
    print(f"plot_fisher_bernoulli OK: {type(fig).__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_smoke_test())
