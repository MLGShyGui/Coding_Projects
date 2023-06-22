# Create a magic 8 ball program that will respond to questions. This one is static to try and match the expected output better, but I could add an input() area to make it dynamic.
import random
Name = "Joe"
Question = "Is this real life?"
Answer1 = "Yes - definitely"
Answer2 = "It is decidedly so"
Answer3 = "Without a doubt"
Answer4 = "Reply hazy, try again"
Answer5 = "Ask again later"
Answer6 = "Better not tell you now"
Answer7 = "My sources say no"
Answer8 = "Outlook not so good"
Answer9 = "Very doubtful"
Answer = random.randint(1,9)
if Answer == 1:
  print(Name + " asks: " + Question + "\n" + "Magic      8-Ball's answer: " + Answer1)
elif Answer == 2:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer2)
elif Answer == 3:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer1)
elif Answer == 4:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer4)
elif Answer == 5:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer5)
elif Answer == 6:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer6)
elif Answer == 7:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer7)
elif Answer == 8:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer8)
elif Answer == 9:
  print(Name + " asks: " + Question + "\n" + "Magic 8-Ball's answer: " + Answer9)
