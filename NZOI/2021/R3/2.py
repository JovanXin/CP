"""
100/100
Self explanatory
"""
shoes = input().upper()
if shoes.count("R") == 2:
    print("Dorothy is in the classroom.")
elif shoes.count("R") == 1:
    print("Hop along Dorothy and find that other shoe.")
elif shoes.count("R") == 0:
    print("Maybe Dorothy is in Kansas.")