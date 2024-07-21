# def binary_to_decimal(binary_str):
#     # Initialize decimal number
#     decimal_number = 0
    
#     # Reverse the binary string for easier calculation
#     binary_str = binary_str[::-1]
    
#     # Loop through the binary string
#     for i in range(len(binary_str)):
#         # Convert binary digit to decimal and add to the decimal_number
#         if binary_str[i] == '1':
#             decimal_number += 2 ** i
    
#     return decimal_number

# # Input binary number as a string
# binary_str = input("Enter a binary number: ")

# # Convert and print the decimal number
# decimal_number = binary_to_decimal(binary_str)
# print(f"The decimal equivalent of binary {binary_str} is {decimal_number}")





# def Reverse(n):
#     if (n==0):
#         return 0
#     return n+Reverse(n-1)
# n=int(input('en'))
# res=Reverse(n)
# print(res)