class shape():
    def area1(self):
        a = 0
        a += (square.length ** 2)
        print(a)

class square(shape):
    length = 0
    def __init__(self):
        self.length = int(input())
        square.length = self.length
    def area2(self):
        a = 0
        a += (self.length ** 2)
        print(a)
        
x = square()
x.area1()
x.area2()