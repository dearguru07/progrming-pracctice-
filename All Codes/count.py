def CountV(n):
    Count=0
    while n!=0:
        n//=10
        Count+=1
    return Count
n=int(input("enter a number"))    
res=CountV(n)
print(res)