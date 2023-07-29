print("#####  Larger Sum #####")
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums,
# afterwards we will compare the two and return which one has a greater sum.
#Write your function here
def larger_sum(lst1, lst2):
  a = 0
  b = 0
  for i in lst1:
    a += i
  for i in lst2:
    b += i
  if b > a:
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))


print("##### Over 9000  #####")
# We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000.
# Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens,
# we should stop adding the numbers and return the value where we stopped.
#Write your function here
def over_nine_thousand(lst):
  limit = 0
  for i in lst:
    if lst == []:
      break
    if limit > 9000:
      break
    else:
      limit += i
  return limit


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


print("##### Max Num  #####")
# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python,
# but as a challenge, we are going to manually implement this function. 
#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


print("##### Same Values  #####")
# In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values,
# if the numbers are equal, then we record the index.
#Write your function here
def same_values(lst1, lst2):
  count = 0
  new_list = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_list.append(i)
  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


print("#####  Reversed List #####")
# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this,
# but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list.
#Write your function here
def reversed_list(lst1, lst2):
  if lst1 == lst2[::-1]:
    return True
  return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
