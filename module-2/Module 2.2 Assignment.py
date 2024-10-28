# Miles Shinsato 09/21/2024 Module 7.2 Assignment

# greeting message to prompt for name input by the user
print ('Hello! I will need to collect some information regarding names')

# prompt to collect the user input name
full_name = input('What is the full name you wish to enter? ')

# define function to gather name and get initials
def get_initials():

  # prompt to split names separated by spaces
  name_parts = full_name.split()

  # calling first character of each name and adding a '.' after each
  initials = ". ".join(part[0] for part in name_parts)

  # prompt to add a '.' after the last initial
  initials += "."

  # print to give results for input
  print(f'Here are the adjusted initials: {initials}')

# close out the function
get_initials()

# simple thank you message
print ('Thank you and have a good day!')
