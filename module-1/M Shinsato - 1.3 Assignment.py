# Miles Shinsato 10/26/2024 Module 1.3 Assignment

# The purpose of this code is create a countdown function that replicates the song "100 Bottles of Beer on the Wall"

# Defining function that will count down the bottles of beer on the wall
def beer_countdown(bottles):

    # Setting function that will act when bottles are more than 0
    while bottles > 0:

        # If statement for when there more than one bottle of beer
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        # Else statement for when it is only 1 bottle of beer on the wall left
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")

        # Takes away 1, shown as -1, from the bottle variable and displays this message
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")

    # Final message when bottles variable count reaches 0
    print("Time to buy more bottles of beer.")

# Defining main function that will start the program
def main():

# Creating a True loop to repeat the program if there is an invalid input
    while True:

        # Using try / except function to allow for an error message if the user puts in a negative variable
        try:

            # Establishing value of bottles variable
            bottles = int(input("Enter number of bottles: "))

            # Setting message for if the bottles variable is set to 0
            if bottles <= 0:

                # Print message to show when negative number is input
                print("Please enter a positive number of bottles.")

            # Else function that will start the beer_countdown function after bottles variable is checked to be number greater than 0
            else:
                beer_countdown(bottles)

                # Create break to end the program and prevent infinite loop
                break

       # Except function being used to cover if there is not a valid number input
        except ValueError:

            # Print message to show when a valid numer is not entered
            print("Please enter a valid number.")


# Run the main program
main()
