inpt = input("Enter value here: ")
input = int(inpt)
sum = 0
Formula_list = []

print(f"Input: {input}")


for i in range(input):
    i += 1
    Formula_list.append(i)
else:
    print("Formula:", end=" ")
    print(*Formula_list, sep='+')

for i in range(input): 
    i += 1
    sum = sum + i
else:
    print(f"Output: {sum}")