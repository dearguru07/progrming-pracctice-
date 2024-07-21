def Prime(n):
    tem=True
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            tem=False
            break
    if tem==True:
        print("Prime Number")    
    else:
        print("not a Prime Number")
n=int(input("netera number"))            
Prime(n)