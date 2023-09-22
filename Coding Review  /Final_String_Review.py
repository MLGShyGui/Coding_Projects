print("### 1. Count Letters ###")
# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters 
# should be counted as different letters.

# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  total = 0
  temp = []
  for i in word:
    if i in letters and not i in temp:
      temp.append(i)
      total+=1
  return total
#Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# I like how efficient CodeAcademy's solution was so I'm putting it here in comments to document it. They didn't loop off the parameter word, but the alphabet variable, to make sure every letter was only 
# checked once. My solution to that was to add every letter checked to a new list and check if the next letter was new based on if it was in that list, inefficient.

# def unique_english_letters(word):
#   uniques = 0
#   for letter in letters:
#     if letter in word:
#       uniques += 1
#   return uniques

print("### 2. Count X ###")

# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

# Write your count_char_x function here:
def count_char_x(word, x):
  temp = 0
  for i in word:
    if x == i:
      temp += 1
  return temp
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Upon completing this challange I just knew python would have a built in function for this exact challange to one line it, so I found the function "word.count(x)". This would get rid of the need for this function.

print("### 3. Count Multi X ###")

# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - 
# it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  temp = word.split(x)
  return len(temp) -1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# This again isn't needed as # return "word.count(x)" does the job for us, but I understand they want me to think through these puzzles to understand the logic and problem solving.

print("### 4. String Between ###")

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  temp = word.find(start)
  temp2 = word.find(end)
  if temp > -1 and temp2 > -1:
    return word[temp+1:temp2]
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# This was testing my understanding of list slices. I did need to look at a hint as its been a while since I worked with list slices, but the more I use it the more I'll remember it as well as everything else.

print("### 5. X Length ###")

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(' ')
  for i in range(len(words)):
    if x > len(words[i]):
      return False
  return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
