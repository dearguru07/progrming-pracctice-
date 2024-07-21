def Happy(n):
    if n==1:
        return True
    if n==4:
        return False
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem*rem
        n//=10
    return Happy(sum)
n=int(input('entera number'))    
Happy(n)
