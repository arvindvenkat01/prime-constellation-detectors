# Prime Constellation Detectors

**Algebraic detection of prime constellations via quasimodular forms.**

This repository contains the Python implementation for the paper *"The Geometry of Prime Constellations in Quasimodular Space"* by Arvind N. Venkat (2025). It provides algorithms to derive and verify polynomial detectors that identify structured prime sets (Twin Primes, Triplets, Quadruplets, Sophie Germain Chains, and Carmichael Numbers) purely from their MacMahon divisor sums $(n, M_1, M_2, M_3)$.

## Key Features
* **Symbolic Derivation:** Uses Gröbner Basis elimination (`derive_constellation_detectors.py`) to algebraically construct detectors from parametric definitions.
* **Robust Verification:** Validates detectors against integers up to $N=100,000$, accounting for edge cases and "Cubic Mimics" (algebraic aliasing by prime cubes).
* **Automated Discovery:** Includes nullspace search algorithms for finding new relations in high-dimensional quasimodular space.

## Quick Start
1.  **Derive Formulas:** Run `python derive_constellation_detectors.py` to generate the polynomial identities.
2.  **Verify Results:** Run `python verify_detectors.py` to test them against the integer number line.

## License
MIT License
