import random

def generate_random_number():
  return random.randint(1, 10)

def play_number_guessing_game():
  """Plays a number guessing game with the user.

  The user has 5 guesses to guess a randomly generated number between 1 and 10.
  """

  # below will create a random number 
  random_number = generate_random_number()

  # select the the number of guesses
  number_of_guesses = 0

  # this is the introductory message I have added in brand new. 
  print("Welcome to the Guess the Number game! You will have 5 chances to guess the correct number.")

  # will loop the game 5 times for time saving purposes
  while number_of_guesses < 5:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 10: "))

    #  the below code will confirm if the guess is correct or not
    if guess == random_number:
      print("You guessed correctly! Congratulations!")
      break

    # Check if the guess is too high/low - help the end user 
    elif guess > random_number:
      print("Your guess is too high.")
    else:
      print("Your guess is too low.")

    # Increment the number of guesses
    number_of_guesses += 1

  # If the user runs out of guesses, the below code will tell the user the correct answer
  if number_of_guesses == 5:
    print("You ran out of guesses. The correct answer was", random_number)

# Play the game
play_number_guessing_game()
