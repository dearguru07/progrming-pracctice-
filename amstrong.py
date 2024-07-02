# def countDD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# def Anstrong(n):
#     tem=n 
#     sum=0
#     powr=countDD(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**powr)
#         n=n//10
#     if tem==sum  :
#         return True
#     else:
#         return False
# sr=int(input('enter a number'))
# er=int(input('entr'))
# float=True
# for i in range(sr,er+1):
#     if float==Anstrong(i):
#         print(i)
    
               
               
               
# def CountDD(n):
#     Count=0
#     while n!=0:
#         n=n//10
#         Count+=1               
#     return Count
# def Amstrong(n):
#     tem=n
#     sum=0
#     power=CountDD(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**power)
#         n=n//10
#     if tem==sum:
#         return True
#     else:
#         return False
# n=int(input('entr a number'))        
# float=Amstrong(n)
# if float==True:
#     print("armgd")
# else:
#     print('not')    
    

# def CountV(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# def Amstrong(n):
#     tem=n
#     sum=0
#     power=CountV(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**power)
#         n//=10
#     if tem==sum:
#         return True
#     else:
#         return False
# n=int(input('enter a numb'))
# float=Amstrong(n)
# if float==True:
#     print('amrg')
# else:
#     print('not')                    



def Find(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
def Amstrong(n):
    tem=n 
    sum=0
    power=Find(n)
    while n!=0:
        rem=n%10
        sum=sum+rem**power
        n//=10
    if tem==sum:
        return True
    else:
        return False
sr=int(input('enter a number'))
er=int(input('enter a number'))
float=True
for i in range(sr,er+1):
    if float==Amstrong(i):
        print(i)