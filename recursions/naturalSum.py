
# def sum(n):
#     if n==1:
#         return n
#     return n+sum(n-1)
# n=int(input('enter a number'))
# res=sum(n)
# print(res)


# def Product(n):
#     if n==1:
#         return n
#     else:
#         return n*Product(n-1)
# n=int(input('enter a number'))
# res=Product(n)
# print(res)


def Count(n,initial):
    if n==0:
        return n
    n//=10
    initial+=1
    return Count(n,initial)
n=int(input('enter a number'))
res=Count(n,0)
print(res)