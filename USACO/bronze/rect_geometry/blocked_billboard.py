# http://www.usaco.org/index.php?page=viewproblem2&cpid=759
import sys

class Rect:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

    def area(self):
        return abs(self.x2 - self.x1) *abs(self.y2-self.y1)

def intersect(rect1: Rect, rect2: Rect):
    x_overlap = max(0, min(rect1.x2, rect2.x2) - max(rect1.x1, rect2.x1))
    y_overlap = max(0, min(rect1.y2, rect2.y2) - max(rect1.y1, rect2.y1))

    return x_overlap * y_overlap

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

bill1 = Rect()
bill2 = Rect()
truck = Rect()

total_area = bill1.area() + bill2.area()

print(total_area - intersect(truck, bill2) - intersect(truck, bill1))