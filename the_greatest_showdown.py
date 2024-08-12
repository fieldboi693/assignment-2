# Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "


# https://www.w3schools.com/python/ref_func_max.asp
# https://www.w3schools.com/python/ref_func_min.asp

# Input number 
# min = min(x, y, z)
# print("min is" + min)

# THIS CODE FOR GREATEST NUMBER
# num1=4
# num2=6
# num3=8
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))

#THIS CODE FOR THE SMALLEST NUMBER     
if num1>=num2 and num1>=num3:
    print(num1, "Is the greatest!")
elif num2>=num1 and num2>num3:
    print(num2,"Is greatest!")
else:
    print(num3,"Is the greatest!")



if num1<=num2 and num1<=num3:
    print(num1, "Is the smallest!")
elif num2<=num1 and num2<num3:
    print(num2,"Is the smallest!")
else:
    print(num3,"Is the smallest!")

