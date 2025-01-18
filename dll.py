class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None 

class DLL:
  def __init__(self):
    self.head = None
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      print(f"{data} added as the first node.")
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    print(f"{data} added.") 
    curr.next = new_node
    new_node.prev = curr
  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      print(f"{data} added as the first node.")
      return
    print(f"{data} added.") 
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node 
  def delete_back(self):
    if self.head is None:
      print("No items to delete.")
      return
    if self.head.next is None:
      self.head = None
      print("Deleted the last item.")
      return
    curr = self.head
    while curr.next.next:
      curr = curr.next
    curr.next = None 
  def delete_front(self):
    if self.head is None:
      print("No items to delete.")
      return
    if self.head.next is None:
      self.head = None
      print("Deleted the last item.")
      return
    self.head = self.head.next
    self.head.prev = None
  def display(self):
    if self.head is None:
      print("List is empty!")
      return
    curr = self.head
    while curr:
      print(f"{curr.data}->", end='') 
      curr = curr.next
    print("None")

def main():
  dll = DLL()
  # dll.append(1)
  # dll.append(2)
  # dll.append(3)
  dll.prepend(1)
  dll.prepend(11)
  dll.prepend(12)
  dll.delete_front()
  dll.display()

if __name__ == "__main__":
  main()