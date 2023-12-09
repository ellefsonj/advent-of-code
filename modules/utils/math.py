# greatest common divisor (Euclidean algorithm)
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    r = a % b
    return gcd(b, r)


# least common multiple
def lcm(a, b):
    return int((a * b) / gcd(a, b))
