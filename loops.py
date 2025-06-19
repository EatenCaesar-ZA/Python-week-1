# loops
# for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# while loop is used to execute a block of code as long as a condition is true

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
    numbers = [1, 2, 3, 5, 7]
    for number in numbers:
        print(number)
        
# Using a while loop

count = 1

while count <= 5:
    print(count)
    count += 1  # Increment count by 1 
    
    # control statements in loops
    
    fruits = ["apple", "banana", "cherry","date"]
for fruit in fruits:
    if fruit == "cherry":
        break  # Skip the rest of the loop for this iteration
    print(fruit)       
    
    for fruit in fruits:
      if fruit == "cherry":
        continue  # Skip the rest of the loop for this iteration
        print(fruit)       
        
    for fruit in fruits:
        if fruit == "cherry":
            pass  # Do nothing for this iteration
        print(fruit)  # This will still print all fruits, including "cherry"
    
    