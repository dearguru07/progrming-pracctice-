# def CountD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count
# def Amsrrong(n):
#     tem=n
#     sum=0
#     power=CountD(n)
#     while n!=0:
#         rem=n%10
#         sum=sum+rem**power
#         n=n//10
#     if tem==sum:
#         return True
#     else:
#         return False
# n=int(input('enter a num'))        
# float=Amsrrong(n)
# if float==True:
#     print('amsrtg')
# else:
#     print('not a amrsh')    


# def Polyn(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# n=int(input('entrer an numb'))    
# res=Polyn(n)
# if res==n:
#     print('poly')
# else:
#     print('not')    

   
    
def Count(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
n=int(input('entr a numb'))     
res=Count(n)
print(res)
