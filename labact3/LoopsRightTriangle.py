print("labact3-loops/right_triangle")
num = [1, 2, 3, 4, 5]
y = 4
x = 0 
while x < 5:
    for i in num:
        print(i, end=" ")
    print("")
    del num[y] 
    y -= 1
    x += 1 
