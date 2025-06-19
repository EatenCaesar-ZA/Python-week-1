# Control Statements

num = 0

if num > 0:
    print("The number is positive.")
else:
    print("The number is Negative.")
    
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")    
    else:
        print("The number is negative.")
        
 # input from user
 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num1 ,"is greater than", num2)
elif num1 < num2:
    print(num1 ,"is less than", num2)
else:
    print(num1 ,"is equal to", num2)       