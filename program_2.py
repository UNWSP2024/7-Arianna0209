# Title: List of Numbers Larger than n
# Author: Arianna Endres
# Date: 10/15/2025

# This program displays all the numbers in a list that are greater than a certain number n.

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)


def display_larger_than_n_list(n, n_list):
    # This function displays all the numbers in the list that are greater than n.

    # Create new list with only the numbers greater than n.
    numbers_greater_than_number = [item for item in n_list if item > n]

    # Display the list.
    print(numbers_greater_than_number)


# Call the main function.
if __name__ == '__main__':
    main()