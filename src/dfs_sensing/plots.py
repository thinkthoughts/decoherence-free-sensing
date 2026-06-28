"""Plot helpers for decoherence-free sensing notebooks."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .core import heisenberg_variance, lieb_mattis_variance_bound, sql_variance


def plot_scaling(output: str | Path = "results/figures/scaling_baselines.png") -> Path:
    """Create a baseline SQL / Lieb-Mattis / HL scaling plot."""
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    n = np.logspace(1, 5, 200)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.loglog(n, sql_variance(n), label="SQL ~ N^-1", linestyle="--")
    ax.loglog(n, lieb_mattis_variance_bound(n), label="Lieb-Mattis QCRB")
    ax.loglog(n, heisenberg_variance(n), label="HL ~ N^-2", linestyle="--")
    ax.set_xlabel("Number of atoms N")
    ax.set_ylabel("Phase-estimation variance")
    ax.set_title("Decoherence-free sensing scaling baselines")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(output, dpi=200)
    plt.close(fig)
    return output
