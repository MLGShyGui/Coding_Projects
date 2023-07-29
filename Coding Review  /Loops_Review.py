print("#####  Divisible By Ten #####")
# Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers.
# This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10,
# a counter will be incremented and the final count will be returned.
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i % 10 == 0:
      count += 1
    else:
      continue
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


print("#####  Greetings #####")
# You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge,
# we will take a list of names and prepend the string 'Hello, ' before each name. 
#Write your function here
def add_greetings(names):
  my_list = []
  for i in names:
    my_list.append("Hello, " + i)
  return my_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


print("##### Delete Starting Even Numbers  #####")
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements.
# It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed.
#Write your function here
def delete_starting_evens(my_list):
  for i in my_list:
    if my_list[0] % 2 == 0:
      my_list = my_list[1:]
    else:
      continue
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


print("#####  Odd Indices #####")
# This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. 
#Write your function here
def odd_indices(my_list):
  count = 0
  new_list = []
  for i in my_list:
    if count % 2 == 1:
      new_list.append(i)
      count += 1
    else:
      count +=1
  return new_list


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


print("#####  Exponents #####")
# In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list,
# we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers.
#Write your function here
def exponents(bases, powers):
  new_list = []
  for index in bases:
    for index2 in powers:
      new_list.append(index ** index2)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
