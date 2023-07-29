print("##### Tenth Power  #####")
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number.
# Write your tenth_power function here:
def tenth_power(num):
  return num**10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


print("##### Square Root  #####")
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. 
# Write your square_root function here:
def square_root(num):
  return round(num ** .5)
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


print("##### Win Percentage  #####")
# Next, we will create a function which calculates the percentage of games won. In order to do this,
# we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters,
# the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100).
# Write your win_percentage function here:
def win_percentage(wins, losses):
  total = wins + losses
  return (wins / total) * 100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


print("#####  Average #####")
# Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. 
# Write your average function here:
def average(num1, num2):
  return (num1+num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


print("##### Remainder  #####")
# For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them.
# We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder.                                                                                                    
# Write your remainder function here:
def remainder(num1, num2):
  return (num1*2) % (num2/2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
