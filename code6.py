# num  =  11
# is_prime =  True 
# 
# for i in  range(2,num):
#    if num % i == 0:
#     is_prime = False 
#     break
# 
# if is_prime:
#   print(num , "is a Prime Number ")
# else:
#   print(num , "is not a Prime Number" )  

# row  =  7
# 
# for i in range(1 , row + 1):
#     print(i* "*")

# name  =  "PYTHON"
# reversed_name  =  ""
# 
# for i in name:
#     reversed_name =  i + reversed_name
# print(reversed_name) 
# 
# table  =  15
# for i in range(1 , 11):
#      print( table , " * " , i , " = " ,i * table)

# 3 * 1 = 3
# 3 * 2  = 6
#  "P"+"" =  "p"
# "Y"+"P" =  "yp"
# "t"+"yp" =  "typ"
# "h"+"typ" = "htyp"
# "o"+"htyp" =  "ohtyp"
# "n"+ "ohtyp" =  "nohtyp"
#  output  =  "nohtyp"

    # nohtyp

# a = 0
# b  = 1
# for i in range(10):
#   print(a , end=" ")
#   next_value  = a + b
#   a = b
#   b= next_value



# a     b    = next_value
# 0     1    = 1
# 1     1    = 2
# 1     2    = 3

total_sum = 0
for i in  range(1 , 6):
    square  =  i * i
    total_sum = total_sum + square
    # total_sum =+square
    print(i , " :  " ,square)
print(total_sum)    