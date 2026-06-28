"""Core helpers for decoherence-free differential quantum sensing.

The functions here are deliberately small and notebook-friendly. They encode
paper-level scaling relations and simple analytic benchmarks before heavier
QuTiP simulations are added.
"""

from __future__ import annotations

import numpy as np


def sql_variance(n_atoms: np.ndarray | float) -> np.ndarray:
    """Standard Quantum Limit scaling: Var(phi) ~ 1 / N."""
    n = np.asarray(n_atoms, dtype=float)
    return 1.0 / n


def heisenberg_variance(n_atoms: np.ndarray | float) -> np.ndarray:
    """Heisenberg-limit scaling: Var(phi) ~ 1 / N^2."""
    n = np.asarray(n_atoms, dtype=float)
    return 1.0 / (n * n)


def lieb_mattis_qfi(n_atoms: np.ndarray | float) -> np.ndarray:
    """QFI for the Lieb-Mattis target state: F_Q = (N^2 + 4N) / 3."""
    n = np.asarray(n_atoms, dtype=float)
    return (n * n + 4.0 * n) / 3.0


def lieb_mattis_variance_bound(n_atoms: np.ndarray | float) -> np.ndarray:
    """QCRB variance for the Lieb-Mattis target state."""
    return 1.0 / lieb_mattis_qfi(n_atoms)


def differential_phase(phi_a: float, phi_b: float) -> float:
    """Differential phase used in the report: (phi_A - phi_B) / 2."""
    return 0.5 * (phi_a - phi_b)


def common_phase(phi_a: float, phi_b: float) -> float:
    """Common phase used in the report: (phi_A + phi_B) / 2."""
    return 0.5 * (phi_a + phi_b)
