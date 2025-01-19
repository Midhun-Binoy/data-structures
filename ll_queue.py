class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
  def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
      self.rear = self.front = new_node
      print(f"{data} inserted to the queue.")
      return
    print(f"{data} inserted to the queue.")
    self.rear.next = new_node
    self.rear = new_node
  def dequeue(self):
    if self.front is None:
      print("Queue is empty!")
      return
    item = self.front.data 
    self.front = self.front.next
    if self.front is None:
      self.rear = None
    print(f"{item} removed from the queue.")
  def display(self):
    if self.front is None:
      print("Queue is empty!")
      return
    curr = self.front
    print("\nQueue elements:")
    while curr:
      print(f"{curr.data}", end=' ') 
      curr = curr.next
    print()

def main():
  que = Queue()
  que.enqueue(1)
  que.enqueue(2)
  que.enqueue(3)
  que.dequeue()
  que.dequeue()
  que.dequeue()
  que.display()

if __name__ == "__main__":
  main()