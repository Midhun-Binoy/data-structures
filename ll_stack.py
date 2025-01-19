class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
  def push(self, data):
    new_node = Node(data)
    print(f"{data} added to the stack.")
    new_node.next = self.top
    self.top = new_node
  def pop(self):
    if self.top is None:
      print("Stack is empty!")
      return
    item = self.top.data
    self.top = self.top.next
    print(f"{item} popped from the stack.")
  def display(self):
    if self.top is None:
      print("Stack is empty!")
      return
    curr = self.top
    print("\nStack elements:")
    while curr:
      print(curr.data)
      curr = curr.next

def main():
  st = Stack()
  st.push(1)
  st.push(2)
  st.push(3)
  st.pop()
  st.display()

if __name__ == "__main__":
  main()