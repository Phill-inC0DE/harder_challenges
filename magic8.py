import random

# you guessed it is a magic 8 ball. 
# type in your name and question before running the code.

name = "Phil"
question = "Are you okay?"
answer = ""
random_number = random.randint(1, 12)

#print(random_number)

if random_number == 1:
  answer = "Yes, definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Don't be ridiculous."
elif random_number == 10:
  answer = "Abso-frickin-lutely."
elif random_number == 11:
  answer = "Nay."
elif random_number == 12:
  answer = "Yeeeeh, obviously."
else:
  answer = "Error"

if not name == "" and not question == "":
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
elif name == "" and not question == "":
  print("Question:", question)
  print("Magic 8-Ball's answer:", answer)
elif question == "" and not name == "":
  print(name, "You need to ask a question.")
else:
  name == "" and question == ""
  print("Who's there? do you have a question.")
 