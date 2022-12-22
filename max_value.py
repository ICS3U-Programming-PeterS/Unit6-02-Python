#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 14 2022
# This program asks the user to enter a decimal
# it then sends it to a function then rounds it
import random
import constants


# function that finds the max value
def find_max_value(list):
    # Initialize max value to the first element in the list
    max_value = list[0]

    # Loop through the rest of the elements in the list
    for index in range(constants.MAX_ARRAY_SIZE):
        # If the current element is greater than the max value
        # update the max value
        if list[index] > max_value:
            max_value = list[index]

    # return the max value to main
    return max_value


def main():
    # Make an empty list
    list_of_int = []

    # Loops through 10 times to generate ten random numbers
    for counter in range(constants.MAX_LIST_SIZE):
        # Generates a random number from (0-100) and added it to a list
        list_of_int.append(random.randint(constants.MIN_NUM,
                                          constants.MAX_NUM))

        # Displays to console what number was added to the list and what
        # position it is at
        print(f"{list_of_int[counter]} added to list at position {counter}")

    # Calls function to find the highest number in the list
    max_number = find_max_value(list_of_int)

    # Displays the max number to the console
    print(f"The max value is: {max_number}")


if __name__ == "__main__":
    main()
