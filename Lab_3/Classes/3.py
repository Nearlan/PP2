class shape():
    def area1(self):
        a = 0
        a += (square.length * square.width)
        print(a)

class square(shape):
    length = 0
    width = 0
    def __init__(self):
        self.length = int(input())
        self.width = int(input())
        square.length = self.length
        square.width = self.width
    def area2(self):
        a = 0
        a += (self.length * self.width)
        print(a)
        
x = square()
x.area1()
x.area2()