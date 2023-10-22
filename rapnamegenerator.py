import random

def generate_rap_name(name, birthplace, favorite_animal, month_of_birth):

  # Create a list of possible rap names
  possible_rap_names = []

  # Add the person's name to the list
  possible_rap_names.append(name)

  # Add the person's birthplace to the list
  possible_rap_names.append(birthplace)

  # Add the person's favorite animal to the list
  possible_rap_names.append(favorite_animal)

  # Add the month of the person's birth to the list
  possible_rap_names.append(month_of_birth)

  # Shuffle the list
  random.shuffle(possible_rap_names)

  # Combine the first two elements of the list to create the rap name
  rap_name = possible_rap_names[0] + " " + possible_rap_names[1]

  # Return the rap name
  return rap_name

# Get the user's inputs
name = input("Enter your name: ")
birthplace = input("Enter your birthplace: ")
favorite_animal = input("Enter your favorite animal: ")
month_of_birth = input("Enter your month of birth: ")

# Generate the rap name
rap_name = generate_rap_name(name, birthplace, favorite_animal, month_of_birth)

# Prinrap the rap name
print("Your rap name is:", rap_name)
