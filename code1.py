def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def unique_prime_factors(n):
    """Get the unique prime factors of a number"""
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def lasker_noether_theorem(n):
    """Apply the Lasker–Noether theorem to a given number"""
    if is_prime(n):
        return [n]
    factors = unique_prime_factors(n)
    ideals = []
    for p in factors:
        ideal = []
        while n % p == 0:
            ideal.append(p)
            n //= p
        ideals.append(ideal)
    return ideals

n = int(input("Enter a number: "))
ideals = lasker_noether_theorem(n)
print("Ideal(s):", ideals)
