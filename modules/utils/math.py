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


def quadracitFormula(a, b, c):
    # provide a set of solutions to a quadratic equation (ax^2 + bx + c = 0)
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print('Complex Square root is yet to be implemented')
    solution_one = (-b + discriminant ** 0.5) / (2 * a)
    solution_two = (-b - discriminant ** 0.5) / (2 * a)

    return [solution_one, solution_two]
