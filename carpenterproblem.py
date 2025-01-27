x = []
n = int(input("Enter the length of the array: "))
arr = list(map(int, input("Enter numbers separated by space: ").split()))
z = 0

for i in range(n):
    for j in range(i + 1, n):
        if (2 * x[i]) > x[j] and (2 * x[j]) > x[i]:
            z = 1
            break
    if z == 1:
        break
if z == 1:
    print("Yes")
else:
    print("No")
