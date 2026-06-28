# Decoherence-Free Sensing

Computational specifications for decoherence-free differential quantum sensing.

Lead report: **Decoherence-Free Subspaces Specify Robust Quantum Sensing**

Paper: *Lieb-Mattis States for Robust Entangled Differential Phase Sensing*, Physical Review X 16, 021052 (2026). DOI: `10.1103/ksyh-mb4s`.

## Leading specification

Decoherence-free subspaces remove common-mode phase noise while preserving sensitivity to differential phase signals.

## Roadmap

| Notebook | Purpose |
|---|---|
| `00_context.ipynb` | Paper context, differential sensing, common-mode noise |
| `07_decoherence_free_subspaces.ipynb` | DFS constraint: common phase rejected, differential phase retained |
| `13_lieb_mattis_states.ipynb` | Lieb-Mattis target states and singlet-pair intuition |
| `17_quantum_fisher_information.ipynb` | SQL, QCRB, Heisenberg scaling comparisons |
| `23_two_mode_squeezing.ipynb` | Unitary cavity-mediated preparation protocol |
| `29_collective_emission.ipynb` | Dissipative preparation through collective emission |
| `37_noise_scaling.ipynb` | Cooperativity, free-space emission, realistic robustness |
| `43_design_rules.ipynb` | Engineering statements for scalable quantum sensor networks |

## Repository layout

```text
src/dfs_sensing/   reusable simulation utilities
notebooks/         executable computational lab notes
figures/           published infographic and static assets
results/           generated figures and tables
site/              labreports.app page assets
paper/             local paper copy for reference
scripts/           command-line helpers
tests/             lightweight checks
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Engineering statement

Constrain dynamics to reject shared noise first, then engineer entanglement that maximizes sensitivity to the remaining differential signal.
