# def Count(n):
#     count=0
#     while n>0:
#         n=n//10
#         count+=1
#     return count
# sr=int(input('enter'))    
# er=int(input('enter'))    
# for i in range(sr,er+1):
#     res=Count(i)
#     print(i,"digits are",res)


# # def countD(n):
# #     count=0
# #     while n>0:
# #         n=n//10
# #         count+=1
# #     return count
# # n=int(input('enter a nub'))
# # res=countD(n)
# # print(res)    
        
        
# def Prime(n):
#     tem=True
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True and n>2:
#         print('prime')
#     else:
#         print('not prime')
# n=int(input('entr'))
# Prime(n)                
            
            
# def Prime(n):
#     er=n//2 
#     tem=True
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('enter'))
# er=int(input('enter'))
# for i in range(sr,er+1):
#     if i>1 :
#         res=Prime(i)
#         if res==True:
            # print(i)


# def Poly(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n= int(input('enter'))
# res=Poly(n)
# print(res)        


# def CountD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# n=int(input('entr numb'))    
# res=CountD(n)
# print(res)



def countD(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
def Amstrong(n):
    tem=n
    sum=0
    power=countD(n)
    while n!=0:
        rem=n%10
        sum=(sum+rem**power)
        n//=10
    if sum==tem:
        return True
    else:
        return False
        
n=int(input('enter a nub'))            
float=Amstrong(n)
if float==True:
    print('amst')
else:
    print('nir')    