"""
Can't tell what's wrong with this solution (didn't pass some test cases past 1/2) 

Potential issue of handling case where capacity of both is equal at a point? 
    -> Need to iterate through possible future scenarios to decide wether to give student chocolate from L or R. 
"""

able = True  # can we serve all students
happiness = 0

l_cap, r_cap = input().split()
l_cap, r_cap = int(l_cap), int(r_cap)

students_num = int(input())

for i in range(students_num):
    cups, happy_l, happy_r = map(int, input().split())

    # Handling edge cases?
    if r_cap == 0:
        if l_cap - cups < 0 or happy_l == -1:
            able = False
        else:
            happiness += happy_l
            l_cap -= cups
    elif l_cap == 0:
        if r_cap - cups < 0 or happy_r == -1:
            able = False
        else:
            happiness += happy_r
            r_cap -= cups

    else:
        if happy_l == -1:
            if r_cap - cups < 0:
                able = False
            else:
                happiness += happy_r
                r_cap -= cups

        elif happy_r == -1:
            if l_cap - cups < 0:
                able = False
            else:
                happiness += happy_l
                l_cap -= cups
        else:
            if happy_l > happy_r:
                if l_cap - cups > 0:
                    happiness += happy_l
                    l_cap -= cups
                elif r_cap - cups > 0:
                    happiness += happy_r
                    r_cap -= cups
                else:
                    able = False
            elif happy_r > happy_l:
                if r_cap - cups > 0:
                    happiness += happy_r
                    r_cap -= cups
                elif l_cap - cups > 0:
                    happiness += happy_l
                    l_cap -= cups
                else:
                    able = False
if able:
    print(happiness)
else:
    print("Camp is cancelled")