class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None
  def insert(self, data):
    if self.root is None: # if there are no elements.
      self.root = Node(data)
    else:
      self._insert(self.root, data)
  def _insert(self, current, data):
    if data < current.data: # insertion at the left of root.
      if current.left is None: # if there is no left child.
        current.left = Node(data)
      else:
        self._insert(current.left, data)
    elif data > current.data: # insertion at the right of root.
      if current.right is None: # if there is no right child.
        current.right = Node(data)
      else:
        self._insert(current.right, data)
    else: # data is already present.
      print(f"{data} already exists in tree!")
  def search(self, data):
    return self._search(self.root, data)
  def _search(self, current, data):
    if current is None:
      return False
    if data == current.data:
      return True
    elif data < current.data:
      return self._search(current.left, data)
    else:
      return self._search(current.right, data)
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

def main():
  bst = BST()
  bst.insert(1)
  bst.insert(11)
  bst.insert(27)
  bst.insert(8)
  bst.insert(18)
  bst.inorder()
  bst.preorder()

if __name__ == "__main__":
  main()