import random

def generate_rap_name(name, birthplace, favorite_animal, month_of_birth):

  # below creates a list of  rap names
  possible_rap_names = []

  # this will add the person's name to the list
  possible_rap_names.append(name)

  # this wil add where they were born to the list
  possible_rap_names.append(birthplace)

  #  favorite animal to the list function below
  possible_rap_names.append(favorite_animal)

  #  month of the birth to the list
  possible_rap_names.append(month_of_birth)

  # the below mixes/shuffles up the list options
  random.shuffle(possible_rap_names)

  #  this will combine the first 2 elements of the list to create the rap name for the person
  rap_name = possible_rap_names[0] + " " + possible_rap_names[1]

  # this is the retun function so it goes back
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
