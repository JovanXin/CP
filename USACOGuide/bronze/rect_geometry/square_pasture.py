# http://www.usaco.org/index.php?page=viewproblem2&cpid=663
import sys

sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def area(self):
        return abs(self.x2 - self.x1) *abs(self.y2-self.y1)

def intersect(rect1: Rect, rect2: Rect):
    x_overlap = max(0, min(rect1.x2, rect2.x2) - max(rect1.x1, rect2.x1))
    y_overlap = max(0, min(rect1.y2, rect2.y2) - max(rect1.y1, rect2.y1))

    return x_overlap * y_overlap

x1, y1, x2, y2 = map(int, input().split())
rect1 = Rect(x1, y1, x2, y2)

x1, y1, x2, y2 = map(int, input().split())
rect2 = Rect(x1, y1, x2, y2)

x = abs(min(rect1.x1, rect2.x1) - max(rect1.x2, rect2.x2))
y = abs(min(rect1.y1, rect2.y1) - max(rect1.y2, rect2.y2))
print(max(x, y)**2)