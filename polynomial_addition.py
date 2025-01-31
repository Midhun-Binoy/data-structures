def add_polynomials(p1, p2):
  n = max(len(p1), len(p2))

  result = [0] * n

  for i in range(len(p1)):
    result[i + n - len(p1)] += p1[i]
  for i in range(len(p2)):
    result[i + n - len(p2)] += p2[i]

  return result

def print_polynomial(p):
  terms = []
  for i in range(len(p)):
    if p[i] != 0:
      terms.append(f"{p[i]}x^{len(p) - 1 - i}" if i < len(p) - 1 else f"{p[i]}")
  print(" + ".join(terms) if terms else "0")

poly1 = [1, 2, 3]
poly2 = [5, 4]

print_polynomial(poly1)
print_polynomial(poly2)

result = add_polynomials(poly1, poly2)
print_polynomial(result)