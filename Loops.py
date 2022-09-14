# break Keyword

numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)
  
# 0
# 254
# 2
# Negative number detected!

# Python List Comprehension

# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]

print(result)
# [0, 4, 16, 36, 64]

# Python For Loop

for <temporary variable> in <list variable>:
  <action statement>
  <action statement>
 
#each num in nums will be printed below
nums = [1,2,3,4,5]
for num in nums: 
  print(num)
  
# The Python continue Keyword

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

# Python Loops with range().

# Print the numbers 0, 1, 2:
for i in range(3):
  print(i)

# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")
  
### Infinite Loop
""" An infinite loop is a loop that never terminates. 
Infinite loops result when the conditions of the loop prevent it from terminating. 
This could be due to a typo in the conditional statement within the loop or incorrect logic. 
To interrupt a Python program that is running forever, press the Ctrl and C keys together on your keyboard.
""""

# Python while Loops

# This loop will only run 1 time
hungry = True
while hungry:
  print("Time to eat!")
  hungry = False

# This loop will run 5 times
i = 1
while i < 6:
  print(i)
  i = i + 1
  
# Python Nested Loops

groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)


