<div align="center">

# ⚛️ Enzyme Quantum Tunneling

### Modeling quantum tunneling effects in enzymatic reactions

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/EstherReagan/enzyme-quantum-tunneling?style=for-the-badge)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/EstherReagan/enzyme-quantum-tunneling?style=for-the-badge)](https://github.com/EstherReagan/enzyme-quantum-tunneling/commits/main)
[![Issues](https://img.shields.io/github/issues/EstherReagan/enzyme-quantum-tunneling?style=for-the-badge)](https://github.com/EstherReagan/enzyme-quantum-tunneling/issues)

<br />

*A computational framework for exploring how quantum mechanical effects influence enzyme-catalyzed reactions.*

</div>

---

## Overview

**Enzyme Quantum Tunneling** investigates the role of quantum tunneling in enzymatic reaction mechanisms, with an emphasis on the transfer of light particles such as protons and hydrogen atoms.

Classical transition-state models may not fully explain the observed rates, temperature dependence, or kinetic isotope effects of certain enzyme reactions. Quantum tunneling provides an alternative mechanism in which particles pass through an energy barrier rather than going over it.

This project provides tools for:

- Modeling enzymatic reaction barriers
- Estimating tunneling contributions to reaction rates
- Exploring temperature-dependent reaction behavior
- Comparing classical and quantum-mechanical models
- Visualizing potential energy surfaces and tunneling probabilities
- Investigating kinetic isotope effects

## Scientific Motivation

Enzyme catalysis is commonly described using classical transition-state theory. However, some reactions exhibit behavior that suggests quantum mechanical contributions, including:

- Large kinetic isotope effects
- Weak temperature dependence
- Non-classical reaction rates
- Hydrogen-transfer reactions occurring faster than expected
- Strong sensitivity to barrier width and donor–acceptor distance

A simplified tunneling probability can be represented by:

\[
P_{\text{tunnel}} \propto
\exp\left(
-\frac{2}{\hbar}
\int_{x_1}^{x_2}
\sqrt{2m\left(V(x)-E\right)}\,dx
\right)
\]

where:

- \(m\) is the transferred particle's mass
- \(V(x)\) is the potential energy barrier
- \(E\) is the particle's energy
- \(\hbar\) is the reduced Planck constant
- \(x_1\) and \(x_2\) define the classically forbidden region

Because tunneling probability depends strongly on particle mass, barrier width, and barrier height, even small changes in an enzyme's active site can significantly affect reaction kinetics.

---

## Key Features

| Feature | Description |
|---|---|
| Classical modeling | Estimate reaction behavior using conventional barrier-crossing models |
| Quantum tunneling | Model barrier penetration by light particles |
| Isotope comparison | Compare hydrogen, deuterium, and other isotopic systems |
| Parameter sweeps | Analyze how rates change with barrier width, height, and temperature |
| Visualization | Generate plots of barriers, probabilities, and reaction rates |
| Reproducibility | Keep simulations and analyses organized in a repeatable workflow |

---

## Project Structure

```text
enzyme-quantum-tunneling/
├── data/                  # Input data and generated datasets
├── notebooks/             # Exploratory analyses and demonstrations
├── src/                   # Core modeling and simulation code
├── tests/                 # Automated tests
├── results/               # Generated plots, tables, and outputs
├── docs/                  # Additional documentation
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── LICENSE                # Project license
└── README.md              # Project documentation

