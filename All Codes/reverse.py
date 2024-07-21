def Reverse(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rem+(rev*10)
        n//=10
    return rev
n=int(input('enter anumber'))    
res=Reverse(n)
print(res)