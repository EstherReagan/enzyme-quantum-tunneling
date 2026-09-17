<div align="center">

# ⚛️ Enzyme Quantum Tunneling

### Modeling quantum tunneling effects in enzymatic reactions

### 📄 Official Publication

[Read the Full Research Manuscript Here (DOI: 10.1/zenodo.22813021)](https://doi.org)

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

This project combines a LaTeX research manuscript with a Python-based Wentzel–Kramers–Brillouin (WKB) mathematical solver. Together, these components provide a compact and reproducible framework for examining how barrier geometry, particle mass, and reaction energy influence tunneling behavior.

The project provides tools for:

- Modeling enzymatic reaction barriers
- Estimating tunneling contributions to reaction rates
- Exploring temperature-dependent reaction behavior
- Comparing classical and quantum-mechanical models
- Visualizing potential energy surfaces and tunneling probabilities
- Investigating kinetic isotope effects
- Reproducing the mathematical analysis presented in the research manuscript

## Scientific Motivation

Enzyme catalysis is commonly described using classical transition-state theory. Within this framework, reactants must acquire sufficient energy to overcome an activation barrier before progressing to products.

However, several enzymatic reactions exhibit behavior that suggests quantum mechanical contributions, including:

- Large kinetic isotope effects
- Weak temperature dependence
- Non-classical reaction rates
- Hydrogen-transfer reactions occurring faster than expected
- Strong sensitivity to barrier width and donor–acceptor distance
- Reaction rates that cannot be fully explained by classical barrier crossing alone

Quantum tunneling provides a complementary explanation. Rather than requiring a particle to pass over an energy barrier, quantum mechanics permits a finite probability that the particle will penetrate through the classically forbidden region.

For a one-dimensional barrier, a simplified WKB tunneling probability can be represented by:

$$
P_{\text{tunnel}} \propto
\exp\left(
-\frac{2}{\hbar}
\int_{x_1}^{x_2}
\sqrt{2m\left(V(x)-E\right)}\,dx
\right)
$$

where:

- \(m\) is the transferred particle's mass
- \(V(x)\) is the potential energy barrier
- \(E\) is the particle's energy
- \(\hbar\) is the reduced Planck constant
- \(x_1\) and \(x_2\) define the classically forbidden region

Because tunneling probability depends strongly on particle mass, barrier width, and barrier height, even small changes in an enzyme's active site can significantly affect reaction kinetics.

In particular, lighter particles generally exhibit greater tunneling probabilities than heavier particles. This mass dependence provides a physical basis for investigating isotope effects, such as the difference between proton and deuteron transfer.

## Key Features

| Feature | Description |
|---|---|
| Classical modeling | Estimate reaction behavior using conventional barrier-crossing models |
| Quantum tunneling | Model barrier penetration by light particles |
| WKB analysis | Calculate tunneling behavior using a semiclassical approximation |
| Isotope comparison | Compare hydrogen, deuterium, and other isotopic systems |
| Parameter analysis | Examine the effects of barrier width, height, energy, and particle mass |
| Reproducibility | Pair the mathematical solver with a formal LaTeX research manuscript |
| Lightweight design | Use a compact flat-file structure with minimal dependencies |

## Project Structure

```text
enzyme-quantum-tunneling/
├── manuscript.tex        # LaTeX source text for the research manuscript
├── wkb\_tunneling.py      # WKB mathematical solver
├── requirements.txt      # Project dependencies framework
├── LICENSE                # MIT license
└── README.md              # Project documentation
