def precedence(op):
  if op == '+' or op == '-':
    return 1
  if op == '*' or op == '/':
    return 2
  if op == '^':
    return 3
  return 0

def infix_to_postfix(infix_expr):
  stack = []
  output = ''

  for char in infix_expr:
    if char.isalnum(): # operand
      output += char
    elif char == '(':
      stack.append(char)
    elif char == ')':
      while stack and stack[-1] != '(':
        output += stack.pop()
      stack.pop() # removing '('
    else: # operator
      while stack and precedence(stack[-1]) >= precedence(char):
        output += stack.pop()
      stack.append(char)

  while stack:
    output += stack.pop()

  return output

infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)