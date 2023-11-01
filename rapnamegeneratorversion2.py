import random

def generate_rap_name(name, birthplace, favorite_animal, favorite_color, favorite_food, month_of_birth):

  # list of possible rap names - same again 
  possible_rap_names = []

  # person's name to the list - - same again
  possible_rap_names.append(name)

  # where the person was born  - same again
  possible_rap_names.append(birthplace)

  # Add the person's favorite animal to the list - - same again
  possible_rap_names.append(favorite_animal)

  # person's favorite color to the list - new to the list
  possible_rap_names.append(favorite_color)

  # person's favorite food to the list - new to the list 
  possible_rap_names.append(favorite_food)

  # month of the person's birth to the list - same again
  possible_rap_names.append(month_of_birth)

  # Shuffle the list = same functio nas last time to randomise the lsit options
  random.shuffle(possible_rap_names)

  #  now the below will let me combine 3 elements instead of 2 for the final rap name
  rap_name = possible_rap_names[0] + " " + possible_rap_names[1] + " " + possible_rap_names[2]

  # Return the rap name
  return rap_name

# get user info based on the below inputs only
name = input("Enter your name: ")
where they are born = input("Enter your birthplace: ")
favorite animal = input("Enter your favorite animal: ")
favorite color = input("Enter your favorite color: ")
favorite food = input("Enter your favorite food: ")
month born = input("Enter your month of birth: ")

# Generate the rap name
rap_name = generate_rap_name(name, birthplace, favorite_animal, favorite_color, favorite_food, month_of_birth)

# Print the rap name
print("Your rap name is:", rap_name)
