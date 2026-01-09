"""
3_derive_constellation_detectors.py

Systematic derivation of quasimodular detectors for prime constellations
and chains using Gröbner Basis elimination.

Includes:
1. Prime Triplets (Type 1 & 2)
2. Prime Quadruplets
3. Sophie Germain Chains (Length 3)
"""

import sympy
from sympy import symbols, groebner, factor, expand

def derive_detector(name, param_vars, n_expr, m1_expr):
    print(f"\n{'='*70}")
    print(f"DERIVING: {name}")
    print(f"{'='*70}")
    
    n, M1 = symbols('n M1')
    
    # Define the Ideal: < n - n(t), M1 - M1(t) >
    polys = [n - n_expr, M1 - m1_expr]
    
    print(f"  n(t)  = {n_expr}")
    print(f"  M1(t) = {m1_expr}")
    print("  Computing Gröbner Basis...")
    
    # Elimination order: parameters > M1 > n
    all_vars = tuple(param_vars) + (M1, n)
    basis = groebner(polys, *all_vars, order='lex')
    
    detector = None
    for poly in basis:
        if not any(poly.has(v) for v in param_vars):
            detector = poly
            break
            
    if detector:
        print("\n  ✅ SUCCESS: Found Detector Polynomial!")
        print(f"  D(n, M1) = {detector}")
        
        # Check if it factors nicely
        factored = factor(detector)
        if str(factored) != str(detector):
            print(f"  Factored:  {factored} = 0")
            
        # Analyze the leading term to spot patterns (like (M1-n)^k)
        # We check the degree of the polynomial
        deg = sympy.degree(detector, M1)
        print(f"  Degree in M1: {deg}")
        
    else:
        print("  ❌ FAILED: Could not eliminate parameter.")

def main():
    p = symbols('p')
    
    # --- 1. Prime Triplets ---
    # Type 1: (p, p+2, p+6)
    derive_detector("Prime Triplet Type 1 (p, p+2, p+6)", [p],
                    p*(p+2)*(p+6), 
                    (p+1)*(p+3)*(p+7))
    
    # Type 2: (p, p+4, p+6)
    derive_detector("Prime Triplet Type 2 (p, p+4, p+6)", [p],
                    p*(p+4)*(p+6), 
                    (p+1)*(p+5)*(p+7))

    # --- 2. Prime Quadruplets ---
    # (p, p+2, p+6, p+8) - The tightest constellation of 4 primes
    derive_detector("Prime Quadruplet (p, p+2, p+6, p+8)", [p],
                    p*(p+2)*(p+6)*(p+8),
                    (p+1)*(p+3)*(p+7)*(p+9))

    # --- 3. Sophie Germain Chains ---
    # Chain Length 3: p -> 2p+1 -> 2(2p+1)+1
    # n = p * (2p+1) * (4p+3)
    # M1 = (p+1) * (2p+2) * (4p+4) = 8(p+1)^3
    p1 = p
    p2 = 2*p + 1
    p3 = 2*p2 + 1
    derive_detector("Sophie Germain Chain (Len 3)", [p],
                    p1 * p2 * p3,
                    (p1+1) * (p2+1) * (p3+1))

if __name__ == "__main__":
    main()
