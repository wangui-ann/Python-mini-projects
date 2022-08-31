import random

randomNumber = random.randint(1, 9)
chances = 0

print("Guess a number between 1 and 9: ")
while True:
  #User is prompted to enter their guess
  guess = int(input())
  #User has a maximum of 5 chances
  while chances < 6
    if guess = randomNumber:
      print(f"CONGRATULATIONS! YOU CORRECTLY GUESSED THE NUMBER {randomNumber} IN {chances} ATTEMPTS!")
      break
    elif guess < randomNumber:
      print(f"Your guess {guess} is too low. Try a higher number.")
      chances += 1
    elif guess > randomNumber:
      print(f"Your guess {guess} is too high. Try a lower number.")
      chances += 1
