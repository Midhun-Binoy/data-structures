MAX = 5

class Queue:
  def __init__(self):
    self.queue = []
  def insert(self, item):
    if len(self.queue) == MAX:
      print("Queue is full!")
    else:
      self.queue.append(item)
      print(f"{item} inserted to the queue.")
  def delete(self):
    if len(self.queue) == 0:
      print("Queue is empty!")
    else:
      item = self.queue.pop(0)
      print(f"{item} deleted from the queue.")
  def display(self):
    if len(self.queue) == 0:
      print("Queue is empty!")
    else:
      print("\nQueue elements:")
      for el in self.queue:
        print(el, end=' ')
      print()

def main():
  queue = Queue()
  queue.insert(7)
  queue.insert(8)
  queue.insert(9)
  queue.insert(10)
  queue.insert(11)
  queue.delete()
  queue.delete()
  queue.delete()
  queue.delete()
  queue.delete()
  queue.delete()
  queue.display()

if __name__ == "__main__":
  main()