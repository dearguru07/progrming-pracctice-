def Polyndrm(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    return rev
n=int(input('enter a number'))    
res=Polyndrm(n)
if res==n:
    print('pplyndrom')
else:
    print("not a polynesrom")    