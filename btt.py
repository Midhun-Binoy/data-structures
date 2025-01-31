class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BTT:
  def __init__(self):
    self.root = None
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert(self.root, data)
  def _insert(self, current, data):
    if data < current.data:
      if current.left is None:
        current.left = Node(data)
      else:
        self._insert(current.left, data)
    elif data > current.data:
      if current.right is None:
        current.right = Node(data)
      else:
        self._insert(current.right, data)
    else:
      print(f"{data} already exists in tree!")
  def preorder(self):
    print("Preorder traversal:")
    self._preorder(self.root)
  def _preorder(self, current):
    if current is not None:
      print(current.data, end=' ')
      self._preorder(current.left)
      self._preorder(current.right)
    else:
      print("None", end=' ')
  def inorder(self):
    print("Inorder traversal:")
    self._inorder(self.root)
  def _inorder(self, current):
    if current is not None:
      self._inorder(current.left)
      print(current.data, end=' ')
      self._inorder(current.right)
    else:
      print("None", end=' ')
  def postorder(self):
    print("Postorder traversal:")
    self._postorder(self.root)
  def _postorder(self, current):
    if current is not None:
      self._postorder(current.left)
      self._postorder(current.right)
      print(current.data, end=' ')
    else:
      print("None", end=' ')

def main():
  bt = BTT()
  bt.insert(50)
  bt.insert(30)
  bt.insert(20)
  bt.insert(40)
  bt.insert(70)
  bt.insert(60)
  bt.insert(80)
  bt.preorder()
  print()
  bt.inorder()
  print()
  bt.postorder()
  print()

if __name__ == "__main__":
  main()