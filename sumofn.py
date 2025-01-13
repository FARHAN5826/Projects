def sumofn(n):
    if(n==1):
        return 1
    else:
        return n+sumofn(n-1)

n=int(input("Enter the number :"))
result=sumofn(n)
print(f"Result = {result}")