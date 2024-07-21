# def Prime(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('enter a number'))    
# er=int(input('enter a number'))    
# if sr>er:
#     print('Invalid range')
# else:
#     for i in range(sr,er+1):
#         res=Prime(i)
#         if res==True and i>1:    
#             print(i)


# def CountD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# sr=int(input('enter a number'))    
# er=int(input('enter a number')) 
# if sr>er:
#     print('invalid range') 
# else:
#     for i in range(sr,er+1):
#         float=CountD(i)
#         print(i,"count of nubrs",float)


# def Reverse(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# sr=int(input('enter a umer'))    
# er=int(input('enter a umer'))   
# if sr>er:
#     print('invalidd') 
# else:
#     for i in range(sr,er+1):
#         float=Reverse(i)
#         print(i,"revse is ",float)    



# def Polyndrom(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# sr=int(input('enter a number'))    
# er=int(input('enter a number'))    
# if sr>er:
#     print('invalid')
# else:
#     for i in range(sr,er+1):
#         res=Polyndrom(i)
#         if res==i:
#             print(i)    



def CountD(n):
    count=0
    while n!=0:
       n=n//10
       count+=1
    return count
def Amsrtng(n):
    tem=n
    sum=0
    power=CountD(n)
    while n!=0:
        rem=n%10
        sum=(sum+rem**power)
        n=n//10
    if tem==sum:
            return True
    else:
            return False
n=int(input('enter a number'))
float=Amsrtng(n)
if float==True:
    print('amsrtg')
else:
    print('not a amrsh')    
    