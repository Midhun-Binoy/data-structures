MAX = 5

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, item):
    if len(self.stack) == MAX: 
      print("Stack is full!")
    else:
      self.stack.append(item)
      print(f"{item} is pushed to the stack.")
  def pop(self):
    if len(self.stack) <= 0:
      print("Stack is empty!")
    else:
      item = self.stack.pop()
      print(f"{item} is popped from the stack.")
  def display(self):
    if len(self.stack) <= 0:
      print("Stack is empty!")
    else:
      print("\nStack contents:")
      for i in range(len(self.stack) - 1, -1, -1):
        print(self.stack[i]) 

def main():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.push(4)
  stack.push(5)
  stack.push(6)
  # stack.pop()
  # stack.pop()
  # stack.pop()
  stack.display()

if __name__ == "__main__":
  main()