# To switch the values of the 2 variables given to us
# I here used the approch of using the temp variable for swapping the variable values
# with each other.

print("A simple program to switch the values of 2 variables using temp variable GG")
a = input("A simple variable enter please : ")
print("The val of variable a is : " + a)
b = input("A simple variable enter please : ")
print("The val of variable b is : " + b)
temp = 0
temp = a
a = b 
b = temp
print("The new value of variable a is : " + a + " and the new value of variable b is : " + b)