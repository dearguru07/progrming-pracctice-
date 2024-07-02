def Polyn(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input('et'))
res=Polyn(n)
if res==n:
    print('poly') 
else:
    print('not')       