print("##### Append Size  #####")
# For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list.
#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


print("#####  Append Sum #####")
# Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end.
# After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. 
#Write your function here
def append_sum(my_list):
  for i in range(3):
    my_list.append(my_list[-1]+my_list[-2])
  return my_list

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


print("#####  Larger List #####")
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, 
# then we need to return the ID of the last item on that belt.
# In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists.
#Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) < len(my_list2):
    return my_list2[-1]
  else:
    return my_list1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


print("##### More Than N  #####")
# Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type.
# We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack),
# a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt).
# The function will return True if the snack we are searching for appears more times than we provided as our third parameter. 
#Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



print("#####  Combine Sort #####")
# Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call.
#Write your function here
def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  new_list.sort()
  return new_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
