class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CLL:
  def __init__(self):
    self.head = None
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
      print(f"{data} added as the first node.")
      return
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    print(f"{data} added.") 
    curr.next = new_node
    new_node.next = self.head
  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
      print(f"{data} added as the first node.")
      return
    print(f"{data} added.") 
    new_node.next = self.head
    curr = self.head
    while curr.next != self.head:
      curr = curr.next
    curr.next = new_node
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
  def display(self):
    if self.head is None:
      print("List is empty!")
      return
    curr = self.head
    while curr.next != self.head:
      print(f"{curr.data}->", end='') 
      curr = curr.next
    print(f"{curr.data}->{self.head.data}")
def main():
  cll = CLL()
  # cll.append(1)
  # cll.append(2)
  # cll.append(3)
  cll.prepend(1)
  cll.prepend(11)
  cll.prepend(12)
  cll.display()
  cll.delete_front()
  # cll.delete_back()
  cll.display()

if __name__ == "__main__":
  main()