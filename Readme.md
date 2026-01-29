Readme.md

# SVGelona_AI 5.0


SVGelona_AI 5.0 is a fully implemented vectorial-spiral AI framework for the Riemann Hypothesis.
It integrates the four Bridge-Theorems, semi-spiral flow dynamics, Q8 + Möbius symmetry invariants,
energy-based barycenter displacement, and numerical validation.


## Project Structure


```
SVGelona_AI.5.0/
│
├── axioms/                 # Core mathematical axioms
├── dynamics/               # Angular defect dynamics, spiral flow, barycenter
├── symmetry/               # Q8 group, Möbius action, invariants
├── engine/                 # Global SVG–Γ engine, constraints, state manager
├── validation/             # Falsifiability tests, consistency checks, numerical experiments
├── papers/                 # Core paper and appendix proofs
├── run.py                  # Example script to run engine and experiments
└── README.md               # Project documentation
```


## Features


- Embeds each potential zero of \(\zeta(s)\) as a 3D vector
- Semi-spiral flow \(T_3^-\) ensures energy decreases monotonically
- Q8 + Möbius invariants, critical line \(L_c\) enforced globally
- Numerical experiments and falsifiability tests
- State management: save/load/restore
- Paper-ready LaTeX documentation included


## Usage


```bash
python run.py
```


This will initialize the engine with example zeros, run the semi-spiral flow, check invariants, and produce a numerical report.


## Papers


- `papers/svg_gamma_core.tex` : Core methodology and proof framework

- `papers/appendix_bridge_proofs.tex` : Detailed Bridge-Theorem proofs

  

DATA/LICENSE_DATA.txt

text
DATA USAGE TERMS

The zeros data in zeros_simple.txt contains 500 Riemann zeta zeros
(indices 21501-22500) derived from publicly available sources.

Usage Conditions:
1. For academic and research purposes only
2. Attribution to original sources required:
   - LMFDB (L-functions and Modular Forms Database)
   - Odlyzko, A. M. "Supercomputers and the Riemann zeta function"
3. No warranty of accuracy is provided
4. Redistribution must include this license file

These terms apply only to the data files, not to the software code
(which is covered by the MIT License in the parent directory).


