
# lambda or unanymus -----------------

# f=lambda a,b:a+b
# res=f(4,7)
# print(res)

# filter------------

# def is_even(n):
#    return n%2==0
# nums=(1,5,4,6,8,2,4,7)
# even=list(filter(is_even,nums))
# print(even)


# nums=(1,5,4,6,8,2,4,7)
# even=list(filter(lambda n:n%2==0,nums))
# print(even)

# map----------------


# def double(n):
#     return n*2
# nums=(1,5,4,6,8,2,4,7)
# double=list(map(double,nums))
# print(double)


# nums=(1,5,4,6,8,2,4,7)
# double=list(map(lambda n:n*2,nums))
# print(double)


# reduce---------------------

# from functools import reduce


# def sum(a,b):
#     return a+b
# nums=(1,5,4,6,8,2,4,7)
# sumv=reduce(sum,nums)
# print(sumv)


# nums=(1,5,4,6,8,2,4,7)
# sumv=reduce(lambda a,b:a+b,nums)
# print(sumv)