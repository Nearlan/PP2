class point:
    def move(self):
        self.fpnt = list(map(int, input().split()))
    def show(self):
        print("(", (self.fpnt)[0], ";", (self.fpnt)[1], ")", sep="")
    def distance(self):
        self.opnt = list(map(int, input("Other point is...\n").split()))
        a = ((self.fpnt)[0]  - (self.opnt)[0]) ** 2 + ((self.fpnt)[1] + (self.opnt)[1]) ** 2
        print("Distance between points: ", a ** (0.5))

points = point()
points.move()
points.show()
points.distance()