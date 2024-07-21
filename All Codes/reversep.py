def Rev(n):
    rev=0
    while n!=0:
        ren=n%10
        rev=(rev*10)+ren
        n=n//10
    return rev
n=int(input('entr'))    
res=Rev(n)
print(res)