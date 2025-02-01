class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class CDLL:
  def __init__(self):
    self.head = None
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      # new_node.next = self.head
      # self.head.prev = new_node
      new_node.next = new_node
      new_node.prev = new_node
      print(f"{data} added as the first node.")
      return
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    print(f"{data} added.") 
    curr.next = new_node
    new_node.prev = curr
    new_node.next = self.head
    self.head.prev = new_node
  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      # new_node.next = self.head
      # self.head.prev = new_node
      new_node.next = new_node
      new_node.prev = new_node
      print(f"{data} added as the first node.")
      return
    print(f"{data} added.") 
    new_node.next = self.head
    self.head.prev = new_node
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    self.head = new_node
  def delete_back(self):
    if self.head is None:
      print("No items to delete.")
      return
    if self.head.next == self.head:
      self.head = None
      print("Deleted the last item.")
      return
    curr = self.head
    while curr.next.next != self.head:
      curr = curr.next
    print(f"Deleted item {curr.next.data}")
    curr.next = self.head
    self.head.prev = curr
  def delete_front(self):
    if self.head is None:
      print("No items to delete.")
      return
    if self.head.next == self.head:
      self.head = None
      print("Deleted the last item.")
      return
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    print(f"Deleted item {self.head.data}")
    self.head = self.head.next
    curr.next = self.head
    self.head.prev = curr
  def display(self):
    if self.head is None:
      print("List is empty!")
      return
    curr = self.head
    while curr.next != self.head:
      print(f"{curr.data}<->", end='') 
      curr = curr.next
    print(f"{curr.data}<->{self.head.data}")
def main():
  cdll = CDLL()
  # cdll.append(1)
  # cdll.append(2)
  # cdll.append(3)
  cdll.prepend(1)
  cdll.prepend(11)
  cdll.prepend(12)
  cdll.display()
  cdll.delete_front()
  cdll.delete_front()
  # cdll.delete_back()
  cdll.display()

if __name__ == "__main__":
  main()