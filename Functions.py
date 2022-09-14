# Function Parameters

def write_a_book(character, setting, special_skill):
  print(character + " is in " + 
        setting + " practicing her " + 
        special_skill)
  
# Multiple Parameters

def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I'm ready for school!")

# Function

# Define a function my_function() with parameter x

def my_function(x):
  return x + 1

# Invoke the function

print(my_function(2))      # Output: 3
print(my_function(3 + 5))  # Output: 9
Function Indentation

# Calling Functions

doHomework()

# Function Arguments

def sales(grocery_store, item_on_sale, cost):
  print(grocery_store + " is selling " + item_on_sale + " for " + cost) 

sales("The Farmer’s Market", "toothpaste", "$1")

# Function Keyword Arguments

def findvolume(length=1, width=1, depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)

# Returning Multiple Values

def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  # Return all three values:
  return x_squared, y_squared, z_squared

three_squared, four_squared, five_squared = square_point(3, 4, 5)

# The Scope of Variables

a = 5

def f1():
  a = 2
  print(a)
  
print(a)   # Will print 5
f1()       # Will print 2

# Returning Value from Function

def check_leap_year(year): 
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."

year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2018 is not a leap year.

# Global Variables

a = "Hello"

def prints_a():
  print(a)
  
# will print "Hello"
prints_a()

# Parameters as Local Variables

def my_function(value):
  print(value)   
  
# Pass the value 7 into the function
my_function(7) 

# Causes an error as `value` no longer exists
print(value) 