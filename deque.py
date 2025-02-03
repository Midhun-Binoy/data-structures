class Deque:
  def __init__(self, size):
    self.size = size
    self.a = []
  def isEmpty(self):
    return len(self.a) == 0
  def isFull(self):
    return len(self.a) == self.size
  def insertFront(self, data):
    if self.isFull():
      print("Queue is full!")
    else:
      self.a.insert(0, data)
  def insertRear(self, data):
    if self.isFull():
      print("Queue is full!")
    else:
      self.a.append(data)
  def deleteFront(self):
    if self.isEmpty():
      print("Queue is empty!")
    else:
      self.a.pop(0)
  def deleteRear(self):
    if self.isEmpty():
      print("Queue is empty!")
    else:
      self.a.pop()
  def display(self):
    print("Queue:")
    print(self.a)
  
def main():
  dq = Deque(5)

  dq.insertFront(10)
  dq.insertFront(20)
  dq.insertFront(30)
  dq.insertRear(40)
  dq.insertRear(50)

  dq.deleteFront()

  dq.display()


if __name__ == "__main__":
  main()