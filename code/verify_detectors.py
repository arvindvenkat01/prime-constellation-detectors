import sympy
from sympy import isprime, divisors

def get_M1(n):
    return sum(divisors(n))

# Robust Constellation Checker
def check_constellation(n, pattern_offsets):
    """
    Checks if n = product(p + k) for k in offsets.
    Does a full scan starting from p=2.
    """
    p = 2
    degree = len(pattern_offsets)
    
    while True:
        # Calculate product for current p
        # pattern_offsets e.g. [0, 2] for p(p+2)
        terms = [p + k for k in pattern_offsets]
        product = 1
        for t in terms: product *= t
        
        # Stop if we exceeded n
        if product > n:
            return False
            
        # Check match
        if product == n:
            # Found a product match! Now check primality.
            if all(isprime(t) for t in terms):
                return True # Valid Constellation
            else:
                return False # Product matches, but factors aren't prime (e.g. 3*5*9)
        
        # Move to next prime (optimization: could just do p+=1, but let's do p+=1 for safety)
        p += 1

def verify_detectors(limit=100000):
    print(f"Running ROBUST verification up to n={limit}...")
    
    # Store FPs
    fps = {"Twin": [], "Trip1": [], "Trip2": [], "Quad": [], "Sophie": [], "Chernick": []}
    
    for n in range(2, limit + 1):
        M1 = get_M1(n)
        
        # --- 1. TWIN PRIME DETECTOR ---
        # Target: p*(p+2) -> Offsets [0, 2]
        val = (M1 - n)**2 - 2*(M1 + n) - 3
        if val == 0:
            if not check_constellation(n, [0, 2]):
                fps["Twin"].append(n)

        # --- 2. TRIPLET T1 DETECTOR ---
        # Target: p*(p+2)*(p+6) -> Offsets [0, 2, 6]
        val = (M1**3 - 3*M1**2*n - 31*M1**2 + 3*M1*n**2 + 35*M1*n + 135*M1 
               - n**3 - 31*n**2 + 185*n + 1575)
        if val == 0:
            if not check_constellation(n, [0, 2, 6]):
                fps["Trip1"].append(n)

        # --- 3. TRIPLET T2 DETECTOR ---
        # Target: p*(p+4)*(p+6) -> Offsets [0, 4, 6]
        val = (M1**3 - 3*M1**2*n - 31*M1**2 + 3*M1*n**2 + 35*M1*n - 185*M1 
               - n**3 - 31*n**2 - 135*n + 1575)
        if val == 0:
            if not check_constellation(n, [0, 4, 6]):
                fps["Trip2"].append(n)

        # --- 4. QUADRUPLET DETECTOR ---
        # Target: p(p+2)(p+6)(p+8) -> Offsets [0, 2, 6, 8]
        val = (M1**4 - 4*M1**3*n - 164*M1**3 + 6*M1**2*n**2 + 36*M1**2*n - 6650*M1**2 
               - 4*M1*n**3 + 36*M1*n**2 + 14980*M1*n + 308700*M1 
               + n**4 - 164*n**3 - 6650*n**2 + 308700*n + 10418625)
        if val == 0:
            if not check_constellation(n, [0, 2, 6, 8]):
                fps["Quad"].append(n)

    print("\nFINAL CLEAN RESULTS:")
    for k, v in fps.items():
        if len(v) > 0:
            print(f"  {k}: {len(v)} Exceptions -> {v}")
        else:
            print(f"  {k}: 100% Clean")

if __name__ == "__main__":
    verify_detectors()
