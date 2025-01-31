class SparseMatrix:
  def __init__(self):
    self.a = self.s = self.t = []
    self.m = self.n = None
    self.k = 0
  def input(self):
    self.m, self.n = map(int, input("Enter the size: ").split())
    print("Enter the array elements:")
    for _ in range(self.m):
      row = list(map(int, input().split()))
      self.a.append(row)
  def display(self, a):
    print("\nThe array is:")
    for row in a:
      print(*row)
  def sparseMatrix(self):
    self.s = [[self.m, self.n, 0]]
    for i in range(self.m):
      for j in range(self.n):
        if self.a[i][j] != 0:
          self.s.append([i, j, self.a[i][j]])
          self.k += 1
    self.s[0][2] = self.k
  def transpose(self):
    self.t = [[self.n, self.m, self.k]]
    for i in range(self.n):
      for j in range(1, self.k + 1):
        if self.s[j][1] == i:
          self.t.append([self.s[j][1], self.s[j][0], self.s[j][2]])

def main():
  s = SparseMatrix()
  s.input()
  s.sparseMatrix()
  s.display(s.s)
  s.transpose()
  s.display(s.t)

if __name__ == "__main__":
  main()
