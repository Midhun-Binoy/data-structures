def evaluate_postfix(postfix):
  stack = []

  for char in postfix.split():
    if char.isdigit():
      stack.append(int(char))
    else:
      b = stack.pop()
      a = stack.pop()

      if char == '+':
        stack.append(a + b)
      elif char == '-':
        stack.append(a - b)
      elif char == '*':
        stack.append(a * b)
      elif char == '/':
        stack.append(a // b)
      elif char == '^':
        stack.append(a ** b)

  return stack.pop()

postfix = "5 3 1 * + 9 -"
result = evaluate_postfix(postfix)
print(result)