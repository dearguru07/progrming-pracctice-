def HappyNumber(n):
    if n==1:
        return True
    else:
        return False
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem*rem
        n//=10
        return HappyNumber(n)
n=int(input('entr a number'))  
if n==True:
    print("happyNumver")
else:
    print('not a haoy')      
res=HappyNumber(n)
