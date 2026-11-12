import random
number = random.randint(1, 100)
"guess a number from 1 to 100"
while True:
  guess= int(input("enter your guess: "))
  if guess > number:
    print("too high try again")
  elif guess < number:
    print("too low try again")
  else:
    print(" great job you got it")
    break



