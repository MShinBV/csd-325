# Miles Shinsato 11/10/2024 Module 4.2 Assignment


# This program is made to show a graph based on a provided CSV file.
# Based on the user's input, it will show a graph of either high or low temperatures.

import csv
from datetime import datetime

# MS: using import sys to allow for a clean exit when calling to sys.exit() at the end
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    # MS: Added a variable to get lows from the file as well.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])

        # MS: Added a data extraction for low temperatures from column 6 in the CSV file
        low = int(row[6])
        highs.append(high)

        # MS: Added lows.append(low) to add the integers to the low list
        lows.append(low)

# MS: Created a function to plot points based on the user choice
def plot_temperatures(temp_type):

    fig, ax = plt.subplots()

    # MS: Added if loop for when user inputs for temp_type to be 'highs'
    if temp_type == 'highs':
        # MS: Formatting the plot graph to be red
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)

    # MS: elif loop for when the user inputs for temp_type to be 'lows'
    elif temp_type == 'lows':

        # MS: Formatting the plot graph to be blue for lows
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)

    # MS: Format the plot graph
    plt.xlabel('', fontsize=16)

    # MS: Auto-formatting the date labels
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # MS: to display the plot
    plt.show()


# MS: Printing a welcome menu to explain the program
# MS: Adding this outside of the main loop so that it does not repeat when an invalid entry is given
print("Hello and welcome!")
print("\nThis program will display a graph for either the 'high' or 'low' temperatures based on what you choose.")

# MS: Main loop for the program
while True:

    # MS: Display menu options for the user to make the choice for highs, lows, or to exit
    print("\nPlease select an option:")
    print("1. View high temperatures")
    print("2. View low temperatures")
    print("3. Exit")

    # MS: Variable for choice for user input
    choice = input("Enter your choice (1, 2, or 3): ")

    # MS: Creating if, elif, elif, else loop for user input behavior

    # MS: Will call to plot_temperatures function to graph the highs
    if choice == '1':
        plot_temperatures('highs')

    # MS: Will call to plot_temperatures function to graph the lows
    elif choice == '2':
        plot_temperatures('lows')

    # MS: Prompt for when the user decides to exit the program
    elif choice == '3':
        print("Thank you for using the temperature viewer.")
        print("Have a good one and goodbye!")

        # MS: Calls to end the program
        sys.exit()

    # MS: Display for when an invalid input is given
    else:
        print("Invalid input. Please enter only 1, 2, or 3.")
