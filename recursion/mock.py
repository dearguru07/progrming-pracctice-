# vice versa------------------------

# a="Hello world"
# b=a.swapcase()
# print(b)

# swapping----------

# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

# string reversing --------

# a="gurucharan"
# b=a[::-1]
# print(b)

# list reversing---------


# a=[1,5,47,8,"guru"]
# b=a[::-1]
# print(b)


# how to access the elements in tuples------------------------------



# tuple=('gm',2,"guru",'hello',3.54,(10,20,45),(2,3,7),2)

# 1.indexing1----------
 
# print(tuple[2])
# print(tuple[4])

# 2.Negitive indexing------

# print(tuple[-1])
# print(tuple[-5])
# print(tuple[-6])

# 3.Sliceing-----------

# print(tuple[1:4])
# print(tuple[::])
# print(tuple[0:6:-1])
# print(tuple[::-1])

# 4.Loopins----------

# for i in tuple:
#     print(i)

# 5.access with nested tuples------------

# print(tuple[5])
# print(tuple[7])
# print(tuple)

# ---------------------------------------------------------------------------------


# list=[1,2,"guru",'hello',3.54]
# print(list[4])






# unpacking of tuples-----------------------


# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a)  
# print(b)  
# print(c) 


# my_tuple = (1, 2, 3, 4, 5)
# a, b, _ = my_tuple[:3]
# print(a)  # Output: 1
# print(b)  # Output: 2
 


# my_tuple = (1, 2, 3, 4, 5)
# a, b, *rest = my_tuple
# print(a)     # Output: 1
# print(b)     # Output: 2
# print(rest)  # Output: [3, 4, 5]



# list=[1,2,5,"hello",'world']
# res=tuple(list)
# print(res)


# str1="hello"
# str2="world"
# # op=str1+str2
# # print(op)

# res=" ".join([str1,str2])
# print(res)

# tuple=(1,5,7,95,1)
# list=[tuple]
# list.append(45)
# print(list) 


# # Reading from a file
# with open('example.txt', 'r') as f:
#     content = f.read()
#     print(content)

# # Writing to a file
# with open('example.txt', 'w') as f:
#     f.write('Hello, world!')

# # Appending to a file
# with open('example.txt', 'a') as f:
#     f.write('\nAppended text.')

# # Reading and writing to a file
# with open('example.txt', 'r+') as f:
#     content = f.read()
#     f.write('\nMore text.')


# import pip
import pickle

mylist=['guru','charan']
with open('textdat.tex','wb') as f:
    pickle.dump(mylist,f)
    
    
unpic=open('text.tex','rb')
res=pickle.load(unpic)
print(res)


