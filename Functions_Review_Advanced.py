print("#####  First Three Multiples #####")
# Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. 
# This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number.
# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


print("#####  Tip #####")
# Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage.
# This function will accept both of those values as inputs and return the amount of money to tip. 
# Write your tip function here:
def tip(total, percentage):
  return total * (percentage/100)
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


print("#####  Bond, James Bond #####")
# It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want.
# The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs.
# Write your introduction function here:
def introduction(first_name, last_name):
  return "{}, {} {}".format(last_name, first_name, last_name)
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou


print("##### Dog Years  #####")
# Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years.
# It will calculate the age of the dog in dog years and return a string describing the dog’s age. 
# Write your dog_years function here:
def dog_years(name, age):
  age = age * 7
  return "{}, you are {} years old in dog years".format(name, age)
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


print("#####   #####")
