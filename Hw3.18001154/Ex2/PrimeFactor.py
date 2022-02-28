# Recursive program analysis of integers into prime factors
def prime_factors(n):
    factors = []
    if n > 1:
        i = 2
        while n % i != 0:
            i += 1
        factors.append(i)
        factors.extend(prime_factors(n / i))
    return factors

n=104
print(prime_factors(n))